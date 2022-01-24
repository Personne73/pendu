from random import *

WORDFILE = "../Pendu/mots.txt"
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
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


def random_word(data):
    return data[randint(0, len(data)-1)]


def affichage(taille: int):
    return "_ " * taille


def ask_letter():
    return input("Entrez une lettre de l'alphabet ! ").lower()


def error_state():
    print(HANGMANPICS[ERROR])


def game(letter, word_to_guess):
    global ERROR
    if letter not in word_to_guess:
        print("Vous venez de faire une erreur !")
        error_state()
        ERROR += 1
    else:
        list_word_to_guess = list(word_to_guess)
        for index, value in enumerate(list_word_to_guess):
            if value != letter:
                list_word_to_guess[index] = "_"
        hidden_word = " ".join(list_word_to_guess)
        print(hidden_word)
        if ERROR > 1:
            error_state()


def main():
    word_data = read_file(WORDFILE)
    word = random_word(word_data)
    hidden_word = affichage(len(word))
    print(word, hidden_word)
    while 1:
        game(ask_letter(), word)
        if ERROR == len(HANGMANPICS):
            print("---- GAME OVER ----")
            print(f"Le bon mot était : {word}")
            return


if __name__ == "__main__":
    main()
