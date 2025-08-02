import os
import cv2

# Change this to your actual val folder
val_dir = r"Your_path_here" 

# Allowed extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.mp4', '.avi', '.mov']
# Loop through all files
for filename in os.listdir(val_dir):
    filepath = os.path.join(val_dir, filename)
    ext = os.path.splitext(filename)[1].lower()

    # Only process images or videos
    if ext in valid_extensions:
        try:
            if ext in ['.jpg', '.jpeg', '.png', '.bmp']:
                img = cv2.imread(filepath)
                if img is None:
                    print(f"Corrupted image removed: {filename}")
                    os.remove(filepath)

            elif ext in ['.mp4', '.avi', '.mov']:
                cap = cv2.VideoCapture(filepath)
                ret, _ = cap.read()
                if not ret:
                    print(f"Corrupted video removed: {filename}")
                    os.remove(filepath)
                cap.release()

        except Exception as e:
            print(f"Error with {filename}: {e}")
            os.remove(filepath)
