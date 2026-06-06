import os
import sys
from PIL import Image
import numpy as np

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

def verify_dataset_structure():
    print(f"Project Root: {project_root}")
    
    # Expected Paths from deep_stego.py
    sources = [
        (os.path.join(project_root, "NewDataset"), "cover", "stego"),
        (os.path.join(project_root, "Dataset"), "clean_images", "stego_images")
    ]
    
    total_found = 0
    
    for base_path, cov_name, steg_name in sources:
        print(f"\nChecking Source: {base_path}")
        if not os.path.exists(base_path):
            print(f"  ❌ Base directory NOT FOUND: {base_path}")
            continue
            
        cover_dir = os.path.join(base_path, cov_name)
        stego_dir = os.path.join(base_path, steg_name)
        
        # Check Cover
        if os.path.exists(cover_dir):
            files = [f for f in os.listdir(cover_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            print(f"  [OK] Cover Dir Found ({cov_name}): {len(files)} images")
            if len(files) > 0:
                try:
                    img = Image.open(os.path.join(cover_dir, files[0]))
                    print(f"     Sample: {files[0]} ({img.size}, {img.mode})")
                except Exception as e:
                    print(f"     [ERR] Error opening sample: {e}")
            total_found += len(files)
        else:
             print(f"  [ERR] Cover Dir NOT FOUND: {cov_name}")
             
        # Check Stego
        if os.path.exists(stego_dir):
            files = [f for f in os.listdir(stego_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            print(f"  [OK] Stego Dir Found ({steg_name}): {len(files)} images")
            if len(files) > 0:
                try:
                    img = Image.open(os.path.join(stego_dir, files[0]))
                    print(f"     Sample: {files[0]} ({img.size}, {img.mode})")
                except Exception as e:
                    print(f"     [ERR] Error opening sample: {e}")
            total_found += len(files)
        else:
             print(f"  [ERR] Stego Dir NOT FOUND: {steg_name}")

    if total_found == 0:
        print("\nCRITICAL: No images found in any expected directory!")
    else:
        print(f"\nTotal Images Found: {total_found}")

if __name__ == "__main__":
    verify_dataset_structure()
