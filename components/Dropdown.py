# Components
from components.GeneralComponents import Button

class Dropdown:
    def __init__(self, parent, width, height, xCoord, name, itemMap, color="dark"):
        # Get styles and set styles
        self.style = parent.style

        # Init Components
        self.dropdownButton = Button(
            parent,
            text=name,
            geometry=(0, 0, 130, 54),
            move=(xCoord, 23.5),
            styleSheet=self.style.qssBlueButton if color == "blue" else self.style.qssDarkButton,
            onClick=lambda:self.toggleDropdown()
        )

        self.isVisible = False
        self.dropdownItems = [];
        self.dropdownItemHeight = 55

        i = 0
        for key in itemMap.keys():
            dropdownItem = Button(
                parent,
                text=key,
                geometry=(0, 0, 130, self.dropdownItemHeight),
                move=(xCoord, 90.5 + (i * self.dropdownItemHeight)),
                styleSheet=self.style.qssLighterDarkButton,
                onClick=itemMap[key],
            )

            dropdownItem.component.setVisible(self.isVisible)
            self.dropdownItems.append(dropdownItem)
            i += 1

    def toggleDropdown(self):
        self.isVisible = not self.isVisible

        for dropdownItem in self.dropdownItems:
            dropdownItem.component.setVisible(self.isVisible)
