from model.tournament import *
from datetime import date, time
import re


def get_tournament_name():
    """ Fonction qui enregistre et renvoie le nom du tournoi """
    confirm = ""
    while confirm.lower() != "y":
        name = input("Enter the tournament name : ")
        r = re.match("^.*[A-Za-a].*", name)
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
    place = input("Enter the tournament place : ")
    while place.isalpha() is False:
        print("The place is not correct, write it again in letters : ")
        place = input("Enter the tournament place : ")
    print(f"The tournament takes place in {place.capitalize()}")
    return place.capitalize()


def get_tournament_date():
    """ Fonction qui enregistre la date """
    tournament_date = date.today()
    return tournament_date


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
