import sys
from start import *
import sys


def main():
    """
    The main function of the hangman game
    """
    app = QApplication(sys.argv)
    starter = Start()
    starter.start_layout()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
