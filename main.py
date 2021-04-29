from controler.TournamentControler import *


if __name__ == "__main__":
    tournament = Tournament(
        "nom", "paris", "date", 4, liste_players, "timecontrol", "description"
    )  # (get_tournament_name(), get_tournament_place(), get_tournament_date(), 4, liste_players, get_tournament_time_control(), get_tournament_description())

    lancement = TournamentControler(tournament)
    lancement.run_first_round()