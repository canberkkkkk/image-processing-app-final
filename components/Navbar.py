# PyQt6
from PyQt6.QtWidgets import QWidget

# Components
from components.GeneralComponents import Text

class Navbar(QWidget):
    def __init__(self, parent, width, filename):
        # Init Parents
        super().__init__(parent)

        # Get styles and set styles
        self.style = parent.style
        self.setStyleSheet(self.style.qssNavbar)
        self.setGeometry(0, 0, width, 100)

        # Init Components
        Text(
            self,
            filename,
            geometry=(0, 0, 165, 55),
            move=(75, 23.5),
            styleSheet=self.style.qssFilenameText
        )
