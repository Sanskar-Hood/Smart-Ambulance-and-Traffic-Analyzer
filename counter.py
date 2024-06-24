from ultralytics import YOLO
import labelImg

# Load your model
model = YOLO('best.pt')

# Run inference
# results1 = model.predict(source="images.jpeg", show=True, conf=0.8)
results = model('images.jpeg')

# Extract class IDs and names
for result in results:
    class_ids = result.boxes.cls
    # class_ids=[1,3,5,7]
    class_names = [model.names[int(cls_id)] for cls_id in class_ids]

    print("Class IDs:", class_ids)
    print("Class Names:", class_names)


# while(1):
#     print(results1)