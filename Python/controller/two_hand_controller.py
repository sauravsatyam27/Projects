import pyautogui

class TwoHandController:
    def __init__(self):
        pass

    def control_left_hand(self, left_landmarks):
        thumb = left_landmarks[4]
        index = left_landmarks[8]
        middle = left_landmarks[12]

        # Volume control (thumb + index pinch)
        if abs(thumb[1] - index[1]) < 40:
            if thumb[1] < index[1]:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")
            return "volume"

        # Brightness (thumb + middle pinch)
        if abs(thumb[1] - middle[1]) < 40:
            if thumb[1] < middle[1]:
                pyautogui.press("brightnessup")
            else:
                pyautogui.press("brightnessdown")
            return "brightness"

        return "none"
