import datetime
from tinydb import where, Query
from model.player import Player


def get_player_name():
    """ Fonction qui enregistre et retourne le prénom d'un joueur """
    player_name = input("Enter player's name : ")
    while not player_name.isalpha():
        player_name = input("Enter player's name : ")
    return player_name.capitalize()


def get_player_surname():
    """ Fonction qui enregistre et retourne le nom d'un joueur """
    player_surname = input("Enter player's surname : ")
    while not player_surname.isalpha():
        player_surname = input("Enter player's surname : ")
    return player_surname.capitalize()


def get_player_birthday():
    """ Fonction qui renregistre et retourne la date de naissance d'un joueur """
    player_birthday = ""
    while player_birthday == "":
        try:
            player_birthday = input("Enter player's birthday (dd-mm-yyyy) : ")
            datetime.datetime.strptime(player_birthday, "%d-%m-%Y")
            return player_birthday
        except ValueError:
            print("Incorrect data format, should be DD-MM-YYYY")
            player_birthday = ""


def get_player_sexe():
    """ Fonction qui enregistre et retourne le sexe d'un joueur """
    player_sexe = input("Woman (W) or Man (M) ? : ")
    while player_sexe.upper() != "W" and player_sexe.upper() != "M":
        player_sexe = input("Woman (W) or Man (M) ? : ")
    return player_sexe


def get_player_elo():
    """ Fonction qui enregistre et retourne l'elo d'un joueur """
    player_elo = ""
    while not player_elo.isdigit():
        player_elo = input("Enter player's rank (ELO) : ")
    return player_elo


def change_elo_actor(actors_db):
    """Fonction qui met à jour le ELO d'un joueur dans le actors.json"""
    name = get_player_name()
    elo = get_player_elo()
    actor_table = actors_db.table(f"{name}")
    actor_data = actor_table.search(where("Name") == name)
    actor = actor_data[0]

    player = Player(
        actor["Name"], actor["Surname"], actor["Birthday"], actor["Sexe"], elo
    )
    serialized_player = player.serialize()
    User = Query()
    actor_table.truncate()
    actor_table.upsert(serialized_player, User.name == name)
    pass
