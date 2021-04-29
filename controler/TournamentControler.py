from view.player import *
from view.round import *
from view.tournament import *
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament


class TournamentControler:
    def __init__(self, tournament):

        self.tournament_progress = tournament

        """for i in range(2):
        nom, elo = v.get_player_info()
        player = Player(nom, elo)
        self.tournament.add_player(player)"""

    def print_all_players(self):
        print(self.tournament_progress.players)

    def run_first_round(self):
        # algorithme pour créer le premier round
        self.tournament_progress.players.sort(key=lambda x: x.elo)
        round_name = "Round 1"  # get_round_name()
        round_date = get_round_date()
        round_starttime = get_round_starttime()
        round1 = Round(round_name, round_date, round_starttime)

        for i in range(4):
            round1.add_match(
                self.tournament_progress.players[i],
                self.tournament_progress.players[4 + i],
            )

        print(round1.matchs)

        self.tournament_progress.add_round(round1)

        # la liste est un Nonetype object --> WHY ?

        print(self.tournament_progress.rounds)

        for match in self.tournament_progress.rounds[0].matchs:
            match.score_player1, match.score_player2 = self.handle_score()
            match.print_match_result(match)

    def handle_score(self):
        score = enter_score()
        while score != "1" and score != "2" and score != "3":
            score = enter_score()

        if score == "1":
            return 1, 0
        elif score == "2":
            return 0, 1
        elif score == "3":
            return 0.5, 0.5

    def run_round(self):
        self.players.sort(key=lambda x: x.elo)
        self.players.sort(key=lambda x: x.score, reverse=True)
        round_name = get_round_name()

        round2 = Round(round_name)
        self.tournament.add_round(round2)
        for i in range(4):
            round2.add_match(self.players[i], self.players[i + 1])

            for match in self.rounds[0].matchs:
                match.score_player1, match.score_player2 = self.handle_score()
                print_match_result(match)

    # trier par nombre de points
    # jumeler joueur 1 avec joueur 2, joueur 3 avec joueur 4 etc (assert qu'ils ont pas joué ensemble)
    # répéter jusqu'à la fin du tournoi

    # joueurs
    # classement

    # def algorithme génération de pairs


# tournamentControler.print_all_players(liste_players)