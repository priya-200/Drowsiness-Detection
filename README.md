# 😴 Drowsiness Detection System using MediaPipe

A real-time drowsiness detection system using MediaPipe Face Mesh and Eye Aspect Ratio (EAR). This project uses your webcam to track facial landmarks, detect if your eyes are closed for too long, and alerts you with an audio alarm if drowsiness is detected.

---

## 🔍 Overview

This project aims to help prevent accidents caused by drowsiness, especially for drivers or machine operators. It leverages:

- 🎯 **MediaPipe** for facial landmark detection  
- 🧠 **Eye Aspect Ratio (EAR)** for detecting eye closure  
- 🎵 **Audio alert system** to wake up a drowsy person  
- 🔴 Real-time video feed from webcam  

---

## ⚙️ How It Works

1. **MediaPipe Face Mesh** detects 468 facial landmarks.
2. Specific eye landmarks are used to calculate EAR.
3. If EAR is below a threshold (e.g., 0.27) for a certain number of frames, the system assumes the eyes are closed.
4. If eyes remain closed for more than `1.5 seconds`, an alarm sound is triggered to wake up the user.

---

## 🧠 Core Concept: Eye Aspect Ratio (EAR)

\[
EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||}
\]

- Open Eye → Higher EAR
- Closed Eye → Lower EAR

Threshold EAR value is empirically set (usually between `0.25 - 0.3`).

---

## 🛠️ Tech Stack

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| Python       | Programming Language                |
| OpenCV       | Video Stream Processing             |
| MediaPipe    | Face Landmark Detection             |
| SciPy        | Distance Calculations               |
| Playsound    | Playing Alarm Sound                 |

---

Install the required libraries:

```bash
pip install -r requirenments.txt
```
## 📌 Features
- 👀 Tracks eye status using 3D landmarks
- 📉 Calculates EAR to detect blinking
- 🔊 Triggers alarm when drowsiness is detected
- 🎯 Lightweight and fast for real-time use

## Future Work
- Add Streamlit or Flask UI
- Use mobile camera for remote monitoring
- Integrate with vehicle systems or smart glasses
