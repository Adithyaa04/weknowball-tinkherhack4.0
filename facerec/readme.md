<p align="center">
  <img src="img.png" alt="Project Banner" width="100%">
</p>

# ഓർമ്മ-Remembrance

## Basic Details

### Team Name: WEKNOWBALL

### Team Members
- Member 1: Adithya Vijay - NSS College Of Engineering Palakkad
- Member 2: Snoopa K - NSS College Of Engineering Palakkad

### Hosted Project Link
[mention your project hosted link here]

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
-Tools used: VS Code, Git, GitHub, Haar Cascade Classifier (pre-trained facial detection model)

## Features

-Real-Time Facial Recognition Pipeline: Implements a locally trained LBPH (Local Binary Pattern Histogram) model with Haar Cascade pre-processing to perform multi-face detection and identity classification through a live MJPEG camera stream, rendering recognised identities with confidence-threshold filtering in real time.

-Caregiver-Controlled Enrolment System: A password-separable caregiver interface allows authorised users to enrol new individuals by capturing a 200-frame face dataset, triggering an on-device model retraining pipeline that updates the recognition system without requiring external compute or cloud dependency.

-Persistent Personal People Directory: Maintains structured JSON-based profiles for each known individual, storing relational metadata, biographical tidbits, and a timestamped conversation history enabling the patient to contextualise and recall past interactions with people in their life.

-Contextual Daily Diary: A chronologically ordered personal journal with collapsible entry rendering, persisted to local storage via a lightweight JSON data layer preserving episodic memory entries across sessions with full read and write access.

-Reminder System: A time-aware daily task management system with per-reminder state toggling, completion progress tracking, and a historical log of past days designed to support medication adherence and routine maintenance for patients with cognitive decline.

-Fully Offline, Privacy-First Architecture: The entire application stack : model training, inference, data storage and UI serving,runs locally on-device with zero network dependency, ensuring sensitive biometric and personal data never leaves the patient's environment.

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

#### Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

<img width="2410" height="2253" alt="image" src="https://github.com/user-attachments/assets/94faa3b3-1bbc-481f-bc82-0a8d43cb3ac3" />

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---


### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- Adithya Vijay: [Specific contributions - e.g., Frontend development, API integration, etc.]
- Snoopa K: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
