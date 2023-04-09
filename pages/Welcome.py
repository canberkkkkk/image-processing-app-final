import os

# PyQt6
from PyQt6.QtWidgets import QWidget

# Components
from components.GeneralComponents import ImageView, Text, Button

class Welcome(QWidget):
    def __init__(self, MainWindow, **kwargs):
        # Init Parents
        super().__init__()

        # Init Main Window
        self.mainWindow = MainWindow
        self.style = self.mainWindow.style
        
        # Init Left Side
        Text(
            self,
            "Welcome,",
            geometry=(0, 0, 350, 100),
            move=(150, 250),
            styleSheet=self.style.qssWelcomeText
        )

        Button(
            self,
            text="Load file from computer",
            geometry=(0, 0, 350, 60),
            move=(150, 365),
            styleSheet=self.style.qssLoadFromComputerButton,
            onClick=self.mainWindow.loadFromComputerHandler
        )

        # Init Right Side
        ImageView(
            self,
            url=os.getcwd() + "/images/welcome.png",
            geometry=(MainWindow.width - 550, 0, 550,
            MainWindow.height)
        )