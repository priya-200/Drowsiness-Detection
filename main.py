import numpy as np
import cv2
import mediapipe as mp
from scipy.spatial import distance as dist
from playsound import playsound
import threading
import time


THRESHOLD = 0.27         
CONSEC_FRAMES = 10       
GAMMA = 1.5

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


COUNTER = 0
ALARM_ON = False

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def sound_alarm():
    global ALARM_ON
    playsound("alert audio\\alert.wav")  
    ALARM_ON = False

# Video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    isTrue, frame = cap.read()
    if not isTrue:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            h, w, _ = frame.shape
            left = []
            right = []

            for idx in LEFT_EYE:
                pt = landmarks.landmark[idx]
                x, y = int(pt.x * w), int(pt.y * h)
                left.append((x, y))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            for idx in RIGHT_EYE:
                pt = landmarks.landmark[idx]
                x, y = int(pt.x * w), int(pt.y * h)
                right.append((x, y))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Compute EAR
            leftEAR = eye_aspect_ratio(left)
            rightEAR = eye_aspect_ratio(right)
            ear = (leftEAR + rightEAR) / 2.0

            if ear < THRESHOLD:
                COUNTER += 1
                if COUNTER >= CONSEC_FRAMES:
                    if not ALARM_ON:
                        ALARM_ON = True
                        threading.Thread(target=sound_alarm).start()
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            else:
                COUNTER = 0
                ALARM_ON = False

            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
