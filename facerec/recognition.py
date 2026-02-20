import cv2
import os

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Ask for person's details
name = input("Enter person's name: ").strip()
relation = input("Enter relation (e.g. Son, Daughter, Doctor, Friend): ").strip()

# Create a folder for this person: faces/John_Son/
folder = f"faces/{name}_{relation}"
os.makedirs(folder, exist_ok=True)

print(f"\n📷 Look at the camera! Collecting 100 photos of {name}...")
print("Press ENTER to stop early.\n")

cap = cv2.VideoCapture(0)
count = 0

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return None
    for (x, y, w, h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = face_extractor(frame)

    if face is not None:
        count += 1
        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = f"{folder}/{count}.jpg"
        cv2.imwrite(file_name_path, face)

        cv2.putText(face, f"{name} {count}/100", (5, 30),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow("Face Collector", face)
    else:
        cv2.putText(frame, "No face detected", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Face Collector", frame)

    if cv2.waitKey(1) == 13 or count == 100:
        break

cap.release()
cv2.destroyAllWindows()
print(f"✅ Collected {count} photos for {name} ({relation})")
print(f"   Saved in: {folder}/")
print("\nRun collect_faces.py again to add another person, or run train.py when done.")