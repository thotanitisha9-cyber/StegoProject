import sys
import os
import numpy as np
from PIL import Image

# Add project root to path
sys.path.append(os.getcwd())

from src.ml.inference import predict_ensemble, detect_encryption_signature

def create_mock_encrypted_stego(filename="mock_sig.png"):
    """Creates a mock stego image with 'gAAAA' signature in LSBs."""
    # 1. Create random image
    img_arr = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    
    # 2. Embed 'gAAAA' (Fernet header)
    # 'g' = 01100111
    # 'A' = 01000001
    header = "gAAAA"
    binary = "".join(format(ord(c), '08b') for c in header)
    
    # Embed in LSBs of first pixels
    pixels = img_arr.reshape(-1, 3)
    idx = 0
    for i in range(len(pixels)):
        for j in range(3):
            if idx < len(binary):
                # Clear LSB and set to bit
                pixels[i][j] = (pixels[i][j] & 0xFE) | int(binary[idx])
                idx += 1
                
    img_reshaped = pixels.reshape((64, 64, 3))
    Image.fromarray(img_reshaped).save(filename)
    return filename

def test_signature():
    print("--- Testing Fernet Signature Detection ---")
    
    # 1. Create mock
    path = create_mock_encrypted_stego()
    print(f"Created mock encoded image: {path}")
    
    # 2. Test Function Directly
    img = Image.open(path)
    is_sig = detect_encryption_signature(img)
    print(f"Direct Signature Check: {'[PASS] PASSED' if is_sig else '[FAIL] FAILED'}")
    
    # 3. Test Full Inference
    label, prob, details = predict_ensemble(path)
    print(f"\nEnsemble Prediction: {label} ({prob*100:.1f}%)")
    print("Details:", details)
    
    if label == "Stego" and "Signature" in details.get("Method", ""):
        print("\n[PASS] SUCCESS: Signature detected and overrode ML/Heuristic.")
        try: os.remove(path) 
        except: pass
    else:
        print("\n[FAIL] FAILURE: Signature not detected or not used.")

if __name__ == "__main__":
    test_signature()
