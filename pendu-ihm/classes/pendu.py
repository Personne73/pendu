from PyQt5.QtGui import *
from string import ascii_lowercase, ascii_uppercase
from bouton import disable_buttons
from timer import start_time

FRENCH = [8.173, 0.901, 3.345, 3.669, 16.734, 1.066, 0.866, 0.737, 7.579, 0.613, 0.049, 5.456, 2.968, 7.095, 5.819,
          2.521, 1.362, 6.693, 7.948, 7.244, 6.429, 1.838, 0.074, 0.427, 0.128, 0.326]

WORDFILE = "../data/mots.txt"

STRING_ACCENTS = 'áàâãäçèéêëìíîïñòóôõöšùúûüýÿž'
LISTE_ACCENTS = list(STRING_ACCENTS)
time2 = 0


def dico(liste):
    """
    Function which do a dictionary associating letter of alphabets to its frequency
    :param liste: a list
    :return: a dico
    """
    d = dict()
    for index, letter in enumerate(ascii_lowercase):
        d[letter] = liste[index]
    return d


def read_file(filename):
    """
    Function that read the specify file and sort it
    :param filename: the file to read
    :return: a list of the words in the file sorted
    """
    words_to_ban = []
    list_to_analyze = []
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
    for word in words:
        if 4 > len(word) or 15 < len(word):
            words_to_ban.append(word)
        for char in word:
            if char in LISTE_ACCENTS or char in ascii_uppercase:
                words_to_ban.append(word.replace(' ', ''))

    set_words = set(words)
    set_words_to_ban = set(words_to_ban)
    words_set = set_words - set_words_to_ban

    for word in list(words_set):
        list_to_analyze.append(word.lower())
    return list_to_analyze


def display(word):
    """
    Function that create a plate of the word to guess
    :param word: word to create a plate
    :return: the plate (mask word)
    """
    plate = "_ " * len(word)
    if "-" in word:
        s = list(word).index("-")
        plate = " ".join(["_" for i in range(s)]) + " - " + " ".join(["_" for i in range(s + 1, len(word))])
    return plate


def change_display(plate, word, player_letter):
    """
    Function which change the display of the plate when a good letter is in the word
    :param plate: the current plate
    :param word: the word to guess
    :param player_letter: the letter of the player
    :return: a modified board
    """
    for index, letter in enumerate(word):
        if letter == player_letter:
            plate = plate[:index * 2] + letter + plate[index * 2 + 1:]
    return plate


def win_label(label_word, input, buttons_list, word, disable_input, button_state, score_button, def_word_button, replay_button):
    """
    Function that change the label by the win text
    :param label_word: the label to change
    :param input: the user input area
    :param buttons_list: the list of buttons
    :param word: the word to guess
    :param disable_input:a function
    :param button_state: a function
    :param score_button: a function
    """
    global time2
    from login import user_pseudo
    label_word.setFont(QFont("Times", 40))
    label_word.setText(f"\n---- Victoire de {user_pseudo} ----\n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)
    button_state(def_word_button, True)
    button_state(replay_button, True)
    from start import duo_mode
    if not duo_mode:
        button_state(score_button, True)
    time2 = start_time()


def lose_label(label_word, input, buttons_list, word, disable_input, button_state, score_button, def_word_button, replay_button):
    """
    Function that change the label by the lose text
    :param label_word: the label to change
    :param input: the player input area
    :param buttons_list: the list of buttons
    :param word: the word to guess
    :param disable_input:a function
    :param button_state: a function
    :param score_button: a function
    """
    global time2
    label_word.setFont(QFont("Times", 40))
    label_word.setText("\n---- GAME OVER ---- \n"
                       f"Le bon mot était : {word}")
    disable_buttons(buttons_list)
    disable_input(input)
    button_state(def_word_button, True)
    button_state(replay_button, True)
    from start import duo_mode
    if not duo_mode:
        button_state(score_button, True)
    time2 = start_time()


def difficulty_analysis(filename, difficulty: str):
    """
    Function which return a list of word depending on the difficulty choose by the player
    :param filename: the file to read
    :param difficulty: the difficulty chosen
    :return: a list of word depending on the difficulty
    """
    dictionary = dico(FRENCH)
    sort_dictionary = dict()
    easy_list = []
    medium_list = []
    hard_list = []
    max = 0

    for word in read_file(filename):
        total = 0
        for char in word:
            total += dictionary.get(char, 0)
        total /= len(word)

        if total > max:
            max = total

        sort_dictionary[word] = round(total)
        if sort_dictionary[word] > 8:
            easy_list.append(word)
        elif 8 > sort_dictionary[word] > 6:
            medium_list.append(word)
        elif 6 > sort_dictionary[word] > 0:
            hard_list.append(word)

    if difficulty == "Niveau 1":
        return easy_list
    elif difficulty == "Niveau 2":
        return medium_list
    elif difficulty == "Niveau 3":
        return hard_list
