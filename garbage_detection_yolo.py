
# Install the necessary library
!pip install ultralytics

import os
from ultralytics import YOLO
import glob

# Set up paths
DATA_PATH = "/content/dataset"
DATA_YAML_PATH = os.path.join(DATA_PATH, "data.yaml")

# If your dataset is in a zip file, unzip it
# !unzip /path/to/your/dataset.zip -d /content/

# Initialize the model (YOLOv8, the latest version)
model = YOLO('yolov8n.yaml')  # You can also use yolov8s.yaml, yolov8m.yaml, yolov8l.yaml, or yolov8x.yaml

# Train the model
model.train(data=DATA_YAML_PATH, epochs=100, imgsz=640)

# Load the trained model
model = YOLO('/content/runs/train/exp/weights/best.pt')

# Run inference on a new image
test_images = glob.glob(os.path.join(DATA_PATH, "test", "*.jpg"))  # Get all test images

for img_path in test_images:
    results = model(img_path)  # Run inference
    results.show()  # Show results
