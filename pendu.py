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
    return data[randint(0, len(data)-1)]


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
        list_word_to_guess = list(word_to_guess)
        list_hidden_word = hidden_word.split(" ")

        if letter not in list_hidden_word:
            for index, value in enumerate(list_word_to_guess):
                if value == letter:
                    list_hidden_word[index] = letter

            hidden_word = " ".join(list_hidden_word)
            if ERROR > 1:
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
            return
        if "_" not in hidden_word:
            print("\n---- Victoire du joueur français ----")
            return


if __name__ == "__main__":
    main()
