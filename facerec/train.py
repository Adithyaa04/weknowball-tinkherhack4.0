import cv2
import numpy as np
import os
import json

data_path = "faces/"
Training_Data = []
Labels = []
label_map = {}  # { "0": {"name": "John", "relation": "Son"}, ... }

# Each subfolder in faces/ is one person
label_id = 0

if not os.path.exists(data_path):
    print("❌ No faces/ folder found. Run collect_faces.py first.")
    exit()

folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]

if len(folders) == 0:
    print("❌ No person folders found inside faces/")
    print("   Expected format: faces/John_Son/, faces/Mary_Daughter/ etc.")
    exit()

print(f"📂 Found {len(folders)} people to train on:\n")

for folder_name in folders:
    folder_path = os.path.join(data_path, folder_name)

    # Parse name and relation from folder name: "John_Son" → John, Son
    parts = folder_name.split("_", 1)
    name = parts[0]
    relation = parts[1] if len(parts) > 1 else "Unknown"

    label_map[str(label_id)] = {"name": name, "relation": relation}
    print(f"   [{label_id}] {name} — {relation}")

    img_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

    for img_file in img_files:
        img_path = os.path.join(folder_path, img_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        Training_Data.append(np.asarray(img, dtype=np.uint8))
        Labels.append(label_id)

    label_id += 1

if len(Training_Data) == 0:
    print("\n❌ No images found in any folder.")
    exit()

print(f"\n🧠 Training on {len(Training_Data)} images...")

Labels = np.asarray(Labels, dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(Training_Data, Labels)

# Save model and label map
model.save("lbph_face_model.xml")

with open("label_map.json", "w") as f:
    json.dump(label_map, f, indent=2)

print("✅ Model trained and saved as lbph_face_model.xml")
print("✅ Label map saved as label_map.json")
print("\nPeople in model:")
for lid, info in label_map.items():
    print(f"   {info['name']} — {info['relation']}")