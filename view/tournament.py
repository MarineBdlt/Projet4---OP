from model.tournament import *
from datetime import date, time
import re

liste_players = [
    Player("Ranga", "Gonnage", "20/07/1980", "H", 200),
    Player("Marine", "Bap", "18/06/1993", "F", 50),
    Player("Monique", "Deletang", "29/10/1933", "F", 75),
    Player("Agnes", "Deletang", "25/06/1963", "F", 80),
    Player("Pascal", "Bap", "12/06/1962", "H", 150),
    Player("Lyam", "Ovitch", "15/08/2000", "H", 160),
    Player("Jeanne", "Jeannot", "14/09/1990", "F", 102),
    Player("Fraise", "Desbois", "17/12/1999", "F", 80),
]


def get_tournament_name():
    """ Fonction qui enregistre et renvoie le nom du tournoi """
    confirm = ""
    while confirm.lower() != "y":
        name = input("Enter the tournament name : ")
        r = re.match("^.*[A-Za-a].*", name)  # changer en isalpha
        if r:
            print(f"The tournament name is : {name.capitalize()}")
            confirm = input("Do you confirm ? (Y/N) : ")
            if confirm.lower() == "y":
                return name.capitalize()
            else:
                print("Please write it again.")
        else:
            print("The name doesn't contains letters. Please write it again.")


def get_tournament_place():
    """ Fonction qui enregistre et renvoie le lieu du tournoi """
    place = input("Enter the tournament place : ")  # vérification ?
    return place


def get_tournament_date():
    """ Fonction qui enregistre la date """
    tournament_date = date.today()
    print(tournament_date)


def get_tournament_players():
    """ Fonction qui enregistre tous les joueurs """
    # changer la fonction pour rentrer les joueurs un par un
    # fonction qui appelle chaque get de chaque player ?
    players = liste_players
    return players


def get_tournament_time_control():
    """ Fonction qui enregistre, imprime et renvoie le type de tournoi """
    time_control = ""
    while (
        time_control.lower() != "bullet"
        and time_control.lower() != "splitz"
        and time_control.lower() != "quick"
    ):
        time_control = input("Enter the Time Control (Bullet/Splitz/Quick) : ")
    print(f"The time control is {time_control.capitalize()}.")
    return time_control.capitalize()


def get_tournament_description():
    """ Fonction qui enregistre et renvoie la description du tournoi """
    description = input("Specify others informations about the tournament : ")
    return description


def print_players(liste_players):
    """ Fonction qui imprime les joueurs et leurs attributs """
    for player in liste_players:
        print(f"Name : {player.name}")
        print(f"Surname : {player.surname}")
        print(f"Birthday : {player.birthday}")
        print(f"Sexe : {player.sexe}")
        print(f"Elo : {player.elo}")
        print(f"Score : {player.score}")


def print_players_scores(liste_players):
    """ Fonction qui imprime les résultats"""
    print(f"Results of the tournament : \n")

    dict_score = {}
    for player in liste_players:
        dict_score[player.name] = player.score
        print(f"{player.name} {player.surname} : {player.score} points.")

    best_score = max(dict_score.values())
    best_players = []
    for player in liste_players:
        if player.score == best_score:
            best_players.append(player.name)
    winners = ", ".join(best_players)

    print("\n\n")
    print(f"The winner(s) of the tournament is/are : {winners} ! Congrats !\n")
