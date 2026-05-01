import time

class FPSCounter:
    def __init__(self):
        self.prev = time.time()
        self.fps = 0

    def update(self):
        now = time.time()
        dt = now - self.prev
        self.prev = now
        self.fps = int(1 / dt) if dt > 0 else 0
        return self.fps
