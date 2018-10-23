from tkinter import Canvas, Tk, Label, StringVar, Frame
from gui import GuiConfig
from arthurStore import ArthurStore
import keyboard

# Pour les pixel eyes
DOT_WIDTH = 18
DOT_HEIGHT = 18

EYES = {
    'neutral':
        (
            (0, 1, 1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1),
            (0, 1, 1, 1, 1, 1, 0)
        ),
    'contempt':
        (
            (0, 0, 0, 0, 0, 0, 0),
            (0, 1, 1, 0, 1, 1, 0),
            (1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1),
            (0, 1, 1, 1, 1, 1, 0),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 0, 0, 1, 0, 0, 0)
        ),
    'fear':
        (
            (1, 0, 0, 0, 0, 0, 1),
            (0, 1, 0, 0, 0, 1, 0),
            (0, 0, 1, 0, 1, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 1, 0, 1, 0, 0),
            (0, 1, 0, 0, 0, 1, 0),
            (1, 0, 0, 1, 0, 0, 1)
        ),
    'happiness':
        (
            (0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 1, 1, 0, 1, 1, 0),
            (1, 1, 0, 0, 0, 1, 1),
            (1, 0, 0, 0, 0, 0, 1),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    'sadness':
        (
            (0, 1, 1, 1, 1, 0, 0),
            (0, 1, 1, 1, 1, 0, 0),
            (0, 1, 1, 1, 1, 0, 0),
            (0, 1, 1, 1, 1, 0, 0),
            (0, 0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 1, 0)
        ),
    'sadnessB':
        (
            (0, 0, 1, 1, 1, 1, 0),
            (0, 0, 1, 1, 1, 1, 0),
            (0, 0, 1, 1, 1, 1, 0),
            (0, 0, 1, 1, 1, 1, 0),
            (0, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0)
        ),
    'surprise':
        (
            (0, 0, 0, 0, 1, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 1, 0, 0, 0, 0),
            (0, 1, 0, 1, 1, 1, 0),
            (0, 0, 0, 1, 1, 1, 0),
            (0, 0, 0, 1, 1, 1, 0),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    'surpriseB':
        (
            (0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0, 0),
            (0, 1, 1, 1, 0, 1, 0),
            (0, 1, 1, 1, 0, 0, 0),
            (0, 1, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    'disgust':
        (
            (0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 1, 0),
            (1, 1, 1, 1, 1, 1, 0),
            (1, 0, 0, 0, 0, 0, 0),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 0, 1, 1, 1, 0, 0)
        ),
    'disgustB':
        (
            (0, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0),
            (0, 1, 1, 1, 1, 1, 1),
            (0, 0, 0, 0, 0, 0, 1),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 0, 1, 1, 1, 0, 0),
            (0, 0, 1, 1, 1, 0, 0)
        ),
    'anger':
        (
            (0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0, 0),
            (0, 1, 1, 1, 0, 1, 0),
            (0, 1, 1, 1, 0, 0, 0),
            (0, 1, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    'angerB':
        (
            (0, 0, 0, 0, 1, 0, 0),
            (0, 0, 0, 1, 0, 0, 0),
            (0, 0, 1, 0, 0, 0, 0),
            (0, 1, 0, 1, 1, 1, 0),
            (0, 0, 0, 1, 1, 1, 0),
            (0, 0, 0, 1, 1, 1, 0),
            (0, 0, 0, 0, 0, 0, 0)
        )
}


class PixelEyes:

    def __init__(self):
        # self.pointer = StringVar()
        self.guiProp = GuiConfig()
        self.store = ArthurStore()
        self._initWindow()
        self._initCanvas()
        self._initEyes()
        self.percentOffsetX = 1.84
        self.percentOffsetY = 1.84
        self.durationEmotion = 0

    def quit(self):
        self.window.destroy()

    def _initWindow(self):
        self.window = Tk()
        self.window.attributes('-fullscreen', self.guiProp.fullscreen)
        # self.window = Toplevel(self.window)

    def _initCanvas(self):
        self.head = Canvas(
            self.window,
            width=self.guiProp.width,
            height=self.guiProp.height,
            bg=self.guiProp.backgroundColor
        )
        self.head.pack()
        self.pointer = StringVar()
        t = Label(self.window, textvariable=self.pointer, fg="red")
        t.pack()
        self.posPupille = StringVar()
        td = Label(self.window, textvariable=self.posPupille, fg="red")
        td.pack()



    def changeEmotion(self):
        if keyboard.is_pressed('c'):
            print("Change emotion")
            self.durationEmotion = 10
            self.store.emotion = 'sadness'

    def refresh(self, lastDuration):
        if self.store.resetEyes:
            self.reset()
            self.store.resetEyes = False

        self.resetRectangle()
        self.changeExpression(lastDuration)
            # self.store.resetEmotion = False
        self.window.update_idletasks()
        self.window.update()
        # print("refresh")

    def _initEyes(self):
        prop = self.guiProp
        self.lastOffsetX = 0.0
        self.lastOffsetY = 0.0
        self.durationEmotion = 0
        self.eyeL = []
        self.eyeR = []
        self.diff = self.rightEye()
        self.changeExpression(0)
        frame = Frame(self.window)
        frame.pack()
        eyes = self.store.emotion
        eyesB = self.rightEye()
        for i, row in enumerate(EYES.get(eyes, ())):
            for j, col in enumerate(row):
                if col:
                    self._cursor_pos = prop.width * 0.30 - DOT_WIDTH*7/2
                    self._line_pos = prop.height * 0.5 - DOT_HEIGHT*7/2
                    self.eyeL.append(self.head.create_rectangle( self._cursor_pos + j * DOT_WIDTH,
                                      self._line_pos + i * DOT_HEIGHT,
                                      self._cursor_pos + (j + 1) * DOT_WIDTH,
                                      self._line_pos + (i + 1) * DOT_HEIGHT,
                                      fill = '#60b6d5'
                                    ))

                    self._cursor_pos = prop.width * 0.70 - DOT_WIDTH*7/2
                    if eyes == eyesB:
                        self.eyeR.append(self.head.create_rectangle( self._cursor_pos + j * DOT_WIDTH,
                                        self._line_pos + i * DOT_HEIGHT,
                                        self._cursor_pos + (j + 1) * DOT_WIDTH,
                                        self._line_pos + (i + 1) * DOT_HEIGHT,
                                        fill = '#60b6d5'
                                      ))
        if eyes != eyesB:
            for i, row in enumerate(EYES.get("AngryB", ())):
                for j, col in enumerate(row):
                    if col:
                        self._cursor_pos = prop.width * 0.70 - DOT_WIDTH*7/2
                        self.eyeL.append(self.head.create_rectangle( self._cursor_pos + j * DOT_WIDTH,
                                        self._line_pos + i * DOT_HEIGHT,
                                        self._cursor_pos + (j + 1) * DOT_WIDTH,
                                        self._line_pos + (i + 1) * DOT_HEIGHT,
                                        fill = '#60b6d5'
                                      ))


    def reset(self):
        self.positionEyesX = 0.0
        self.positionEyesY = 0.0
        self.lastOffsetX = 0.0
        self.lastOffsetY = 0.0
        self.applyNewEyesPosition()

    def _initEvents(self):
        self.shutdown = False

    def computeEyesPosition(self):
        prop = self.guiProp

    def applyNewEyesPosition(self):
        # t = Label(self.window, text="nik ta race", fg="red")
        # t.pack()

        offsetX = self.positionEyesX * self.percentOffsetX
        offsetY = self.positionEyesY * self.percentOffsetY

        for pixel in self.eyeL:
            x1, y1, w1, h1 = self.head.coords(pixel)
            x1 += offsetX - self.lastOffsetX
            w1 += offsetX - self.lastOffsetX
            y1 += offsetY - self.lastOffsetY
            h1 += offsetY - self.lastOffsetY
            self.head.coords(pixel, x1, y1, w1, h1)
        for pixel in self.eyeR:
            x1, y1, w1, h1 = self.head.coords(pixel)
            x1 += offsetX - self.lastOffsetX
            w1 += offsetX - self.lastOffsetX
            y1 += offsetY - self.lastOffsetY
            h1 += offsetY - self.lastOffsetY
            self.head.coords(pixel, x1, y1, w1, h1)
        self.lastOffsetX = offsetX
        self.lastOffsetY = offsetY



    def calculPupillex(self):
        sourisx = self.window.winfo_pointerx()
        if sourisx >= 0 & sourisx <= 1440:
            xWindowPercent = sourisx/1440 * 100
            xEyePos = round(xWindowPercent / 100 * 6)
            return xEyePos
        else:
            return -1

    def calculPupilley(self):
        sourisy = self.window.winfo_pointery()
        if sourisy >= 0 & sourisy <= 900:
            yWindowPercent = sourisy/900 * 100
            yEyePos = round(yWindowPercent / 100 * 6)
            return yEyePos
        else:
            return -1

    def calculPupille(self):

        yEyePos = 3
        xEyePos = 3
        sourisx = self.window.winfo_pointerx()
        sourisy = self.window.winfo_pointery()
        if sourisx >= 0 & sourisx <= self.guiProp.width:
            if sourisy >= 0 & sourisy <= self.guiProp.height:
                xWindowPercent = sourisx / self.guiProp.width * 100
                yWindowPercent = sourisy / self.guiProp.height * 100
                xEyePos = round(xWindowPercent / 100 * 6)
                yEyePos = round(yWindowPercent / 100 * 6)

        return {'x': xEyePos, 'y': yEyePos}

    def changeExpression(self, lastDuration):
        self.changeEmotion()
        pupillePos = self.calculPupille()

        self.pointer.set(str(self.window.winfo_pointerx()) + " " + str(self.window.winfo_pointery()))
        self.posPupille.set(str(pupillePos['x']) + " " + str(pupillePos['y']))
        eyes = self.store.emotion
        eyesB = self.rightEye()

        for i, row in enumerate(EYES.get(eyes, ())):
            for j, col in enumerate(row):
                if self.store.emotion == 'neutral' and self.durationEmotion <= 0:
                    if col & (j != pupillePos['x']) | col & (i != pupillePos['y']):
                        self._cursor_pos = self.guiProp.width * 0.30 - DOT_WIDTH * 7 / 2
                        self._line_pos = self.guiProp.height * 0.5 - DOT_HEIGHT * 7 / 2
                        self.eyeL.append(self.head.create_rectangle(self._cursor_pos + j * DOT_WIDTH,
                                                                    self._line_pos + i * DOT_HEIGHT,
                                                                    self._cursor_pos + (j + 1) * DOT_WIDTH,
                                                                    self._line_pos + (i + 1) * DOT_HEIGHT,
                                                                    fill='#60b6d5'
                                                                    ))

                        self._cursor_pos = self.guiProp.width * 0.70 - DOT_WIDTH * 7 / 2
                        #if eyes == eyesB:
                        self.eyeR.append(self.head.create_rectangle(self._cursor_pos + j * DOT_WIDTH,
                                                                    self._line_pos + i * DOT_HEIGHT,
                                                                    self._cursor_pos + (j + 1) * DOT_WIDTH,
                                                                    self._line_pos + (i + 1) * DOT_HEIGHT,
                                                                    fill='#60b6d5'
                                                                    ))
                else:
                    self.durationEmotion -= lastDuration
                    if self.durationEmotion <= 0:
                        self.store.emotion = "neutral"
                    if col:
                        self._cursor_pos = self.guiProp.width * 0.30 - DOT_WIDTH * 7 / 2
                        self._line_pos = self.guiProp.height * 0.5 - DOT_HEIGHT * 7 / 2
                        self.eyeL.append(self.head.create_rectangle(self._cursor_pos + j * DOT_WIDTH,
                                                                    self._line_pos + i * DOT_HEIGHT,
                                                                    self._cursor_pos + (j + 1) * DOT_WIDTH,
                                                                    self._line_pos + (i + 1) * DOT_HEIGHT,
                                                                    fill='#60b6d5'
                                                                    ))

                        self._cursor_pos = self.guiProp.width * 0.70 - DOT_WIDTH * 7 / 2
                        if eyes == eyesB:
                            self.eyeR.append(self.head.create_rectangle(self._cursor_pos + j * DOT_WIDTH,
                                                                        self._line_pos + i * DOT_HEIGHT,
                                                                        self._cursor_pos + (j + 1) * DOT_WIDTH,
                                                                        self._line_pos + (i + 1) * DOT_HEIGHT,
                                                                        fill='#60b6d5'
                                                                        ))

        if eyes != eyesB:
            for i, row in enumerate(EYES.get(eyesB, ())):
                for j, col in enumerate(row):
                    if col:
                        self._cursor_pos = self.guiProp.width * 0.70 - DOT_WIDTH * 7 / 2
                        self.eyeR.append(self.head.create_rectangle(self._cursor_pos + j * DOT_WIDTH,
                                                                    self._line_pos + i * DOT_HEIGHT,
                                                                    self._cursor_pos + (j + 1) * DOT_WIDTH,
                                                                    self._line_pos + (i + 1) * DOT_HEIGHT,
                                                                    fill='#60b6d5'))

    def resetRectangle(self):
        self.head.delete("all")
        self.eyeL[:] = []
        self.eyeR[:] = []

    def rightEye(self):
        e = self.store.emotion
        droite = e
        if e == "anger":
            droite = "angerB"
        if e == "sadness":
            droite = "sadnessB"
        if e == "surprise":
            droite = "surpriseB"
        if e == "disgust":
            droite = "disgustB"
        return droite
