from random import *

WORDFILE = "../Pendu/mots.txt"
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

ERROR = 0
WORD = "banane pomme mandarine orange".split(" ")


def read_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.read().split()


def random_word():
    return WORD[randint(0, len(WORD)-1)]


def affichage(taille: int):
    str_affiche = ""

    for i in range(taille):
        str_affiche += "_ "

    return str_affiche


def main():
    print(read_file(WORDFILE))
    # word = random_word()
    # word_suspens = affichage(len(word))
    # print(HANGMANPICS[6])
    # print(word, word_suspens)
    # s = input("Entrez une lettre ?")


if __name__ == "__main__":
    main()
