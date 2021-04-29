from datetime import date, time


def get_round_name():
    name_input = input("Enter the round number : ")
    name = f"Round {name_input}"
    while name_input.isdigit() == False:
        name_input = input("Enter the round number : ")
        name = f"Round {name_input}"
    return name


def get_round_date():
    round_date = date.today()
    return round_date


def get_round_starttime():
    starttime = time()
    return starttime


def get_round_endtime():
    endtime = time()
    return endtime


def enter_score():
    score = input(
        f"Enter score (1 : {match.player1.name} 1 win / 2 : {match.player2.name} win / 3 : draw) "
    )
    return score
    # tester


def print_match_result(match):
    print(
        f"{match.player1.name} : {match.score_player1}",
        f"\n{match.player2.name} : {match.score_player2}",
    )
