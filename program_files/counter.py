import sys
import signals
import threading
from ultralytics import YOLO
import time


# Load your model
model = YOLO('../models/best.pt')
# Flag to keep track of ambulance presence
ambulance_detected = False

# Function to run countdown in a separate thread
def start_countdown():
    global ambulance_detected
    current_state = 0
    while True:
        if ambulance_detected:
            signals.countdown(1,1)
        else:
            signals.countdown(0,1)
        time.sleep(1)  # Adjust this sleep time to control how often it checks

# Start the countdown thread
countdown_thread = threading.Thread(target=start_countdown)
countdown_thread.daemon = True  # Daemonize thread to ensure it exits when main program does
countdown_thread.start()
# Run inference

results = model('../test_files/video2.mp4',verbose=False,stream=True,show=True)

# Extract class IDs and names
for frame_idx, result in enumerate(results):
    # Extract class IDs for the current frame
    class_ids = result.boxes.cls
    # Extract class names for the current frame
    class_names = [model.names[int(cls_id)] for cls_id in class_ids]

    # Print class IDs and names
    # print(f"Frame {frame_idx + 1}:")
    # print("Class IDs:", class_ids)
    # print("Class Names:", class_names)

    # Check if "ambulance" is detected
    if "ambulance" in class_names:
        print("Ambulance detected")
        ambulance_detected=True
    else:
        ambulance_detected=False

     # To control the frame processing rate