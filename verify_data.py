
import os
import random
import string
from PIL import Image, ImageDraw
import sys

# Add project root to sys.path to import src modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import core steganography logic
from src.core.lsb import encode_text_in_image

# Configuration
NUM_IMAGES = 200  # Number of new images to generate
DATASET_DIR = "NewDataset"
COVER_DIR = os.path.join(DATASET_DIR, "cover")
STEGO_DIR = os.path.join(DATASET_DIR, "stego")

os.makedirs(COVER_DIR, exist_ok=True)
os.makedirs(STEGO_DIR, exist_ok=True)

def random_color():
    """Generates a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_random_image(width=512, height=512):
    """Generates a random image with geometric shapes."""
    img = Image.new("RGB", (width, height), random_color())
    draw = ImageDraw.Draw(img)
    
    # Add random shapes (Rectangles, Circles, Lines)
    for _ in range(random.randint(5, 15)):
        shape_type = random.choice(["rectangle", "circle", "line"])
        
        # Random coordinates
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        
        color = random_color()
        
        if shape_type == "rectangle":
            draw.rectangle([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=random_color())
        elif shape_type == "circle":
            draw.ellipse([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=random_color())
        elif shape_type == "line":
            draw.line([x1, y1, x2, y2], fill=color, width=random.randint(1, 5))
            
    return img

def generate_random_text(length=100):
    """Generates a random string of text."""
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

def main():
    print(f"Generating {NUM_IMAGES} synthetic images...")
    
    for i in range(NUM_IMAGES):
        try:
            # 1. Create a Synthetic Cover Image
            cover_img = generate_random_image()
            cover_filename = f"synth_cover_{i}.png"
            cover_path = os.path.join(COVER_DIR, cover_filename)
            cover_img.save(cover_path)
            
            # 2. Create Stego Version
            message_len = random.randint(50, 500)
            secret_message = generate_random_text(message_len)
            
            # Use core logic
            stego_bytes = encode_text_in_image(secret_message, input_image=cover_path)
            
            stego_filename = f"synth_stego_{i}.png"
            stego_path = os.path.join(STEGO_DIR, stego_filename)
            
            with open(stego_path, "wb") as f:
                f.write(stego_bytes.read())
                
            print(f"[{i+1}/{NUM_IMAGES}] Generated: {cover_filename} -> {stego_filename}")
            
        except Exception as e:
            print(f"Error generating image {i}: {e}")

    print("Synthetic dataset generation complete.")

if __name__ == "__main__":
    main()
