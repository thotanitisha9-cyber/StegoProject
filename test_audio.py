import wave
import math
import struct
import os
import sys

# Add src to path
sys.path.append(os.getcwd())

from src.core.audio_stego import encode_audio_v2, decode_audio_v2

def create_sine_wave(filename, duration=1.0, freq=440.0, frame_rate=44100):
    """Generates a sine wave WAV file."""
    try:
        n_frames = int(duration * frame_rate)
        data = []
        for i in range(n_frames):
            value = int(32767.0 * math.sin(2.0 * math.pi * freq * i / frame_rate))
            data.append(struct.pack('<h', value)) # 16-bit little-endian
        
        with wave.open(filename, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(frame_rate)
            wav_file.writeframes(b''.join(data))
        print(f"Created {filename}")
        return True
    except Exception as e:
        print(f"Error creating wav: {e}")
        return False

def test_audio_stego():
    input_wav = "test_audio_source.wav"
    output_wav = "test_audio_stego.wav"
    secret_message = "This is a secret audio message! 123"
    
    # 1. Create Source
    if not create_sine_wave(input_wav):
        return
        
    # 2. Encode
    print(f"Encoding message: '{secret_message}'")
    if encode_audio_v2(input_wav, secret_message, output_wav):
        print("Encoding successful.")
    else:
        print("Encoding failed.")
        return
        
    # 3. Decode
    print("Decoding...")
    decoded = decode_audio_v2(output_wav)
    print(f"Decoded message: '{decoded}'")
    
    # 4. Verification
    if decoded == secret_message:
        print("SUCCESS: Message matches!")
    else:
        print("FAILURE: Message mismatch.")

    # Cleanup
    if os.path.exists(input_wav):
        os.remove(input_wav)
    if os.path.exists(output_wav):
        os.remove(output_wav)

if __name__ == "__main__":
    test_audio_stego()
