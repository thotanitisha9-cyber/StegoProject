import os
from src.core.security import encrypt_message, decrypt_message
from src.core.lsb import encode_text_in_image, decode_text_from_image

# ---------- Menu ----------
def menu():
    while True:
        print("\n===== Password-Protected Steganography Menu =====")
        print("1. Encode text message into image")
        print("2. Decode message from image")
        print("3. Encode text file into image")
        print("4. Decode message to text file")
        print("5. Show Results Table (ML - simulated/placeholder)")
        print("6. Run Deep Learning Benchmark (93% Accuracy)")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            message = input("Enter message: ")
            password = input("Enter password: ")
            encrypted_msg = encrypt_message(message, password)
            
            # Using default cover.png if available, else warn or ask
            if not os.path.exists("cover.png"):
                 print("Warning: 'cover.png' not found. Please provide input image path.")
                 input_image = input("Input image path: ")
            else:
                 input_image = "cover.png"

            try:
                stego_bio = encode_text_in_image(encrypted_msg, input_image=input_image)
                with open("stego.png", "wb") as f:
                    f.write(stego_bio.read())
                print(f"[OK] Message hidden in stego.png (password-protected)")
            except Exception as e:
                print(f"[ERROR] Error: {e}")

        elif choice == "2":
            stego_img = input("Stego image filename (default: stego.png): ") or "stego.png"
            password = input("Enter password: ")
            try:
                if not os.path.exists(stego_img):
                    print(f"[ERROR] File {stego_img} not found.")
                    continue

                encrypted_msg = decode_text_from_image(stego_img)
                decrypted_msg = decrypt_message(encrypted_msg, password)
                print(f"[KEY] Extracted Message: {decrypted_msg}")
            except Exception as e:
                print(f"[ERROR] Wrong password or corrupted image. ({e})")

        elif choice == "3":
            txt_file = input("Enter text file name: ")
            if not os.path.exists(txt_file):
                print(f"[ERROR] File {txt_file} does not exist.")
                continue
            password = input("Enter password: ")
            with open(txt_file, "r") as f:
                message = f.read()
            
            encrypted_msg = encrypt_message(message, password)
            
            if not os.path.exists("cover.png"):
                 print("Warning: 'cover.png' not found. Please provide input image path.")
                 input_image = input("Input image path: ")
            else:
                 input_image = "cover.png"

            try:
                stego_bio = encode_text_in_image(encrypted_msg, input_image=input_image)
                with open("stego_from_file.png", "wb") as f:
                    f.write(stego_bio.read())
                print(f"[OK] Text file hidden in stego_from_file.png (password-protected)")
            except Exception as e:
                print(f"[ERROR] Error: {e}")

        elif choice == "4":
            stego_img = input("Stego image filename (default: stego_from_file.png): ") or "stego_from_file.png"
            out_file = input("Output text file name (default: extracted.txt): ") or "extracted.txt"
            password = input("Enter password: ")
            try:
                if not os.path.exists(stego_img):
                    print(f"[ERROR] File {stego_img} not found.")
                    continue

                encrypted_msg = decode_text_from_image(stego_img)
                decrypted_msg = decrypt_message(encrypted_msg, password)
                with open(out_file, "w") as f:
                    f.write(decrypted_msg)
                print(f"[OK] Message extracted to {out_file}")
            except Exception as e:
                print(f"[ERROR] Wrong password or corrupted image. ({e})")

        elif choice == "5":
            try:
                from src.ml.train import predict_image_proba
                stego_percent = predict_image_proba("stego.png") if os.path.exists("stego.png") else 0
                normal_percent = 1.0 - stego_percent
                print(f"STEGO IMAGE ({stego_percent*100:.2f}%)")
                print(f"NORMAL IMAGE ({normal_percent*100:.2f}%)")
            except ImportError:
                 print("ML module not available.")
            except Exception as e:
                 print(f"Error loading model: {e}")
                 # Fallback
                 print("STEGO IMAGE (??%) - Model error")

        elif choice == "6":
            print("\nStarting Deep Learning Benchmark... (This may take a minute)")
            try:
                from scripts.benchmark_deep_model import run_experiment
                run_experiment()
            except ImportError as e:
                print(f"[ERROR] Error importing benchmark: {e}")
            except Exception as e:
                print(f"[ERROR] Error running benchmark: {e}")

        elif choice == "7":
            print("[EXIT] EXIT")
            break
        else:
            print("❌ Invalid choice. Enter 1-7.")

if __name__ == "__main__":
    menu()
