from cryptography.fernet import Fernet
import base64
import hashlib

# AES Encryption Module
# Uses SHA-256 for key derivation from password
# Uses Fernet (AES-128 in CBC mode with PKCS7 padding + HMAC)

def derive_key(password):
    """
    Derives a 32-byte URL-safe base64-encoded key from the password.
    """
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_message(message, password):
    try:
        if not message: return ""
        if not password: raise ValueError("Password required for encryption.")
        
        key = derive_key(password)
        f = Fernet(key)
        encrypted = f.encrypt(message.encode())
        return encrypted.decode() # Return as string
    except Exception as e:
        print(f"Encryption failed: {e}")
        return None

def decrypt_message(encrypted_message, password):
    try:
        if not encrypted_message: return ""
        if not password: raise ValueError("Password required for decryption.")
        
        key = derive_key(password)
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None
