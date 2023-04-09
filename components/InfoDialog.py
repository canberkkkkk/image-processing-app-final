import os

# PyQt
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QDialog

# Components
from components.GeneralComponents import Text, ImageView, Button

class InfoDialog(QDialog):
    def __init__(self, parent, infoType, message):
        super().__init__(parent)

        # Get styles
        self.style = parent.style

        # Init Window
        self.setFixedSize(QSize(350, 300))
        self.setWindowTitle(infoType)
        self.setStyleSheet(self.style.qssMainWindow)

        Text(
            self,
            message,
            geometry=(80, 115, 200, 100),
            styleSheet=self.style.qssInfoText
        )

        ImageView(
            self,
            url=os.getcwd() + "/images/" + ("error.png" if infoType == "ERROR" else "success.png"),
            geometry=(175 - (79 / 2), 50, 79, 83)
        )

        Button(
            self,
            text="OKAY",
            geometry=(0, 0, 130, 50),
            move=(175 - (130 / 2), 200),
            styleSheet=self.style.qssBlueButton,
            onClick=self.destroy
        )

    def render(self):
        self.exec()
    
    def destroy(self):
        self.close()