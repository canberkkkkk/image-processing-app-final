import os

# cv2
import cv2

# PIL
from PIL import Image as PILImage

# Numpy
import numpy as np

# PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QImage
from PyQt6.QtWidgets import QLabel, QPushButton

class Component:
    def __init__(self, component, parent, **kwargs):
        self.component = component(parent)

        # Set Features
        if("geometry" in kwargs):
            self.component.setGeometry(*kwargs.get("geometry"))

        if("move" in kwargs):
            self.component.move(*kwargs.get("move"))

        if("styleSheet" in kwargs):
            self.component.setStyleSheet(kwargs.get("styleSheet"))

class Image:
    def open(self, url):
        try:
            if os.path.exists(url):
                self.set(url, True)
                self.verify()
            else:
                raise Exception
        except Exception:
            return False

        return True

    def set(self, img, firstTime = False):
        self.img = cv2.imread(img) if firstTime else img

        # Constraints
        self.height, self.width = self.img.shape[:2]
        self.channels = self.img.shape[2] if len(self.img.shape) == 3 else 1

        # Set PIL Image as well
        self.imgPIL = PILImage.fromarray(self.img)

        # Return self for chaining
        return self

    def setPIL(self, img):
        return self.set(np.asarray(img))

    def get(self, type = "CV2"):
        return self.imgPIL if type == "PIL" else self.img

    def dimensions(self):
        return (self.width, self.height)

    def verify(self):
        return self.imgPIL.verify()

class ImageView(Component):
    def __init__(self, parent, url = None, image = None, **kwargs):
        Component.__init__(self, QLabel, parent, **kwargs)
        
        self.width = kwargs.get("geometry")[2]
        self.height = kwargs.get("geometry")[3]

        if url is None and image is None:
            raise Exception("Please specify an url or image")
        elif url is not None:
            self.image = Image()
            if self.image.open(url) is False:
                raise Exception("Cannot display view, the url or the image is broken")
        elif image is not None:
            self.image = image
            
        self.setImage(changeImage=False)

    def setImage(self, img = None, firstTime = False, PIL = False, changeImage = True):
        if changeImage:
            self.image.set(img, firstTime)

        self.renderPixmap()

    def renderPixmap(self):
        # Set Pixmap
        pixmap = QPixmap(QImage(
            self.image.img.data,
            self.image.width,
            self.image.height,
            self.image.channels * self.image.width,
            QImage.Format.Format_Grayscale8 if self.image.channels == 1 else QImage.Format.Format_BGR888
        ))

        self.component.setPixmap(pixmap.scaled(
            self.width,
            self.height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

        self.component.setAlignment(Qt.AlignmentFlag.AlignCenter)

class Text(Component):
    def __init__(self, parent, text, **kwargs):
        super().__init__(QLabel, parent, **kwargs)

        # Init Text
        self.component.setText(text)

class Button(Component):
    def __init__(self, parent, **kwargs):
        super().__init__(QPushButton, parent, **kwargs)

        # Init Button
        self.component.setCursor(Qt.CursorShape.PointingHandCursor)

        if("text" in kwargs):
            self.component.setText(kwargs.get("text"))
        
        if("icon" in kwargs):
            self.component.setIcon(QIcon(QPixmap(kwargs.get("icon"))))

        # Events
        if("onClick" in kwargs):
            self.component.clicked.connect(kwargs.get("onClick"))