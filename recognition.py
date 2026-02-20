import cv2
import numpy as np
import os

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Create faces directory if not exists
os.makedirs("faces", exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

count = 0

def face_extractor(img):
    """
    Detects face and returns cropped face.
    If no face detected, returns None
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    for (x, y, w, h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Collect 100 samples
while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = face_extractor(frame)

    if face is not None:
        count += 1
        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = f"faces/{count}.jpg"
        cv2.imwrite(file_name_path, face)

        cv2.putText(face, str(count), (20, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Face Cropper", face)

    else:
        cv2.imshow("Face Cropper", frame)

    if cv2.waitKey(1) == 13 or count == 100:  # Enter key
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Collecting Samples Complete")
