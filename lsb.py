import sys
import os
import numpy as np
from PIL import Image

# Add project root to path
sys.path.append(os.getcwd())

from src.ml.inference import predict_ensemble

def create_mock_stego(filename="mock_stego.png"):
    """Creates a high-entropy mock stego image."""
    img = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
    # Ensure LSBs are random (they are by default in random image)
    Image.fromarray(img).save(filename)
    return filename

def test_heuristic():
    print("--- Testing LSB Heuristic Safety Net ---")
    
    # 1. Create a mock stego image (High Entropy)
    mock_path = create_mock_stego()
    print(f"Created mock stego: {mock_path}")
    
    # 2. Run Inference
    label, prob, details = predict_ensemble(mock_path)
    
    print(f"\nPrediction: {label} ({prob*100:.1f}%)")
    print("Details:", details)
    
    # 3. Validation
    if label == "Stego" and "Heuristic" in details and "TRIGGERED" in details["Heuristic"]:
        print("\n✅ SUCCESS: Heuristic triggered correctly for high-entropy image.")
        os.remove(mock_path)
    else:
        print("\n❌ FAILURE: Heuristic did not trigger.")

if __name__ == "__main__":
    test_heuristic()
