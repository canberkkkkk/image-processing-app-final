import os

# PyQt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtWidgets import QDialog, QLineEdit

# Components
from components.GeneralComponents import Text, ImageView, Button
from components.InfoDialog import InfoDialog

class CropDialog(QDialog):
    def __init__(self, parent, title, label, handler):
        super().__init__(parent)

        # Get styles
        self.style = parent.style
        
        # Set Handler
        self.handler = handler

        # Init Window
        self.setFixedSize(QSize(490, 350))
        self.setWindowTitle(title)
        self.setStyleSheet(self.style.qssMainWindow)

        self.top = QLineEdit(self)
        self.top.setText(str(0))
        self.top.setValidator(QIntValidator())
        self.top.setStyleSheet(self.style.qssInput)
        self.top.setGeometry(60, 195, 55, 42)

        self.right = QLineEdit(self)
        self.right.setText(str(0))
        self.right.setValidator(QIntValidator())
        self.right.setStyleSheet(self.style.qssInput)
        self.right.setGeometry(180, 195, 55, 42)

        self.bottom = QLineEdit(self)
        self.bottom.setText(str(0))
        self.bottom.setValidator(QIntValidator())
        self.bottom.setStyleSheet(self.style.qssInput)
        self.bottom.setGeometry(310, 195, 55, 42)

        self.left = QLineEdit(self)
        self.left.setText(str(0))
        self.left.setValidator(QIntValidator())
        self.left.setStyleSheet(self.style.qssInput)
        self.left.setGeometry(415, 195, 55, 42)

        Text(
            self,
            label,
            geometry=(0, 0, 200, 100),
            move=(165, 110),
            styleSheet=self.style.qssInputText
        )

        Text(
            self,
            "Top",
            geometry=(0, 0, 50, 100),
            move=(25, 165),
            styleSheet=self.style.qssInputText
        )

        Text(
            self,
            "Right",
            geometry=(0, 0, 50, 100),
            move=(135, 165),
            styleSheet=self.style.qssInputText
        )

        Text(
            self,
            "Bottom",
            geometry=(0, 0, 50, 100),
            move=(255, 165),
            styleSheet=self.style.qssInputText
        )

        Text(
            self,
            "Left",
            geometry=(0, 0, 50, 100),
            move=(380, 165),
            styleSheet=self.style.qssInputText
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/icon-image.png",
            geometry=(245 - (79 / 2), 50, 79, 83)
        )

        Button(
            self,
            text="Cancel",
            geometry=(0, 0, 130, 50),
            move=(95, 275),
            styleSheet=self.style.qssCancelButton,
            onClick=lambda: self.close()
        )

        Button(
            self,
            text="Apply",
            geometry=(0, 0, 130, 50),
            move=(255, 275),
            styleSheet=self.style.qssBlueButton,
            onClick=self.onClickHandler
        )

    def onClickHandler(self):
        self.destroy()

        try:
            self.handler(int(self.top.text()), int(self.right.text()), int(self.bottom.text()), int(self.left.text()))
        except:
            errorDialog = InfoDialog(self, "ERROR", "Tile cannot extend the image!")
            errorDialog.render()

    def render(self):
        self.exec()
    
    def destroy(self):
        self.close()