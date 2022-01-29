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
LETTERUSED = []


def read_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.read().split()


def random_word(data):
    word = data[randint(0, len(data)-1)]
    if len(word) < 4:
        random_word(data)
    return word
    # return data[randint(0, len(data)-1)]


def affichage(taille: int):
    return "_ " * taille


def ask_letter():
    return input("\nEntrez une lettre de l'alphabet : ").lower()


def error_state():
    print(HANGMANPICS[ERROR])


def game(letter, word_to_guess, hidden_word):
    global ERROR
    global LETTERUSED

    if letter not in word_to_guess:
        print("Vous venez de faire une erreur !\n")
        error_state()
        ERROR += 1
        LETTERUSED.append(letter)
    else:
        if letter not in hidden_word:
            for index, value in enumerate(word_to_guess):
                if value == letter:
                    hidden_word = hidden_word[:index * 2] + letter + hidden_word[index * 2 + 1:]

            if ERROR > 0:
                error_state()
        else:
            print("Vous avez déjà entrez cette lettre, choisissez en une autre !\n")

    print("Lettre déjà utilisée : ", set(LETTERUSED))
    print(hidden_word, "\n")
    return hidden_word


def main():
    word_data = read_file(WORDFILE)
    word = random_word(word_data)
    hidden_word = affichage(len(word))
    print(hidden_word)
    while 1:
        hidden_word = game(ask_letter(), word, hidden_word)
        if ERROR == len(HANGMANPICS):
            print("\n---- GAME OVER ----")
            print(f"Le bon mot était : {word}")
            input()
            return
        if "_" not in hidden_word:
            print("\n---- Victoire du joueur français ----")
            input()
            return


if __name__ == "__main__":
    main()
