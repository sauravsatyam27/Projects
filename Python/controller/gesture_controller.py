import pyautogui
import math
from utils.smoothing import smooth_point

pyautogui.FAILSAFE = False

class GestureController:
    def __init__(self):
        self.prev_x, self.prev_y = 0, 0
        self.dragging = False

    def update(self, lm):
        x, y = lm[8]  # index tip
        x, y = smooth_point(x, y)  # smoothing
        
        screen_w, screen_h = pyautogui.size()
        cursor_x = int((x / 640) * screen_w)
        cursor_y = int((y / 480) * screen_h)

        pyautogui.moveTo(cursor_x, cursor_y, duration=0)

        # Fingers
        index_up = lm[8][1] < lm[6][1]
        middle_up = lm[12][1] < lm[10][1]

        # LEFT CLICK
        if index_up and not middle_up:
            pyautogui.click()

        # RIGHT CLICK
        if not index_up and middle_up:
            pyautogui.rightClick()

        # DRAG
        if index_up and middle_up:
            if not self.dragging:
                pyautogui.mouseDown()
                self.dragging = True
        else:
            if self.dragging:
                pyautogui.mouseUp()
                self.dragging = False
