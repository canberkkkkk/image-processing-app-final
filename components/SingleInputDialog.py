import os

# PyQt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QDialog, QLineEdit

# Components
from components.GeneralComponents import Text, ImageView, Button

class SingleInputDialog(QDialog):
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

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText(str(0.0))
        self.lineEdit.setValidator(QDoubleValidator(0.0, 100.0, 2, notation=QDoubleValidator.Notation.StandardNotation))
        self.lineEdit.setStyleSheet(self.style.qssInput)
        self.lineEdit.setGeometry(35, 195, 280, 50)

        Text(
            self,
            label,
            geometry=(0, 0, 200, 100),
            move=(107.5, 110),
            styleSheet=self.style.qssInputText
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/icon-image.png",
            geometry=(175 - (79 / 2), 50, 79, 83)
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
        self.handler(float(self.lineEdit.text()))
        self.destroy()

    def render(self):
        self.exec()
    
    def destroy(self):
        self.close()