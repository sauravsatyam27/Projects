import cv2
import mediapipe as mp
import pyautogui
import time
from controller.hand_detector import HandDetector
from controller.gesture_controller import GestureController
from controller.fps import FPSCounter

# Auto camera search
def find_camera():
    print("🔍 Searching for available camera...")
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            print(f"📷 Camera found at index {i}")
            return i
    print("❌ ERROR: No camera detected!")
    exit()

CAM_INDEX = find_camera()
cap = cv2.VideoCapture(CAM_INDEX)

detector = HandDetector()
gestures = GestureController()
fps_counter = FPSCounter()

print("✅ System is ready. Show your hand to control the mouse.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame read error!")
        break

    frame = cv2.flip(frame, 1)
    landmarks = detector.get_landmarks(frame)

    if landmarks is not None and len(landmarks) >= 21:
        gestures.update(landmarks)

    # Display FPS
    fps = fps_counter.update()
    cv2.putText(frame, f"FPS: {fps}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
