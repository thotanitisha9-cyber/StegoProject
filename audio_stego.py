import os
import sys
import numpy as np
from PIL import Image
from scipy.stats import entropy

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def extract_features(path):
    print(f"--- Features for {os.path.basename(path)} ---")
    img = Image.open(path).convert("RGB")
    arr = np.array(img)
    
    # 1. LSB Analysis
    lsb_plane = arr & 1
    values, counts = np.unique(lsb_plane, return_counts=True)
    entr = entropy(counts, base=2) if len(counts) > 1 else 0
    lsb_frac = lsb_plane.mean()
    
    print(f"LSB Entropy: {entr}")
    print(f"LSB Fraction: {lsb_frac}")
    
    # 2. RGB Stats
    print(f"Mean: {arr.mean()}")
    print(f"Var: {arr.var()}")
    
    return [entr, lsb_frac, arr.mean(), arr.var()]

if __name__ == "__main__":
    BASE_DIR = "NewDataset"
    cover = os.path.join(BASE_DIR, "cover", "cover_001.png")
    stego = os.path.join(BASE_DIR, "stego", "stego_001.png")
    
    f1 = extract_features(cover)
    f2 = extract_features(stego)
    
    print("\nComparison:")
    print(f"Entropy diff: {f2[0] - f1[0]}")
    print(f"Fraction diff: {f2[1] - f1[1]}")
