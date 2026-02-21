<p align="center">
  <img src="facerec/img.png" alt="Project Banner" width="100%">
</p>

# ഓർമ്മ-Remembrance

## Basic Details

### Team Name: WEKNOWBALL

### Team Members
- Member 1: Adithya Vijay - NSS College Of Engineering Palakkad
- Member 2: Snoopa K - NSS College Of Engineering Palakkad

### Hosted Project Link
https://aerotropic-nonabstractly-tona.ngrok-free.dev/

### Project Description
ഓർമ്മ (Remembrance) is a supportive application designed to help Alzheimer’s patients manage daily life with confidence. It includes a digital diary, gentle reminders for important tasks, and a face recognition system to identify familiar people. The app aims to reduce confusion, improve independence, and provide emotional reassurance.

### The Problem statement
Over 55 million people worldwide live with dementia, facing the same quiet crisis every day — a familiar face without a name, a missed appointment, a routine that simply won't stick. Caregivers carry this burden silently, answering the same questions repeatedly with no tools built to help them. Existing apps are generic, cluttered, and designed for everyone except the people who need them most.
ഓർമ്മ changes that. With face recognition that puts names back to faces, a personal diary to capture each day, a My People directory of everyone who matters, and Gentle Reminders for medications and appointments all wrapped in a calm, accessible design — Recall gives Alzheimer's patients a quiet, reassuring companion that keeps their world from feeling lost.

### The Solution
 ഓർമ്മ is a facial recognition-based memory aid designed for Alzheimer's patients, built using OpenCV's LBPH algorithm trained on locally collected face data. When a face is detected through the live camera feed, the app identifies the person and displays their name and relation to the patient — helping them recognise family members, doctors, and caregivers. The system is entirely offline, ensuring patient privacy, and is complemented by a diary, reminders, and a personal people directory, all accessible through a single Flask-powered web interface.

## Technical Details

### Technologies/Components Used

**For Software:**
-Languages used: Python, HTML5, CSS3, JavaScript (ES6)
-Frameworks used: Flask (RESTful web framework), OpenCV LBPH (Local Binary Pattern Histogram) facial recognition pipeline
-Libraries used: OpenCV (opencv-contrib-python), NumPy, Jinja2 templating engine, Python standard libraries (JSON, OS, DateTime)
-Tools used: VS Code, Git, GitHub, Haar Cascade Classifier ,(pre-trained facial detection model)

## Features

-Real-Time Facial Recognition Pipeline: Implements a locally trained LBPH (Local Binary Pattern Histogram) model with Haar Cascade pre-processing to perform multi-face detection and identity classification through a live MJPEG camera stream, rendering recognised identities with confidence-threshold filtering in real time.

-Caregiver-Controlled Enrolment System: A password-separable caregiver interface allows authorised users to enrol new individuals by capturing a 200-frame face dataset, triggering an on-device model retraining pipeline that updates the recognition system without requiring external compute or cloud dependency.

-Persistent Personal People Directory: Maintains structured JSON-based profiles for each known individual, storing relational metadata, biographical tidbits, and a timestamped conversation history enabling the patient to contextualise and recall past interactions with people in their life.

-Contextual Daily Diary: A chronologically ordered personal journal with collapsible entry rendering, persisted to local storage via a lightweight JSON data layer preserving episodic memory entries across sessions with full read and write access.

-Reminder System: A time-aware daily task management system with per-reminder state toggling, completion progress tracking, and a historical log of past days designed to support medication adherence and routine maintenance for patients with cognitive decline.

-Fully Offline, Privacy-First Architecture: The entire application stack : model training, inference, data storage and UI serving,runs locally on-device with zero network dependency, ensuring sensitive biometric and personal data never leaves the patient's environment.
## Deployment

This application runs locally and is served as a live public link using **ngrok**.

Because the face recognition module requires direct access to a physical webcam,
the app cannot be hosted on traditional cloud platforms like GitHub Pages, 
Vercel or Railway.

### To run locally:
pip install flask opencv-contrib-python numpy
python app.py

### To make it publicly accessible:
ngrok http 5000

This generates a live public URL (e.g. https://abc123.ngrok-free.app) that 
works on any device while your machine is running.

> Note: The public link is only active while the host machine is running 
> both app.py and ngrok simultaneously.

## Implementation

### For Software:

#### Installation
```bash
pip install flask opencv-contrib-python numpy
```

#### Run
```bash
python app.py
```

## Project Documentation

### For Software:

#### Screenshots 
![WhatsApp Image 2026-02-21 at 5 12 55 AM](https://github.com/user-attachments/assets/3802888f-d359-4e27-91a3-97326cd2fbeb)
This is how our face detection looks like in the beginning.It can only detect two people. 

![WhatsApp Image 2026-02-21 at 5 12 55 AM (5)](https://github.com/user-attachments/assets/b3618344-448d-45f9-9caf-80ea5167fc2c)
These are the codes at the beginning.

![WhatsApp Image 2026-02-21 at 5 12 55 AM (4)](https://github.com/user-attachments/assets/caef1a7d-7267-4af5-82df-4606ff949f62)
In this image, we have implemented html,css,javascript and made a minimal UI.

![WhatsApp Image 2026-02-21 at 5 12 55 AM (3)](https://github.com/user-attachments/assets/0086f0c4-c64c-418d-bbb7-a4b4c1800dba)
Now it can smoothly detect the recognized faces.

![WhatsApp Image 2026-02-21 at 5 12 55 AM (2)](https://github.com/user-attachments/assets/7206f11a-1e2d-49d8-b516-b668d1a00522)

#### Diagrams

**System Architecture:**
<img width="1318" height="821" alt="Screenshot 2026-02-21 043853" src="https://github.com/user-attachments/assets/ef54b559-101e-414b-8476-630896a00156" />

-ഓർമ്മ follows a modular monolithic architecture where a single Flask web server acts as the central nervous system, routing requests between four independent feature modules and serving a unified HTML/CSS/JS frontend.

-Component Interaction:
The browser never talks directly to the data layer — all requests go through Flask routes defined in app.py
camera.py is the only component that interfaces with hardware (webcam via OpenCV), streaming live MJPEG frames directly to the browser via the /video_feed route
Training pipeline reads raw face images from faces/, builds the LBPH model, and writes lbph_face_model.xml and label_map.json to disk — these are then loaded by the recognition engine at runtime
All persistent data is stored as local JSON files — no database engine, no external server, no network calls of any kind
Jinja2 templating renders all HTML server-side, meaning the frontend receives fully formed pages rather than raw data payloads


**Application Workflow:**

START
  │
  ▼
Open browser → http://127.0.0.1:5000/home
  │
  ├──────────────────────────────────────────┐
  │                                          │
  ▼                                          ▼
PATIENT SIDE                          CAREGIVER SIDE
  │                                          │
  ├─ Recognise                               ├─ Add New Person
  │   └─ Camera opens                        │   ├─ Enter name + relation
  │   └─ Face detected                       │   └─ Camera captures 200 photos
  │   └─ Name + relation displayed           │       └─ Saved to faces/Name_Relation/
  │                                          │
  ├─ My People                               ├─ Train Model
  │   ├─ View familiar faces                 │   ├─ Reads all face folders
  │   ├─ Click person → view profile         │   ├─ Trains LBPH model
  │   └─ Add conversation note               │   ├─ Saves lbph_face_model.xml
  │                                          │   └─ Saves label_map.json
  ├─ Diary                                   │
  │   ├─ Write new entry                     └─ Recognition engine
  │   └─ Read past entries                       updated immediately
  │
  └─ Reminders
      ├─ View today's tasks
      ├─ Mark tasks as done
      └─ View past days

#### Build Photos

### WEKNOWBALL
![WhatsApp Image 2026-02-21 at 4 52 04 AM](https://github.com/user-attachments/assets/ea8dd211-c118-4160-8958-4ea542695f8a)


## Project Demo

### Video
https://drive.google.com/file/d/1kIHS6YLy6Wyp3YBWk3qhAiYnjsM-5fIU/view?usp=drivesdk
https://drive.google.com/file/d/1q5VePDA6pUEuKCEz5pRjnJYRrJ-8G4Wa/view?usp=drivesdk

## AI Tools Used 
**Tool Used:** VS code, GitHub,ChatGpt,Gemini,Ngrok(For deployment).

**Purpose:** 
-VS Code was the primary code editor used to write, debug, and manage the entire project — from the Flask backend to the frontend templates.
 GitHub served as the version control and collaboration platform, keeping the codebase organized, tracking changes, and allowing the team to work together without overwriting each other's work.
-ChatGPT and Gemini were used as AI-assisted development tools: helping generate boilerplate code, debug errors, suggest UI improvements, and speed up the building process during the hackathon.
-Ngrok acted as a temporary deployment tunnel, exposing the locally running Flask app to the internet so judges, testers, and caregivers could access and demo the application from any device without needing a full cloud deployment.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Made with ❤️ at TinkerHub
