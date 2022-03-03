from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def shadow(widget, color=None, radius=10):
    """
    Function to add some shadow to the buttons
    :param widget: the wiget where we will set the effets
    :param color: the color of the shadow
    :param radius: the number use for set the blur
    """
    shade = QGraphicsDropShadowEffect()

    # réglage du flou
    shade.setBlurRadius(radius)
    if color is not None:
        shade.setColor(QColor(color))

    # ajout de l'ombre au widget
    widget.setGraphicsEffect(shade)


def button_click(button, label_word, top_grid_layout, game, input, word, score_button, def_word_button, replay_button, ihm):
    """
    Function to define what to do when a button is pressed
    :param button: a button
    :param label_word: the label where is the word to guess
    :param top_grid_layout: a layout
    :param game: a function which manages the hangman
    :param input: the area where the user can enter a word
    :param word: the word to guess
    :param score_button: the score button
    """
    button.setEnabled(False)
    game(button, label_word, top_grid_layout, input, word, score_button, def_word_button, replay_button, ihm)
    if button.text() in word:
        button.setStyleSheet("background-color : #7CF96F")
    else:
        button.setStyleSheet("background-color : #FB5952")


def disable_buttons(buttons_list):
    """
    Function which disable all the buttons of the list
    :param buttons_list: list of buttons
    """
    for button in buttons_list:
        button.setEnabled(False)


def reset_buttons(buttons_list):
    for button in buttons_list:
        button.close()


def buttons_position(bottom_grid_layout, buttons_list):
    bottom_grid_layout.addWidget(buttons_list[0], 1, 1)
    bottom_grid_layout.addWidget(buttons_list[25], 1, 2)
    bottom_grid_layout.addWidget(buttons_list[4], 1, 3)
    bottom_grid_layout.addWidget(buttons_list[17], 1, 4)
    bottom_grid_layout.addWidget(buttons_list[19], 1, 5)
    bottom_grid_layout.addWidget(buttons_list[24], 1, 6)
    bottom_grid_layout.addWidget(buttons_list[20], 1, 7)
    bottom_grid_layout.addWidget(buttons_list[8], 1, 8)
    bottom_grid_layout.addWidget(buttons_list[14], 1, 9)
    bottom_grid_layout.addWidget(buttons_list[15], 1, 10)

    bottom_grid_layout.addWidget(buttons_list[16], 2, 1)
    bottom_grid_layout.addWidget(buttons_list[18], 2, 2)
    bottom_grid_layout.addWidget(buttons_list[3], 2, 3)
    bottom_grid_layout.addWidget(buttons_list[5], 2, 4)
    bottom_grid_layout.addWidget(buttons_list[6], 2, 5)
    bottom_grid_layout.addWidget(buttons_list[7], 2, 6)
    bottom_grid_layout.addWidget(buttons_list[9], 2, 7)
    bottom_grid_layout.addWidget(buttons_list[10], 2, 8)
    bottom_grid_layout.addWidget(buttons_list[11], 2, 9)
    bottom_grid_layout.addWidget(buttons_list[12], 2, 10)

    bottom_grid_layout.addWidget(buttons_list[22], 3, 3)
    bottom_grid_layout.addWidget(buttons_list[23], 3, 4)
    bottom_grid_layout.addWidget(buttons_list[2], 3, 5)
    bottom_grid_layout.addWidget(buttons_list[21], 3, 6)
    bottom_grid_layout.addWidget(buttons_list[1], 3, 7)
    bottom_grid_layout.addWidget(buttons_list[13], 3, 8)


class Button(QPushButton):
    """
    Class for create the alphabet buttons and which connects them to the right function
    """
    def __init__(self, label, label_word, top_grid_layout, game, input, word, score_button, def_word_button, replay_button, ihm):
        super().__init__(label)
        self.clicked.connect(lambda: button_click(self, label_word, top_grid_layout, game, input, word, score_button, def_word_button, replay_button, ihm))
        shadow(self)
