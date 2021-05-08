import datetime


def get_player_name():
    """ Fonction qui enregistre et retourne le prénom d'un joueur """
    player_name = input("Enter player's name : ")
    while player_name.isalpha() == False:
        player_name = input("Enter player's name : ")
    return player_name.capitalize()


def get_player_surname():
    """ Fonction qui enregistre et retourne le nom d'un joueur """
    player_surname = input("Enter player's surname : ")
    while player_surname.isalpha() == False:
        player_surname = input("Enter player's surname : ")
    return player_surname.capitalize()


def get_player_birthday():
    """ Fonction qui renregistre et retourne la date de naissance d'un joueur """
    player_birthday = ""
    while player_birthday == "":
        try:
            player_birthday = input("Enter player's birthday (jj-mm-aaaa) : ")
            datetime.datetime.strptime(player_birthday, "%d-%m-%Y")
            return player_birthday
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
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
    while player_elo.isdigit() == False:
        player_elo = input("Enter player's rank (ELO) : ")
    return player_elo
