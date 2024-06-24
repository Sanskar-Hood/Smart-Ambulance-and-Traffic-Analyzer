import sys

from ultralytics import YOLO


# Load your model
model = YOLO('../models/best.pt')

# Run inference
results = model('video2.mp4')

# Extract class IDs and names
for frame_idx, result in enumerate(results):
    # Extract class IDs for the current frame
    class_ids = result.boxes.cls
    # Extract class names for the current frame
    class_names = [model.names[int(cls_id)] for cls_id in class_ids]

    # Print class IDs and names
    print(f"Frame {frame_idx + 1}:")
    print("Class IDs:", class_ids)
    print("Class Names:", class_names)

    # Check if "ambulance" is detected
    if "ambulance" in class_names:
        sys.exit()
        # print(f"Ambulance detected in frame {frame_idx + 1}")
        # # Perform desired action upon detecting an ambulance
        # # For example, you can save the frame, alert the user, etc.
        # break  # Exit the loop once the ambulance is detected