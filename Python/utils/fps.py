import time

class FPS:
    def __init__(self):
        self.prev = time.time()
        self.fps = 0

    def update(self):
        now = time.time()
        self.fps = 1 / (now - self.prev)
        self.prev = now
        return int(self.fps)
