from view.player import *
from view.round import *
from view.tournament import *
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament

# tempérer le temps
# ajouter les joueurs
# checker TinyDB


class TournamentControler:
    """ Classe qui lance et fait fonctionner le tournoi """

    def __init__(self, tournament):

        self.tournament_progress = tournament

        """for i in rang(2):
        nom, elo = v.get_player_info()
        player = Player(nom, elo)
        self.tournament.add_player(player)"""

    def print_all_players(self):
        """ Fonction qui imprime les joueurs d'un tournoi"""
        print(self.tournament_progress.players)

    def run_first_round(self):
        """ Fonction qui fait tourner le premier round """
        self.tournament_progress.players.sort(key=lambda x: x.elo)
        round_name = "Round 1"
        round_date = get_round_date()
        round_starttime = get_round_starttime()
        round1 = Round(round_name, round_date, round_starttime)
        print(
            f"{self.tournament_progress.name} begins !\n--------------------------------------\n"
        )
        print(f"{round_name} launchment...")

        for i in range(4):

            round1.add_match(
                self.tournament_progress.players[i],
                self.tournament_progress.players[4 + i],
            )

        self.tournament_progress.add_round(round1)

        for match in self.tournament_progress.rounds[0].matchs:  # changer l'indice ?
            print("\n...\n")
            print(
                f"{match.player1.name} and {match.player2.name} play against each other !"
            )

            match.score_player1, match.score_player2 = self.handle_score(match)
            print_match_result(match)

            match.player1.add_score(match.score_player1)
            match.player2.add_score(match.score_player2)

        round1.endtime = get_round_endtime()
        print(f"End of the Round1 at {round1.endtime}.")
        print("\n--------------------------------------\n")

    def handle_score(self, match):
        """ Fonction qui calcule le score d'un match """
        score = enter_score(match)
        while score != "1" and score != "2" and score != "3":
            score = enter_score(match)

        if score == "1":
            return 1, 0
        elif score == "2":
            return 0, 1
        elif score == "3":
            return 0.5, 0.5

    def run_rounds(self):
        """ Fonction qui fait tourner les rounds suivants """

        for i in range(int(self.tournament_progress.number_of_rounds) - 1):
            self.tournament_progress.players.sort(key=lambda x: x.elo)

            self.tournament_progress.players.sort(key=lambda x: x.score, reverse=True)

            round_name = f"Round {i+2}"
            round_date = get_tournament_date()
            round_starttime = get_round_starttime()
            next_round = Round(round_name, round_date, round_starttime)
            self.tournament_progress.add_round(next_round)

            print(f"{round_name} launchment...")

            for i in range(4):
                next_round.add_match(
                    self.tournament_progress.players[i],
                    self.tournament_progress.players[i + 1],
                )

            for match in self.tournament_progress.rounds[0].matchs:  # bon indice ?
                print("\n...\n")
                print(
                    f"{match.player1.name} and {match.player2.name} play against each other !"
                )

                match.score_player1, match.score_player2 = self.handle_score(match)
                print_match_result(match)

                match.player1.add_score(match.score_player1)
                match.player2.add_score(match.score_player2)

            next_round.endtime = get_round_endtime()
            print(f"End of the {round_name} at {next_round.endtime}.")
            print("\n--------------------------------------\n")
            i += 1

        print(
            f"{self.tournament_progress.name} is over !\n--------------------------------------\n"
        )
        print_players_scores(liste_players)


# {match.player1.name}
# trier par nombre de points
# jumeler joueur 1 avec joueur 2, joueur 3 avec joueur 4 etc (assert qu'ils ont pas joué ensemble)
# répéter jusqu'à la fin du tournoi

# joueurs
# classement

# def algorithme génération de pairs


# tournamentControler.print_all_players(liste_players)