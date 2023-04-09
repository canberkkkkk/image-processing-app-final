import os

# PyQt6
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow
from components.InfoDialog import InfoDialog

# Style
from style.Style import Style

# Pages
from pages.Welcome import Welcome
from pages.EditImage import EditImage

#Testing
from components.GeneralComponents import Image

class App(QApplication):
    def __init__(self, title, width, height):
        super().__init__([])
        style = Style();
        self.mainWindow = MainWindow(style, title, width, height)

    def render(self):
        self.mainWindow.render()
        self.exec()

    def destroy(self):
        self.mainWindow.destroy()
        self.destroy()

class MainWindow(QMainWindow):
    def __init__(self, style, title, width, height):
        # Init parents
        super().__init__()

        # Init Constraints
        self.title = title
        self.width = width
        self.height = height

        # Init Window
        self.style = style
        self.setWindowTitle(title)
        self.setFixedSize(QSize(width, height))
        self.setStyleSheet(style.qssMainWindow)
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Router
        self.pages = {
            "welcome": Welcome,
            "edit-image": EditImage
        }
        
        self.push("welcome")

    def loadFromComputerHandler(self):
        self.openEditImage(QFileDialog.getOpenFileName(
            self,
            'Open file', os.getcwd(),
            "Image files (*.jpg *.png)"
        )[0])

    def openEditImage(self, url):
        if(url == ""):
            return

        image = Image()
        openImage = image.open(url)

        if(openImage):
            self.push("edit-image", image=image, filename=os.path.basename(url))
        else:
            infoDialog = InfoDialog(self, "ERROR", "Error happened while opening file")
            infoDialog.render()

    def push(self, component, **kwargs):
        self.setCentralWidget(self.pages[component](self, **kwargs))

    def render(self):
        self.show()

    def destroy(self):
        self.destroy()

if __name__ == "__main__":
    App("EMA | Your new image editing tool", 1200, 750).render()