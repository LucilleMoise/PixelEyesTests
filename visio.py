from tkinter import Toplevel, Label
#import mttkinter
#from PIL import Image, ImageTk

from arthurStore import ArthurStore


class Visio:
    def __init__(self):
        self.window = None
        self.panel = None
        self.store = ArthurStore()
        self.image = None
        self.showPanel = False

    def show(self, root):
        if(self.window is None):
            self.window = Toplevel(root)
            self.window.title("Camera")
        self.panel = Label(self.window)
        self.panel.pack()
        self.showPanel = True

    def hide(self):
        self.window.destroy()
        self.window = None
        self.showPanel = False

    #def refresh(self, image):
    #    self.image = cv2.resize(image, (
    #        self.config.cameraProp.width, self.config.cameraProp.height
    #    ), interpolation=cv2.INTER_AREA)
    #    if self.showPanel:
    #        self._displayAll()

    #def _displayAxis(self):
    #    if self.config.hudProp.displayAxis:
    #        cameraProp = self.config.cameraProp
    #        cv2.line(self.image,
    #                 (int(cameraProp.width / 2), 0),
    #                 (int(cameraProp.width / 2), int(cameraProp.height)), (255, 0, 0), 1)
    #        cv2.line(self.image,
    #                 (0, int(cameraProp.height / 2)),
    #                 (cameraProp.width, int(cameraProp.height / 2)), (255, 0, 0), 1)

    #def _displayIdentities(self):
    #    # TODO replace with good condition
    #    if True:  # self.config.hudProp.displayIdentities:
    #        if self.store.facesData is not None:
    #            for face in self.store.facesData:
    #                (x, y, w, h) = face.openCVData
    #                if face.display and face.person is not None:
    #                    font = cv2.FONT_HERSHEY_SIMPLEX
    #                    cv2.putText(self.image, face.person.firstname+" "+face.person.lastname, (x, y-10), font, 0.4, (0, 255, 0))
