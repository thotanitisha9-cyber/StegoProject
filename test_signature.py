from PIL import Image
import numpy as np
import os

def analyze_uploads():
    img1_path = r"C:/Users/PADHMA SRI/.gemini/antigravity/brain/a96dd45c-afe8-4b9c-9c39-12a001361d97/uploaded_media_0_1770105990940.png"
    img2_path = r"C:/Users/PADHMA SRI/.gemini/antigravity/brain/a96dd45c-afe8-4b9c-9c39-12a001361d97/uploaded_media_1_1770105990940.png"

    print(f"Comparing Uploads:")
    print(f"  Image 1: {os.path.basename(img1_path)}")
    print(f"  Image 2: {os.path.basename(img2_path)}")

    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        print("Error: Files not found.")
        return

    try:
        img1 = Image.open(img1_path).convert("RGB")
        img2 = Image.open(img2_path).convert("RGB")
    except Exception as e:
        print(f"Error opening images: {e}")
        return

    arr1 = np.array(img1)
    arr2 = np.array(img2)

    if arr1.shape != arr2.shape:
        print(f"Images have different dimensions: {arr1.shape} vs {arr2.shape}")
        return

    if np.array_equal(arr1, arr2):
        print("Result: The images are IDENTICAL (Bitwise exact match).")
    else:
        print("Result: The images are DIFFERENT.")
        
        diff = np.abs(arr1.astype(int) - arr2.astype(int))
        num_diff_pixels = np.count_nonzero(np.sum(diff, axis=2))
        total_pixels = arr1.shape[0] * arr1.shape[1]
        
        print(f"  - Modified Pixels: {num_diff_pixels} out of {total_pixels} ({num_diff_pixels/total_pixels*100:.2f}%)")
        print(f"  - Max pixel change: {np.max(diff)}")
        
        # Analyze bit planes
        # If max change is 1, it's likely LSB
        if np.max(diff) == 1:
            print("\nExplanation: The difference is only +/- 1 pixel value.")
            print("This strongly suggests LSB (Least Significant Bit) Steganography.")
            print("The images look identical to the human eye because the change is too small to perceive.")

if __name__ == "__main__":
    analyze_uploads()
