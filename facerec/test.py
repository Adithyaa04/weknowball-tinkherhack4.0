import cv2
import numpy as np
import json
import os

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load trained LBPH model
model = cv2.face.LBPHFaceRecognizer_create()
model.read("lbph_face_model.xml")

# Load name/relation map
with open("label_map.json", "r") as f:
    label_map = json.load(f)

# Start webcam
cap = cv2.VideoCapture(0)

CONFIDENCE_THRESHOLD = 80

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = model.predict(face)

        if confidence < CONFIDENCE_THRESHOLD:
            info = label_map.get(str(label), {"name": "Unknown", "relation": ""})
            name = info["name"]
            relation = info["relation"]
            color =(34, 180, 100)  # green

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.rectangle(frame, (x, y - 55), (x + w, y), color, -1)
            cv2.putText(frame, name, (x + 6, y - 32),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(frame, relation, (x + 6, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 255, 220), 1)
        else:
            color = (0, 0, 220)  # red
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.rectangle(frame, (x, y - 36), (x + w, y), color, -1)
            cv2.putText(frame, "Unknown Person", (x + 6, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

    cv2.imshow("AlzHelper - Face Recognition", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()