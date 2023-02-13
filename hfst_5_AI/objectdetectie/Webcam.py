# Klasse (OOP) om een camera op een aparte thread te starten.
from threading import Thread
import cv2
class Webcam:
    def __init__(self, src=0, fps=60):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.width, self.height =  int(self.stream.get(3)), int(self.stream.get(4))
        self.fps = fps

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:  # Stop de schrijver als de eigenschap stopped = True
                self.stream.release()
                return

            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.grabbed, self.frame

    def stop(self):
        self.stopped = True