from login import *

difficulty_level = "Niveau 1"
word = ""
ihm = None
duo_mode = False


def set_duo_mode():
    global duo_mode
    duo_mode = False


def level_button_connect(button):
    """
    Function that permit to set the difficulty level when a button is click
    :param button: button click
    """
    global difficulty_level
    difficulty_level = button.text()


def choose_word():
    """
    Function which choose the word to guess
    """
    global word
    words_list = difficulty_analysis(WORDFILE, difficulty_level)
    word = choice(words_list)
    # print(word)


def solo_button_click(window):
    """
    Function which indicate what to do when the solo connect button is pressed
    :param window: the window to hide
    """
    global ihm
    choose_word()
    plate = display(word)
    errors = 0
    ihm = UserInterface(word, plate, errors)
    user = Login(ihm)
    user.layout()
    window.hide()


def duo_button_click(input, window):
    """
    Function which indicate what to do when the duo connect button is pressed
    :param window: the window to hide
    """
    global word, duo_mode, ihm
    if isinstance(input.text(), str):
        if input.text() != "":
            word = input.text()
        else:
            choose_word()
    else:
        duo_button_click(input, window)
    plate = display(word)
    errors = 0
    ihm = UserInterface(word, plate, errors)
    ihm.layout()
    duo_mode = True
    window.hide()


class Start:
    """
    Class that manages the starting layout
    """
    def __init__(self):
        self.window = None

    def start_layout(self):
        self.window = QTabWidget()
        self.window.setWindowTitle("Démarrage")
        self.window.resize(450, 200)
        self.window.setStyleSheet("background : #D2E1E1")

        ############### TAB POUR JOUER TOUT SEUL ##################

        solo_tab = QWidget()
        solo_layout = QFormLayout()
        solo_label1 = QLabel("Choisir le niveau : ")
        solo_button_start = QPushButton("Jouer tout seul")
        space_label = QLabel("\n")

        level_box = QHBoxLayout()
        level_box.setAlignment(Qt.AlignCenter)

        level1_button = QRadioButton("Niveau 1")
        level1_button.setChecked(True)
        level2_button = QRadioButton("Niveau 2")
        level3_button = QRadioButton("Niveau 3")

        level_box.addWidget(level1_button)
        level_box.addWidget(level2_button)
        level_box.addWidget(level3_button)

        level1_button.clicked.connect(lambda: level_button_connect(level1_button))
        level2_button.clicked.connect(lambda: level_button_connect(level2_button))
        level3_button.clicked.connect(lambda: level_button_connect(level3_button))

        solo_button_start.clicked.connect(lambda: solo_button_click(self.window))
        solo_layout.addRow(solo_label1)
        solo_layout.addRow(space_label)
        solo_layout.addRow(level_box)
        solo_layout.addRow(space_label)
        solo_layout.addRow(solo_button_start)

        solo_tab.setLayout(solo_layout)

        ############### TAB POUR JOUER A DEUX ##################

        duo_tab = QWidget()
        duo_layout = QFormLayout()
        duo_input = QLineEdit()
        duo_input.setEchoMode(QLineEdit.Password)
        duo_label1 = QLabel("Mot à faire deviner : ")
        duo_button_start = QPushButton("Jouer à deux")
        space_label1 = QLabel("\n")

        duo_button_start.clicked.connect(lambda: duo_button_click(duo_input, self.window))
        duo_layout.addRow(space_label1)
        duo_layout.addRow(duo_label1, duo_input)
        duo_layout.addRow(space_label1)
        duo_layout.addRow(duo_button_start)

        duo_tab.setLayout(duo_layout)

        self.window.addTab(solo_tab, "Jouer seul")
        self.window.addTab(duo_tab, "Jouer à deux")
        self.window.show()
