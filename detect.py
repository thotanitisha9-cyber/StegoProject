import cv2
import os
import shutil
import numpy as np
from PIL import Image
from io import BytesIO
from src.core.lsb import encode_text_in_image, decode_text_from_image

def encode_video(input_video_path, message, output_video_path):
    """
    Embeds a secret message into the first frame of a video using LSB.
    Note: Audio is discarded due to OpenCV limitations.
    Returns: (success, error_message)
    """
    try:
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            return False, "Could not open input video file."

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if width == 0 or height == 0:
             return False, "Video has invalid dimensions."

        # CRITICAL: We MUST use a LOSSLESS codec. 
        # MP4V/MJPG/AVC1 are lossy and DESTROY LSB data.
        # 'FFV1' is a great lossless codec supported by OpenCV.
        # 'png ' is also an option but FFV1 is better for video.
        
        fourcc = cv2.VideoWriter_fourcc(*'FFV1')
        output_video_path = output_video_path.replace(".mp4", ".avi") # Enforce AVI for FFV1
        
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
        
        if not out.isOpened():
             return False, f"Could not create video writer for {output_video_path} with codec."

        frame_idx = 0
        success = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_idx == 0:
                # --- EMBED MESSAGE IN FIRST FRAME ---
                # Convert BGR (OpenCV) to RGB (PIL)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_img = Image.fromarray(frame_rgb)
                
                # Embed message
                # Note: encode_text_in_image returns BytesIO, need to convert back to cv2 frame
                # We need to seek(0) the buffer before reading
                stego_buffer = encode_text_in_image(message, input_image=pil_img)
                stego_buffer.seek(0)
                stego_pil = Image.open(stego_buffer)
                
                # Convert back RGB (PIL) to BGR (OpenCV)
                stego_frame = cv2.cvtColor(np.array(stego_pil), cv2.COLOR_RGB2BGR)
                out.write(stego_frame)
                success = True
            else:
                # Write remaining frames as is
                # Note: If encoding fails (success=False), we should probably stop or handle it
                # But here we just copy frames
                out.write(frame)
            
            frame_idx += 1

        cap.release()
        out.release()
        
        if not success:
             return False, "Failed to embed message in the first frame."
             
        return True, "Success"

    except Exception as e:
        print(f"Video Encoding Error: {e}")
        return False, str(e)

def decode_video(input_video_path):
    """
    Extracts secret message from the first frame of a video.
    Returns: Decoded message string or None.
    """
    try:
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise ValueError("Could not open video file.")

        # Read only the first frame
        ret, frame = cap.read()
        cap.release()

        if not ret:
            raise ValueError("Empty video or read error.")

        # Convert BGR to RGB (PIL)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(frame_rgb)

        # Extract message using LSB module
        # Need to save momentarily or pass object? decode accepts file-like
        # Let's verify decode_text_from_image implementation... 
        # It accepts 'image_path_or_file' and calls Image.open(). 
        # However, we already have a PIL image.
        
        # HACK: Save frame to temp buffer to pass to decode function 
        # (or update decode function to accept PIL image - but let's stick to existing API)
        buf = BytesIO()
        pil_img.save(buf, format="PNG")
        buf.seek(0)
        
        message = decode_text_from_image(buf)
        return message

    except Exception as e:
        print(f"Video Decoding Error: {e}")
        return None
