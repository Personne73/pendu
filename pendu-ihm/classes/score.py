from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from json_data import read_json_file, load_file
from timer import get_time

database_dict = {}
current_player = ""


def get_score(difficulty_level: str, word: str, ihm):
    """
    Function to calculate the score of the current player
    :param difficulty_level: the difficulty
    :param word: the word to guess
    :param ihm: the hangman interface
    :return: the score
    """
    score = 0

    time1 = ihm.time
    from pendu import time2
    final_time = get_time(time1, time2)

    if final_time > 0:
        if difficulty_level == "Niveau 1":
            score = 100 + len(word) * 10 - ihm.errors*10 - final_time
        elif difficulty_level == "Niveau 2":
            score = 200 + len(word) * 10 - ihm.errors*10 - final_time
        elif difficulty_level == "Niveau 3":
            score = 300 + len(word) * 10 - ihm.errors*10 - final_time

        if ihm.errors == 0:
            score += 500
        elif ihm.errors > 11:
            score = 0

    return round(score)


def get_users():
    """
    Function to get the current user and a dict of all users
    """
    global database_dict, current_player
    read_json_file()
    from json_data import data
    database_dict = data
    from login import user_pseudo
    current_player = user_pseudo


class Score(QScrollArea):
    """
    CLass that manages the scoreboard layout
    """
    def __init__(self):
        super(Score, self).__init__()
        self.window = None

    def score_layout(self):
        """
        Function that shows the scoreboard at the end of the game
        """
        self.window = QWidget()
        self.resize(600, 600)
        self.window.setWindowTitle("Tableau des scores")
        self.window.setStyleSheet("background-color : #D2E1E1")

        form_layout = QFormLayout()
        label_global_scores = QLabel("Scores globaux")
        label_global_scores.setAlignment(Qt.AlignCenter)
        label_global_scores.setFont(QFont('Times', 50))
        form_layout.addRow(label_global_scores)
        label_space = QLabel("\n")

        grid_layout = QGridLayout()
        label_username = QLabel("Pseudo")
        label_username.setFont(QFont("Times", 25))
        label_username.setAlignment(Qt.AlignCenter)
        label_score = QLabel("Score")
        label_score.setFont(QFont("Times", 25))
        label_score.setAlignment(Qt.AlignCenter)

        get_users()
        load_file(current_player)

        label_pseudos_tab = QWidget()
        label_pseudos_layout = QFormLayout()
        label_scores_tab = QWidget()
        label_scores_layout = QFormLayout()

        label_list = []
        label_scores_list = []

        # allows sorting in descending order by the score the dict
        e = sorted(database_dict.items(), key=lambda x: x[1], reverse=True)
        for username, score in dict(e).items():
            label_scores_list.append(QLabel(str(score)))
            label_list.append(QLabel(username))

        for i in range(len(label_list)):
            if current_player == label_list[i].text():
                label_list[i].setStyleSheet("color: red")
                label_scores_list[i].setStyleSheet("color: red")

            # label test
            label_list[i].setFont(QFont("Times", 12))
            label_list[i].setAlignment(Qt.AlignCenter)
            label_scores_list[i].setFont(QFont("Times", 12))
            label_scores_list[i].setAlignment(Qt.AlignCenter)

            label_scores_layout.addRow(label_scores_list[i])
            label_pseudos_layout.addRow(label_list[i])

        label_scores_tab.setLayout(label_scores_layout)
        label_pseudos_tab.setLayout(label_pseudos_layout)

        grid_layout.addWidget(label_username, 1, 1)
        grid_layout.addWidget(label_pseudos_tab, 2, 1)
        grid_layout.addWidget(label_score, 1, 2)
        grid_layout.addWidget(label_scores_tab, 2, 2)

        form_layout.addRow(label_space)
        form_layout.addRow(grid_layout)

        self.window.setLayout(form_layout)

        self.setWidget(self.window)
        self.setWidgetResizable(True)
        self.show()
