import os

class Style:
    def __init__(self):
        self.initColors()
        self.initHelpers()
        self.initQSS()

    def initColors(self):
        self.colorBG = "#212229"
        self.colorBGHover = "#1C1D22"
        self.colorBlue = "#4B7AE5"
        self.colorBlueHover = "#386ADE"
        self.colorDark = "#26272E"
        self.colorDarkHover = "#2B2C34"
        self.colorLighterDark = "#292A34"
        self.colorLighterDarkHover = "#2B2D38"
        self.colorTextFaded = "#939397"

    def initHelpers(self):
        self.borderRadiusSmall = "5px"
        self.borderRadiusBig = "10px"

    def initQSS(self):
        self.qssMainWindow = """
            QMainWindow, QDialog {
                background-color: """ + self.colorBG + """;
            }
        """

        self.qssWelcomeText = """
            QLabel {
                color: white;
                font-size: 60px;
            }
        """

        self.qssButtonReset = lambda color="white" : """
            color: """ + color + """;
            border: none;
            outline: none;
        """

        self.qssLoadFromComputerButton = """
            QPushButton {
                """ + self.qssButtonReset() + """
                background-color: """ + self.colorBlue + """;
                border-radius: """ + self.borderRadiusBig + """;
            }

            QPushButton:hover {
                background-color: """ + self.colorBlueHover + """;
            }
        """

        self.qssLoadRecentFileButton = """
            QPushButton {
                """ + self.qssButtonReset(self.colorTextFaded) + """
                background-color: """ + self.colorDark + """;
                border-radius: """ + self.borderRadiusBig + """;
            }

            QPushButton:hover {
                color: white;
                background-color: """ + self.colorDarkHover + """;
            }
        """

        self.qssCancelButton = self.qssLoadRecentFileButton

        self.qssDarkButton = """
            QPushButton {
                color: white;
                background-color: """ + self.colorBG + """;
                border-radius: """ + self.borderRadiusBig + """;
            }

            QPushButton:hover {
                background-color: """ + self.colorBGHover + """;
            }
        """

        self.qssLighterDarkButton = """
            QPushButton {
                color: white;
                background-color: """ + self.colorLighterDark + """;
                border-radius: 0;
            }

            QPushButton:hover {
                background-color: """ + self.colorLighterDarkHover + """;
            }
        """

        self.qssBlueButton = """
            QPushButton {
                color: white;
                background-color: """ + self.colorBlue + """;
                border-radius: """ + self.borderRadiusBig + """;
            }

            QPushButton:hover {
                background-color: """ + self.colorBlueHover + """;
            }
        """

        self.qssNavbar = """
            QWidget {
                background-color: """ + self.colorDark + """;
            }
        """

        self.qssFilenameText = """
            QLabel {
                text-align: center;
                color: white;
                font-size: 15px;
                background-color: """ + self.colorBG + """;
                border-radius: """ + self.borderRadiusBig + """;
                padding: 0 20px 0 12.5px;
            }
        """

        self.qssInput = """
            QLineEdit {
                color: """ + self.colorTextFaded + """;
                border: none;
                background: """ + self.colorDark + """;
                padding: 0 15px;
            }
        """

        self.qssInputText = """
            QLabel {
                color: white;
                font-size: 15px;
                border-radius: """ + self.borderRadiusBig + """;
            }
        """

        self.qssImage = """
            QLabel {
                background-color: """ + self.colorBG + """;
                padding: 20px;
                border: 2px dashed #44454B;
            }
        """

        self.qssInfoText = self.qssInputText

    def __str__(self):
        return "Stylesheets for EMA -- version 1.0"

if __name__ == "__main__":
    print(Style())