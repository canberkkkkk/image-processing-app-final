import os

# cv2
import cv2

# PyQt6
from PyQt6.QtWidgets import QFileDialog, QVBoxLayout, QWidget

# Components
from components.Navbar import Navbar
from components.Dropdown import Dropdown
from components.GeneralComponents import ImageView
from components.SingleInputDialog import SingleInputDialog
from components.ColorBalanceDialog import ColorBalanceDialog
from components.CropDialog import CropDialog
from components.InfoDialog import InfoDialog

# Image Processing Methods
from processing.Filters import filterBlur, filterDeblur, filterDetectEdges, filterToGrayscale
from processing.Enhance import enhanceContrast, enhanceBrightness, enhanceSaturation, enhanceColorBalance
from processing.Ops import opsCropImage, opsFlipImage, opsMirrorImage, opsReverseColors, opsRotateImage

class EditImage(QWidget):
    def __init__(self, MainWindow, filename="None", **kwargs):
        # Init Parents
        super().__init__()

        # Init Main Window
        self.mainWindow = MainWindow
        self.style = self.mainWindow.style

        # Init Image
        if "image" not in kwargs:
            self.mainWindow.push("welcome")

        self.inputImage = kwargs["image"]
        self.outputImage = kwargs["image"]

        # Init Right Side
        ImageView(
            self,
            image=self.inputImage,
            geometry=(75, 167.5, 475, 500),
            styleSheet=self.style.qssImage
        )

        outputImageView = ImageView(
            self,
            image=self.outputImage,
            geometry=(650, 167.5, 475, 500),
            styleSheet=self.style.qssImage
        )

        # Init layout
        layout = QVBoxLayout()
        layout.addWidget(Navbar(self, self.mainWindow.width, filename=filename))

        self.dropdownFilters = Dropdown(self, self.mainWindow.width, self.mainWindow.height, 545, "Filters", {
            "Grayscale": lambda: self.grayscaleOperation(outputImageView, self.outputImage),
            "Blur": lambda: self.singleDialogOperation(
                "Blur",
                "Enter Value for Blur",
                lambda n: filterBlur(outputImageView, self.outputImage, n)
            ),
            "Deblur": lambda: self.singleDialogOperation(
                "Deblur",
                "Enter Value for Deblur",
                lambda n: filterDeblur(outputImageView, self.outputImage, n)
            ),
            "Detect Edges": lambda: self.operation(lambda: filterDetectEdges(outputImageView, self.outputImage))
        })

        self.dropdownEnhancement = Dropdown(self, self.mainWindow.width, self.mainWindow.height, 695, "Enhancement", {
            "Contrast": lambda: self.singleDialogOperation(
                "Contrast",
                "Value for Contrast",
                lambda n: enhanceContrast(outputImageView, self.outputImage, n),
            ),
            "Brightness": lambda: self.singleDialogOperation(
                "Brightness",
                "Value for Brightness",
                lambda n: enhanceBrightness(outputImageView, self.outputImage, n),
            ),
            "Saturation": lambda: self.singleDialogOperation(
                "Saturation",
                "Value for Saturation",
                lambda n: enhanceSaturation(outputImageView, self.outputImage, n),
            ),
            "Color Balance": lambda: self.colorBalanceOperation(
                "Color Balance",
                "Value for Color Balance",
                lambda r, g, b: enhanceColorBalance(outputImageView, self.outputImage, r, g, b),
            ),
        })

        self.dropdownOperations = Dropdown(self, self.mainWindow.width, self.mainWindow.height, 845, "Operations", {
            "Reverse Color": lambda: self.operation(lambda: opsReverseColors(outputImageView, self.outputImage)),
            "Flip Image": lambda: self.operation(lambda: opsFlipImage(outputImageView, self.outputImage)),
            "Mirror Image": lambda: self.operation(lambda: opsMirrorImage(outputImageView, self.outputImage)),
            "Rotate Image": lambda: self.singleDialogOperation(
                "Rotate Image",
                "Enter Value for Rotation",
                lambda n: opsRotateImage(outputImageView, self.outputImage, n)
            ),
            "Crop Image": lambda: self.cropDialogOperation(
                "Crop Image",
                "Enter Value for Cropping",
                lambda top, right, bottom, left: opsCropImage(outputImageView, self.outputImage, top, right, bottom, left)
            ),
        })

        self.dropdownFile = Dropdown(self, self.mainWindow.width, self.mainWindow.height, 995, "File", {
            "Save Image": self.saveImage,
            "Load Image": self.loadImage,
        }, color="blue")

    def grayscaleOperation(self, outputImageView, outputImage):
        self.closeDropdowns()
        if(filterToGrayscale(outputImageView, outputImage) is False):
            errorDialog = InfoDialog(self, "ERROR", "Image is already grayscaled!")
            errorDialog.render()

    def singleDialogOperation(self, title, label, handler):
        self.closeDropdowns()
        singleInputDialog = SingleInputDialog(self, title, label, handler)
        singleInputDialog.render()

    def colorBalanceOperation(self, title, label, handler):
        self.closeDropdowns()
        colorBalanceDialog = ColorBalanceDialog(self, title, label, handler)
        colorBalanceDialog.render()

    def cropDialogOperation(self, title, label, handler):
        self.closeDropdowns()
        cropDialog = CropDialog(self, title, label, handler)
        cropDialog.render()

    def loadImage(self):
        self.closeDropdowns()
        self.mainWindow.loadFromComputerHandler()

    def saveImage(self):
        self.closeDropdowns()
        imgName = QFileDialog.getSaveFileName(
            self,
            'Save File',
            os.getcwd(),
        )[0]

        if(imgName == ""):
            return

        if(not (os.path.basename(imgName).endswith(".jpg") or os.path.basename(imgName).endswith(".png"))):
            errorDialog = InfoDialog(self, "ERROR", "Image needs to be .jpg or .png!")
            errorDialog.render()
            return

        cv2.imwrite(imgName, self.outputImage.get())

    def operation(self,func):
        self.closeDropdowns()
        func()

    def closeDropdowns(self):
        if(self.dropdownFilters.isVisible is True):
            self.dropdownFilters.toggleDropdown()

        if(self.dropdownOperations.isVisible is True):
            self.dropdownOperations.toggleDropdown()

        if(self.dropdownEnhancement.isVisible is True):
            self.dropdownEnhancement.toggleDropdown()

        if(self.dropdownFile.isVisible is True):
            self.dropdownFile.toggleDropdown()