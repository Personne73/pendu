from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def error_state(top_grid_layout, pictures_list, errors):
    """
    Function to change the pictures depending on the number of errors
    :param top_grid_layout: the layout
    :param pictures_list: the list of pictures
    :param errors: the number of errors
    """
    picture = Pictures(pictures_list, errors)
    picture.display(top_grid_layout)


class Pictures:
    """
    Class that manages the hangman picture of the errors
    """
    def __init__(self, liste, index):
        self.liste = liste
        self.index = index

    def display(self, widget):
        """
        Function that display the pictures
        :param widget: the widget used
        """
        name = self.liste[self.index]
        pixmap = QPixmap(f"../images/{name}")
        picture_label = QLabel()
        picture_label.setAlignment(Qt.AlignCenter)
        picture_label.setPixmap(pixmap)
        widget.addWidget(picture_label, 1, 1)
