import cv2
import numpy as np
import os

# Path to face images
data_path = "faces"

# Get all image files
onlyfiles = [
    f for f in os.listdir(data_path)
    if os.path.isfile(os.path.join(data_path, f))
]

# Prepare training data
TrainingData = []
Labels = []

for i, file in enumerate(onlyfiles):
    image_path = os.path.join(data_path, file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        continue

    TrainingData.append(np.asarray(image, dtype=np.uint8))
    Labels.append(i)

# Convert labels to numpy array
Labels = np.asarray(Labels, dtype=np.int32)

# Check if data exists
if len(TrainingData) == 0:
    print("❌ No training data found")
    exit()

# Create LBPH recognizer
model = cv2.face.LBPHFaceRecognizer_create()

# Train model
model.train(TrainingData, Labels)

# Save model
model.save("lbph_face_model.xml")

print("✅ Model trained successfully")
