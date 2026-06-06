import os
import sys
import numpy as np
from PIL import Image
from scipy.stats import entropy

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

def calculate_entropy(img_path):
    try:
        img = Image.open(img_path).convert('RGB')
        arr = np.array(img)
        lsb = arr & 1
        _, counts = np.unique(lsb, return_counts=True)
        return entropy(counts, base=2)
    except Exception:
        return 0.0

def analyze_directory(name, directory):
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"\nAnalyzing {name} ({len(files)} images)...")
    
    entropies = []
    for f in files:
        path = os.path.join(directory, f)
        ent = calculate_entropy(path)
        entropies.append(ent)
        
    if entropies:
        print(f"  Min: {min(entropies):.4f}")
        print(f"  Max: {max(entropies):.4f}")
        print(f"  Avg: {np.mean(entropies):.4f}")
        return min(entropies), max(entropies)
    else:
        print("  No images found.")
        return 0, 0

if __name__ == "__main__":
    stego_dir = os.path.join(project_root, "NewDataset", "stego")
    cover_dir = os.path.join(project_root, "NewDataset", "cover")
    
    analyze_directory("NewDataset/cover", cover_dir)
    analyze_directory("NewDataset/stego", stego_dir)
