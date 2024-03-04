from collections import defaultdict

from torchvision.datasets import coco
from ultralytics import YOLO

model = YOLO("best.pt")


# Predict using the model
results = model.predict(source='images2.jpeg', show=True, conf=0.8)

print(results)