from userinterface import *
from json_data import *
from random import *

user_pseudo = ""
adjectives_list = ["Happy", "Sad", "Depressed", "Calm", "Playful", "Lucky", "Short", "Tall", "Big", "Little", "Good",
                   "Great", "Bad", "Best", "New", "Young", "Old", "Same", "Full", "Fresh", "Pink", "Orange", "Yellow",
                   "Pink", "Brown", "Gold", "Silver", "Sarcastic", "Bold", "Smart", "Involved", "Political", "Dynamic",
                   "Energetic", "Unknown", "Random"]
names_list = ["Cat", "Dog", "Keyboard", "Mouse", "Computer", "Car", "Squirrel", "Phone", "Octane", "Player", "Gamer",
              "Tree", "Eagle", "Banana", "Orange", "Apple", "Pineapple", "Ball", "Book", "Mask", "Calendar"]


def connect_button_click(ihm, window, username):
    """
    Function which control the click of the connect button
    :param ihm: a UserInterface object
    :param window: the window to hide
    :param username: the username of the player
    """
    global user_pseudo
    ihm.layout()
    window.hide()
    if username == "":
        user_pseudo = choice(adjectives_list) + choice(names_list)
        username = user_pseudo
    else:
        user_pseudo = username
    read_json_file()
    load_file(username)


class ConnectButton(QPushButton):
    """
    Class for create the connect button and which connects it to the good function
    """

    def __init__(self, label, ihm, window, input_user):
        super().__init__(label)
        self.clicked.connect(lambda: connect_button_click(ihm, window, input_user.text()))


class Login:
    """
    Class that manages the login layout
    """

    def __init__(self, ihm):
        self.window = None
        self.ihm = ihm

    def layout(self):
        """
        Function that create the login window
        """
        self.window = QWidget()
        self.window.setWindowTitle("Login")
        self.window.resize(450, 120)
        self.window.setStyleSheet("background : #D2E1E1")

        label_text = QLabel(self.window)
        label_text.setText("Entrez un pseudo puis connectez vous")
        label_text.setAlignment(Qt.AlignCenter)
        label_text.setFont(QFont("Times", 10))

        label_user = QLabel("Pseudo")
        label_user.setFont(QFont("Times", 9))
        input_user = QLineEdit()
        input_user.setFont(QFont("Times", 10))
        label_space = QLabel()

        login_layout = QFormLayout()

        connect_button = ConnectButton("Se connecter", self.ihm, self.window, input_user)

        login_layout.addRow(label_text)
        login_layout.addRow(label_space)
        login_layout.addRow(label_user, input_user)
        login_layout.addWidget(connect_button)

        self.window.setLayout(login_layout)
        self.window.show()
