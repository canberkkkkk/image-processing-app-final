import os

# PyQt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QDialog, QLineEdit

# Components
from components.GeneralComponents import Text, ImageView, Button
from components.InfoDialog import InfoDialog

class ColorBalanceDialog(QDialog):
    def __init__(self, parent, title, label, handler):
        super().__init__(parent)

        # Get styles
        self.style = parent.style
        
        # Set Handler
        self.handler = handler

        # Init Window
        self.setFixedSize(QSize(350, 350))
        self.setWindowTitle(title)
        self.setStyleSheet(self.style.qssMainWindow)

        self.r = QLineEdit(self)
        self.r.setText(str(0))
        self.r.setValidator(QIntValidator(-255, 255))
        self.r.setStyleSheet(self.style.qssInput)
        self.r.setGeometry(65, 195, 55, 42)

        self.g = QLineEdit(self)
        self.g.setText(str(0))
        self.g.setValidator(QIntValidator(-255, 255))
        self.g.setStyleSheet(self.style.qssInput)
        self.g.setGeometry(165, 195, 55, 42)

        self.b = QLineEdit(self)
        self.b.setText(str(0))
        self.b.setValidator(QIntValidator(-255, 255))
        self.b.setStyleSheet(self.style.qssInput)
        self.b.setGeometry(265, 195, 55, 42)

        Text(
            self,
            label,
            geometry=(0, 0, 200, 100),
            move=(105, 110),
            styleSheet=self.style.qssInputText
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/icon-image.png",
            geometry=(175 - (79 / 2), 50, 79, 83)
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/red.png",
            geometry=(35, 207.5, 16, 18)
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/green.png",
            geometry=(135, 207.5, 16, 18)
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/blue.png",
            geometry=(235, 207.5, 16, 18)
        )

        Button(
            self,
            text="Cancel",
            geometry=(0, 0, 130, 50),
            move=(35, 275),
            styleSheet=self.style.qssCancelButton,
            onClick=lambda: self.close()
        )

        Button(
            self,
            text="Apply",
            geometry=(0, 0, 130, 50),
            move=(185, 275),
            styleSheet=self.style.qssBlueButton,
            onClick=self.onClickHandler
        )

    def onClickHandler(self):
        self.destroy()

        if(self.handler(int(self.r.text()), int(self.g.text()), int(self.b.text())) is False):
            errorDialog = InfoDialog(self, "ERROR", "Image is already grayscaled!")
            errorDialog.render()

    def render(self):
        self.exec()
    
    def destroy(self):
        self.close()