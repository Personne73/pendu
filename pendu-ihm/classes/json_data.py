import json

file_json = "../data/database.json"
data = {}


def read_json_file():
    """
    Function which permit to load the json file
    """
    global data
    with open(file_json, "r", encoding="utf8") as file:
        data = json.load(file)


def load_file(username):
    """
    Function which permit to add to the json file a username
    :param username: the username to add to the json file
    """
    with open(file_json, "w", encoding="utf8") as file:
        from start import ihm, difficulty_level, word
        from score import get_score
        data[username] = get_score(difficulty_level, word, ihm)
        json.dump(data, file, indent=4)
