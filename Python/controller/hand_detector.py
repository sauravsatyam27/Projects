import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6,
            model_complexity=1
        )
        self.mpDraw = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if not result.multi_hand_landmarks:
            return None

        hand = result.multi_hand_landmarks[0]
        h, w, _ = frame.shape
        landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand.landmark]

        self.mpDraw.draw_landmarks(frame, hand, self.mpHands.HAND_CONNECTIONS)

        return landmarks
