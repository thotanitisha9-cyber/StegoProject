
def text_to_binary(text):
    """Convert text to a binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Convert binary string to text."""
    # Ensure binary length is multiple of 8
    if len(binary) % 8 != 0:
        # trim to nearest multiple of 8
        binary = binary[:-(len(binary) % 8)]
        
    chars = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def encode_zwc(cover_text, secret_message):
    """
    Embeds a secret message into cover text using Zero-Width Characters.
    A zero-width space (U+200B) represents bit '1'.
    A zero-width non-joiner (U+200C) represents bit '0'.
    """
    if not cover_text:
        raise ValueError("Cover text cannot be empty.")
    
    binary_secret = text_to_binary(secret_message)
    
    # Map 1 -> U+200B, 0 -> U+200C
    zwc_secret = ""
    for bit in binary_secret:
        if bit == '1':
            zwc_secret += '\u200B'
        else:
            zwc_secret += '\u200C'
            
    # Insert the hidden ZWC string after the first character of the cover text
    # This is a simple strategy. We could distribute it, but keeping it contiguous is easier for this demo.
    if len(cover_text) > 0:
        return cover_text[0] + zwc_secret + cover_text[1:]
    else:
        return zwc_secret

def decode_zwc(stego_text):
    """
    Extracts the secret message from text containing Zero-Width Characters.
    """
    binary_extracted = ""
    for char in stego_text:
        if char == '\u200B':
            binary_extracted += '1'
        elif char == '\u200C':
            binary_extracted += '0'
            
    if not binary_extracted:
        return ""
        
    return binary_to_text(binary_extracted)