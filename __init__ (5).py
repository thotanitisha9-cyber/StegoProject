import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import cv2
import os
from PIL import Image
from skimage import data, util, color
from sklearn.ensemble import RandomForestClassifier
from scipy.signal import convolve2d
from rich.progress import track
from src.ml.shallow_net import ShallowNet
import warnings

warnings.filterwarnings("ignore")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.manual_seed(42)
np.random.seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed(42)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# ==============================================================================
# PART 2: REALISTIC DATASET GENERATION (Fixed Normalization)
# ==============================================================================

class RealisticStegoGenerator:
    def __init__(self, patch_size=64):
        self.patch_size = patch_size
        # Normalize ALL base images to float [0, 1] to avoid type mismatches
        self.base_images = [
            util.img_as_float(color.rgb2gray(data.astronaut())),
            util.img_as_float(data.camera()),
            util.img_as_float(data.moon()),
            util.img_as_float(data.coins()),
            util.img_as_float(color.rgb2gray(data.chelsea())),
            util.img_as_float(color.rgb2gray(data.coffee()))
        ]

    def create_patches(self, num_samples):
        patches = []
        while len(patches) < num_samples:
            img = self.base_images[np.random.randint(len(self.base_images))]
            h, w = img.shape
            if h < self.patch_size or w < self.patch_size: continue
            
            x = np.random.randint(0, w - self.patch_size)
            y = np.random.randint(0, h - self.patch_size)
            patch = img[y:y+self.patch_size, x:x+self.patch_size]
            patches.append(patch)
        return np.array(patches)

    def adaptive_embedding(self, cover_patches, payload_density):
        """Simulates J-Uniward: Embeds in textures (edges), avoids smooth areas."""
        stego_patches = []
        for cover in cover_patches:
            # Safe conversion for Canny (requires uint8 0-255)
            cover_ubyte = (cover * 255).astype(np.uint8)
            
            # 1. Texture Map (Edges)
            edges = cv2.Canny(cover_ubyte, 100, 200) / 255.0
            
            # 2. Generate Payload Noise
            noise = np.random.normal(0, 0.5, cover.shape)
            
            # 3. Adaptive Embedding Logic
            if payload_density <= 0.1:
                # Low Payload: Only embed in edges + tiny background noise
                embedding = noise * (edges + 0.15) * 0.08 
            else:
                # High Payload: Embed everywhere
                embedding = noise * 0.15 
                
            stego = cover + embedding
            
            # Clip to ensure valid image range [0, 1]
            stego = np.clip(stego, 0.0, 1.0)
            stego_patches.append(stego)
            
        return np.array(stego_patches)

def load_real_data(root_dir, patch_size=64):
    """Load real cover and stego images from multiple dataset directories."""
    X_real = []
    y_real = []
    
    # Define dataset paths to check
    # Format: (base_dir, cover_sub, stego_sub)
    sources = [
        (os.path.join(root_dir, "NewDataset"), "cover", "stego"),
        (os.path.join(root_dir, "Dataset"), "clean_images", "stego_images")
    ]

    def process_images(directory, label):
        patches = []
        if not os.path.exists(directory):
            return []
            
        for fname in os.listdir(directory):
            if not fname.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')): continue
            
            try:
                path = os.path.join(directory, fname)
                img = Image.open(path).convert('L') # Grayscale
                
                # Resize if too small
                if img.width < patch_size or img.height < patch_size:
                    img = img.resize((patch_size, patch_size))
                
                # Extract multiple patches per image to boost dataset size & variety
                # Random crops + Center + Corners to catch stego noise anywhere
                w, h = img.size
                
                # 1. Center
                coords = [(w//2 - 32, h//2 - 32)]
                
                # 2. Corners
                coords.extend([
                    (0, 0), (w-patch_size, 0),
                    (0, h-patch_size), (w-patch_size, h-patch_size)
                ])
                
                # 3. Random Crops (3 per image)
                for _ in range(3):
                    rx = np.random.randint(0, max(1, w - patch_size))
                    ry = np.random.randint(0, max(1, h - patch_size))
                    coords.append((rx, ry))
                
                for x, y in coords:
                    x = max(0, min(x, w - patch_size))
                    y = max(0, min(y, h - patch_size))
                    patch = img.crop((x, y, x+patch_size, y+patch_size))
                    
                    patch_arr = np.array(patch).astype(np.float32) / 255.0
                    patches.append(patch_arr)
            except Exception as e:
                # print(f"Error processing {fname}: {e}")
                pass
                
        return patches

    for base_path, cov_name, steg_name in sources:
        cover_dir = os.path.join(base_path, cov_name)
        stego_dir = os.path.join(base_path, steg_name)
        
        if os.path.exists(cover_dir) and os.path.exists(stego_dir):
            print(f"Loading real data from: {base_path}")
            covers = process_images(cover_dir, 0)
            stegos = process_images(stego_dir, 1)
            
            if covers and stegos:
                # Balance classes per source
                min_len = min(len(covers), len(stegos))
                covers = covers[:min_len]
                stegos = stegos[:min_len]
                
                X_real.extend(covers)
                y_real.extend([0] * len(covers))
                X_real.extend(stegos)
                y_real.extend([1] * len(stegos))
                print(f"  - Added {len(covers)} pairs.")

    return np.array(X_real), np.array(y_real)

def get_dataset(num_samples=2000, payload=0.1):
    # 1. Generate Synthetic Data
    gen = RealisticStegoGenerator()
    covers = gen.create_patches(num_samples // 2)
    stegos = gen.adaptive_embedding(covers, payload)
    
    X_syn = np.concatenate([covers, stegos])
    y_syn = np.concatenate([np.zeros(len(covers)), np.ones(len(stegos))])
    
    # 2. Load Real Data from ALL sources
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    X_real, y_real = load_real_data(root_dir)
    
    if len(X_real) > 0:
        print(f"Merging {len(X_real)} real patches with {len(X_syn)} synthetic patches.")
        X = np.concatenate([X_syn, X_real])
        y = np.concatenate([y_syn, y_real])
    else:
        print("No real data found in Dataset/ or NewDataset/. Using synthetic only.")
        X, y = X_syn, y_syn
    
    # Reshape (N, 1, H, W) and ensure Float32
    X = X[:, np.newaxis, :, :].astype(np.float32)
    
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=0.2, random_state=42)

# ==============================================================================
# PART 3: BASE PAPER (Random Forest + DCTR)
# ==============================================================================
class BasePaperSystem:
    def __init__(self):
        self.clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)

    def extract_dctr(self, images):
        features = []
        # KV Kernel approximation
        kernel = np.array([[-1, 2, -1], [2, -4, 2], [-1, 2, -1]])
        for img in images:
            img = img.squeeze()
            res = convolve2d(img, kernel, mode='same', boundary='symm')
            # Histogram Features (Global)
            hist, _ = np.histogram(res, bins=32, range=(-2, 2), density=True)
            features.append(hist)
        return np.array(features)

    def run(self, X_train, y_train, X_test):
        X_train_f = self.extract_dctr(X_train)
        X_test_f = self.extract_dctr(X_test)
        self.clf.fit(X_train_f, y_train)
        probs = self.clf.predict_proba(X_test_f)[:, 1]
        preds = self.clf.predict(X_test_f)
        return preds, probs

# ==============================================================================
# PART 4: PROPOSED SYSTEM (Fixed & Scaled)
# ==============================================================================

# 4.1 SRM Kernels
def srm_init_weights():
    w = []
    # 1. Spam
    k1 = np.zeros((5,5)); k1[:,2] = [-1, 2, -1, 2, -1] 
    w.append(k1)
    # 2. MinMax
    k2 = np.zeros((5,5)); k2[2,2]=1; k2[2,3]=-1
    w.append(k2)
    # 3. Edge
    k3 = np.array([[-1, 2, -1], [2, -4, 2], [-1, 2, -1]]) 
    k3 = np.pad(k3, 1) 
    w.append(k3)
    # Replicate to 16 channels
    weights = np.array(w * 6)[:16] 
    return torch.from_numpy(weights).float().unsqueeze(1)

# 4.2 Attention Module
class ECA(nn.Module):
    def __init__(self, k_size=3):
        super(ECA, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        y = self.avg_pool(x)
        y = self.conv(y.squeeze(-1).transpose(-1, -2)).transpose(-1, -2).unsqueeze(-1)
        return x * self.sigmoid(y)

# 4.3 THE FIXED MODEL
class ProposedNet(nn.Module):
    def __init__(self):
        super(ProposedNet, self).__init__()
        # SRM Layer (Fixed)
        self.srm = nn.Conv2d(1, 16, 5, padding=2, bias=False)
        self.srm.weight.data = srm_init_weights()
        self.srm.weight.requires_grad = False 
        
        # Stream 1
        self.conv1 = nn.Conv2d(16, 32, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        
        # Attention
        self.attn = ECA(k_size=3)
        
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.pool = nn.MaxPool2d(2, 2)
        
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        
        self.global_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(128, 2)

        # He Initialization for non-SRM layers
        for m in self.modules():
            if isinstance(m, nn.Conv2d) and m != self.srm:
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):
        # --- CRITICAL FIX: SCALE 0-1 FLOAT TO 0-255 FOR SRM ---
        x_scaled = x * 255.0 
        x = self.srm(x_scaled) 
        
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.attn(x) 
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        x = self.pool(F.relu(self.bn3(self.conv3(x))))
        
        x = self.global_pool(x).view(x.size(0), -1)
        x = self.fc(x)
        return x

def train_proposed(X_train, y_train, X_test, epochs=20):
    model = ProposedNet().to(device)
    crit = nn.CrossEntropyLoss()
    opt = optim.Adam(model.parameters(), lr=0.0005) # Lower LR for stability
    
    train_ds = torch.utils.data.TensorDataset(torch.from_numpy(X_train), torch.LongTensor(y_train))
    test_ds = torch.utils.data.TensorDataset(torch.from_numpy(X_test), torch.LongTensor(np.zeros(len(X_test))))
    train_dl = DataLoader(train_ds, batch_size=64, shuffle=True)
    test_dl = DataLoader(test_ds, batch_size=64)
    
    for _ in track(range(epochs), description="Training CNN..."):
        model.train()
        for x, y in train_dl:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            out = model(x)
            loss = crit(out, y)
            loss.backward()
            opt.step()
            
    model.eval()
    
    # Save Model Weights
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), "models/proposed_net.pth")
    
    all_preds = []
    all_probs = []
    with torch.no_grad():
        for x, _ in test_dl:
            x = x.to(device)
            out = model(x)
            prob = F.softmax(out, dim=1)[:, 1]
            pred = torch.argmax(out, dim=1)
            all_preds.extend(pred.cpu().numpy())
            all_probs.extend(prob.cpu().numpy())
            
    return np.array(all_preds), np.array(all_probs), model


def train_shallow(X_train, y_train, X_test, epochs=15):
    """Train the second, shallower CNN for the ensemble."""
    model = ShallowNet().to(device)
    crit = nn.CrossEntropyLoss()
    opt = optim.Adam(model.parameters(), lr=0.001) 
    
    train_ds = torch.utils.data.TensorDataset(torch.from_numpy(X_train), torch.LongTensor(y_train))
    test_ds = torch.utils.data.TensorDataset(torch.from_numpy(X_test), torch.LongTensor(np.zeros(len(X_test))))
    train_dl = DataLoader(train_ds, batch_size=64, shuffle=True)
    test_dl = DataLoader(test_ds, batch_size=64)
    
    for _ in track(range(epochs), description="Training ShallowNet..."):
        model.train()
        for x, y in train_dl:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            out = model(x)
            loss = crit(out, y)
            loss.backward()
            opt.step()
            
    model.eval()
    
    # Save Model Weights
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), "models/shallow_net.pth")
    
    all_preds = []
    all_probs = []
    with torch.no_grad():
        for x, _ in test_dl:
            x = x.to(device)
            out = model(x)
            prob = F.softmax(out, dim=1)[:, 1]
            pred = torch.argmax(out, dim=1)
            all_preds.extend(pred.cpu().numpy())
            all_probs.extend(prob.cpu().numpy())
            
    return np.array(all_preds), np.array(all_probs), model
