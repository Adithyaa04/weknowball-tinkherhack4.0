import cv2
import numpy as np
import json
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

CONFIDENCE_THRESHOLD = 80

def load_model():
    if not os.path.exists("lbph_face_model.xml") or not os.path.exists("label_map.json"):
        return None, {}
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read("lbph_face_model.xml")
    with open("label_map.json", "r") as f:
        label_map = json.load(f)
    return model, label_map

def generate_frames():
    model, label_map = load_model()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            if model:
                label, confidence = model.predict(face)
                if confidence < CONFIDENCE_THRESHOLD:
                    info = label_map.get(str(label), {"name": "Unknown", "relation": ""})
                    name = info["name"]
                    relation = info["relation"]
                    color = (34, 180, 100)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                    cv2.rectangle(frame, (x, y-55), (x+w, y), color, -1)
                    cv2.putText(frame, name, (x+6, y-32),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(frame, relation, (x+6, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220,255,220), 1)
                else:
                    color = (0, 0, 220)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                    cv2.rectangle(frame, (x, y-36), (x+w, y), color, -1)
                    cv2.putText(frame, "Unknown Person", (x+6, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 200, 0), 2)
                cv2.putText(frame, "No model trained yet", (x+6, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)

        ret2, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()


def collect_faces_stream(name, relation):
    """Generator that captures 100 face photos and streams progress frames."""
    folder = f"faces/{name}_{relation}"
    os.makedirs(folder, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cropped = frame[y:y+h, x:x+w]

            count += 1
            face_gray = cv2.cvtColor(cv2.resize(cropped, (200, 200)), cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{folder}/{count}.jpg", face_gray)

            # Draw progress on frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (34, 180, 100), 2)
            cv2.rectangle(frame, (0, 0), (frame.shape[1], 50), (34, 180, 100), -1)
            cv2.putText(frame, f"Capturing {name}: {count}/100", (10, 34),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
        else:
            cv2.rectangle(frame, (0, 0), (frame.shape[1], 50), (0, 0, 180), -1)
            cv2.putText(frame, "No face detected — look at the camera", (10, 34),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2)

        ret2, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

        if count >= 100:
            break

    cap.release()


def run_training():
    """Train model from faces/ folder. Returns (success, message)."""
    data_path = "faces/"
    Training_Data = []
    Labels = []
    label_map = {}

    if not os.path.exists(data_path):
        return False, "No faces/ folder found."

    folders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
    if not folders:
        return False, "No person folders found in faces/."

    label_id = 0
    for folder_name in folders:
        folder_path = os.path.join(data_path, folder_name)
        parts = folder_name.split("_", 1)
        name = parts[0]
        relation = parts[1] if len(parts) > 1 else "Unknown"
        label_map[str(label_id)] = {"name": name, "relation": relation}

        for img_file in os.listdir(folder_path):
            if not img_file.endswith(".jpg"):
                continue
            img = cv2.imread(os.path.join(folder_path, img_file), cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            Training_Data.append(np.asarray(img, dtype=np.uint8))
            Labels.append(label_id)
        label_id += 1

    if not Training_Data:
        return False, "No images found in face folders."

    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(Training_Data, Labels)
    model.save("lbph_face_model.xml")

    with open("label_map.json", "w") as f:
        json.dump(label_map, f, indent=2)

    names = [v["name"] for v in label_map.values()]
    return True, f"Trained on {len(names)} people: {', '.join(names)}"