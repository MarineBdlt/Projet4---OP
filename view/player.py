import datetime


def get_player_name():
    player_name = input("Enter player's name : ")
    while player_name.isalpha() == False:
        player_name = input("Enter player's name : ")
    return player_name.capitalize()


def get_player_surname():
    player_surname = input("Enter player's surname : ")
    while player_surname.isalpha() == False:
        player_surname = input("Enter player's surname : ")
    return player_surname.capitalize()


def get_player_birthday():
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
    player_sexe = input("Woman (W) or Man (M) ? : ")
    while player_sexe.upper() != "W" and player_sexe.upper() != "M":
        player_sexe = input("Woman (W) or Man (M) ? : ")
    return player_sexe


def get_player_elo():
    player_elo = ""
    while player_elo.isdigit() == False:
        player_elo = input("Enter player's Rank (elo) : ")
    return player_elo


def print_players(liste_players):
    for player in liste_players:
        print(f"name : {player.name}")
        print(f"surname : {player.surname}")
        print(f"birthday : {player.birthday}")
        print(f"sexe : {player.sexe}")
        print(f"elo : {player.elo}")