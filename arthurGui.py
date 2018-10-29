import time
from threading import Thread
from arthurStore import ArthurStore
from PixelEyes import PixelEyes


class ArthurGui(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.eyes = PixelEyes()
        self.root = self.eyes.window
        self.isRun = True
        self.store = ArthurStore()
        self.wait = 15

        self.lastDuration = 0

    def stop(self):
        self.isRun = False

    def run(self):
        while self.isRun:
            start = time.time()
            #self.store.emotion = 'neutral'
            self.eyes.refresh(self.lastDuration)
            self.lastDuration = time.time() - start
            time.sleep(max(1. / 14 - self.lastDuration, 0))
        # des qu'on sort de la boucle alors on ferme les fenêtes des yeux
        self.eyes.quit()
