from datetime import date
from time import asctime


def get_round_name():
    """ Fonction qui enregistre le numéro du round """
    name_input = input("Enter the round number : ")
    name = f"Round {name_input}"
    while name_input.isdigit() == False:
        name_input = input("Enter the round number : ")
        name = f"Round {name_input}"
    return name


def get_round_date():
    """ Fonction qui enregistre la date """
    round_date = date.today()
    return round_date.strftime("%d/%m/%Y")


def get_round_starttime():
    """ Fonction qui enregistre l'heure """
    starttime = asctime()
    return starttime


def get_round_endtime():
    """ Fonction qui enregistre l'heure """
    endtime = asctime()
    return endtime


def enter_score(match):
    """ Fonction qui enregistre le score d'un match """
    score = input(
        f"Enter score ({match.player1.name} WON : enter 1 | {match.player2.name} WON : enter 2 | DRAW : enter 3) : "
    )
    return score


def print_match_result(match):
    """ Fonction qui imprime les résultats d'un match """
    print(
        f"{match.player1.name} : {match.score1}",
        f"\n{match.player2.name} : {match.score2}",
    )
