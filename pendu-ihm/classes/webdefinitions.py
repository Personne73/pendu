from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
import requests as req


def get_definition_string(word):
    try:
        resp = req.get(f"https://www.cnrtl.fr/definition/{word}")
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup.find_all('span', class_="tlf_cdefinition")[0].text
    except:
        try:
            resp = req.get(f"https://www.larousse.fr/dictionnaires/francais/{word}")
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup.find_all('p', class_="def")[0].text
        except:
            return "Veuillez vous connecter à internet."


def button_clicked(word):
    """
     Function that allows the creation of the window
     :param word: the word that the player needs to guess
     """
    import webbrowser
    webbrowser.open(f"https://www.larousse.fr/dictionnaires/francais/{word}")


class WebDef:
    """
    Class for create a window with the definition of the word chosen
    """

    def __init__(self):
        self.window = None
        self.box = None

    def definition_word(self, word: str):
        """
        Function that allows the creation of the window
        :param word: the word that the player needs to guess
        """
        self.box = QMessageBox()
        # self.box.resize(1000, 1000)
        self.box.setWindowTitle(f"Définiton du mot {word}")
        self.box.setIcon(QMessageBox.Question)
        self.box.setText(f"La définition du mot '{word}' est : ")
        self.box.setInformativeText(get_definition_string(word))
        self.box.addButton(QPushButton("Ok"), QMessageBox.YesRole)
        more = QPushButton("En savoir plus")
        self.box.addButton(more, QMessageBox.YesRole)
        more.clicked.connect(lambda: button_clicked(word))
        self.box.show()

# soup.find_all('p', class_="def")[0].text
