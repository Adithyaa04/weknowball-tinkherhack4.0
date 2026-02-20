import cv2
import numpy as np

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load trained LBPH model
model = cv2.face.LBPHFaceRecognizer_create()
model.read("lbph_face_model.xml")

# Start webcam
cap = cv2.VideoCapture(0)

# Confidence threshold (lower = stricter)
CONFIDENCE_THRESHOLD = 40

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
            text = f"KNOWN ({round(confidence,2)})"
            color = (0, 255, 0)
        else:
            text = f"UNKNOWN ({round(confidence,2)})"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
        cv2.putText(frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 13:  # Enter key
        break

cap.release()
cv2.destroyAllWindows()
