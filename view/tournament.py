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
    place = input("Enter the tournament place : ")
    return place


def get_tournament_date():
    tournament_date = date.today()
    print(tournament_date)


def get_tournament_players():
    # changer la fonction pour rentrer les joueurs un par un
    # fonction qui appelle chaque get de chaque player ?
    players = liste_players
    return players


def get_tournament_time_control():
    time_control = ""
    while (
        time_control.lower() != "bullet"
        and time_control.lower() != "splitz"
        and time_control.lower() != "quick"
    ):
        time_control = input("Enter the Time Control (Bullet/Splitz/Quick) : ")
    print(f"The time control is {time_control.capitalize()}.")


def get_tournament_description():
    description = input("Specify others informations about the tournament : ")
    return description


def print_all_players(players):
    for player in players:
        player.print_player()
        print("--------")
