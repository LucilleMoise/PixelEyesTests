import time


class ArthurStore:

    def __init__(self):
        start = time.time()
        self.facesDetected = []
        #Tous les cadres détectés
        self.facesData = None
        self.faceApiRecall = start
        self.redirectHead = start
        self.redirectWheels = start
        self.timeoutCalm = start
        self.timeoutNobody = start
        self.nbFaces = 0
        self.nbConnections = 0
        self.presentate = False
        #Affiche la caméra
        self.showVisio = False
        self.controlWheels = False
        self.isCalm = True
        self.disableArduinos = False
        self.resetEyes = False
        self.ipController = None
        self.listIPsConnected = []
        self.resetEmotion = True
        self.emotion = "neutral"
        self.durationEmotion = 0
        #Variable peremettant de savoir si on a vue quelqu'un mais pas reconnu
        self.personSeenButNotRecognize = False
        # Image de la personne reconnu
        self.personSeenButNotRecognizeImage = None
