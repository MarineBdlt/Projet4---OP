import view.player as vp
import view.round as vr
import view.tournament as vt
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament

from tinydb import TinyDB, Query, where


# Pour recharger les joueurs sérialisés, tu peux faire ceci :
# serialized_players = players_table.all()
# User = Query()
# db.insert({'name': 'John', 'age': 22})
# db.search(User.name == 'John')


class TournamentControler:
    """ Classe qui lance et fait fonctionner le tournoi """

    def __init__(self, db):
        # instanciée dans la classe création"
        self.tournament_table = db.table("Tournament")

        # sortir de la classe
        # créer une fonction reprendre le dernier tournoi ou en créer un autre

    def new_tournament_created(self, db):

        # instancier le tournoi en dehors de la classe
        tournament_progress = Tournament(
            vt.get_tournament_name(),
            "Paris",
            "12-10-2000",
            4,
            [],
            [],
            [],
            "Quick",
            "None",
        )
        "Dans tournament classe, ne pas avoir besoin de l'instanciation"
        """
            vt.get_tournament_name(),
            vt.get_tournament_place(),
            vt.get_tournament_date(),
            4,
            [],
            vt.get_tournament_time_control(),
            vt.get_tournament_description(),
        )"""

        serialized_tournament = tournament_progress.serialize()
        self.tournament_table.insert(serialized_tournament)
        print(tournament_progress)
        return tournament_progress

    def init_players(self, tournament_progress):
        """ Fonction qui instancie les joueurs du tournoi """
        for i in range(8):
            input(f"\nEnter player{i+1} informations [ENTER]\n")
            name = "Hugo" + str(i)  # vp.get_player_name()
            surname = "Barrier" + str(i)  # vp.get_player_surname()
            birthday = "11-06-1996" + str(i)  # vp.get_player_birthday()
            sexe = "M" + str(i)  # vp.get_player_sexe()
            elo = "elo"  # vp.get_player_elo()
            score = 0
            player = Player(name, surname, birthday, sexe, elo, score)
            tournament_progress.add_player(player)

            serialized_player = player.serialize()
            tournament_progress.serialized_players.append(serialized_player)

        print(tournament_progress.serialized_players)
        tournament_progress.serialized_players = tournament_progress.serialized_players

        tournament_progress.serialized_tournament = tournament_progress.serialize()
        self.tournament_table.insert(tournament_progress.serialized_tournament)
        return tournament_progress

    def print_all_players(self, tournament_progress):
        """ Fonction qui imprime les joueurs d'un tournoi"""
        print(tournament_progress.players)

    def run_first_round(self, tournament_progress):
        """ Fonction qui fait tourner le premier round """
        # instancie le round
        round_name = "Round 1"
        round_date = vr.get_round_date()
        round_starttime = vr.get_round_starttime()
        round1 = Round(round_name, round_date, round_starttime)

        # serialize le round
        serialized_round1 = round1.serialize()
        # self.rounds_table.insert(serialized_round1)

        tournament_progress.serialized_rounds.append(serialized_round1)
        tournament_progress.serialized_rounds = tournament_progress.serialized_rounds

        tournament_progress.serialized_tournament = tournament_progress.serialize()
        self.tournament_table.insert(tournament_progress.serialized_tournament)

        print(
            f"{tournament_progress.name} begins !\n--------------------------------------\n"
        )
        print(f"{round_name} launchment...")

        tournament_progress.players.sort(key=lambda x: x.elo)

        for i in range(4):
            round1.add_match(
                tournament_progress.players[i],
                tournament_progress.players[4 + i],
            )

        print(round1.matchs)
        # ajoute le round au tournoi
        tournament_progress.add_round(round1)

        # instancie les matchs dans la classe Round
        i = 0

        tournament_progress.serialized_players.clear()
        self.tournament_table.truncate()
        for match in tournament_progress.rounds[0].matchs:
            print("\n...\n")
            print(
                f"{match.player1.name} and {match.player2.name} play against each other !"
            )
            # input et print les résultats du match
            match.score1, match.score2 = self.handle_score(match)
            i += 1

            vr.print_match_result(match)

            serialized_match = match.serialize()
            round1.serialized_matchs.append(serialized_match)

            # ajout des scores dans la classe Player() et print dans les players
            match.player1.add_score(match.score1)
            match.player2.add_score(match.score2)
            serialized_player = match.player1.serialize()
            tournament_progress.serialized_players.append(serialized_player)

            self.tournament_table.update_multiple(
                [
                    (
                        {"Score": match.player1.score},
                        where("Name") == match.player1.name,
                    ),
                    (
                        {"Score": match.player2.score},
                        where("Name") == match.player2.name,
                    ),
                ]
            )
        # itérer sur les players? mettre les scores dans tournament

        # ajout des matchs et de end-time
        round1.endtime = vr.get_round_endtime()
        serialized_round1 = {
            "Round end-time": round1.endtime,
            "Round Matchs": round1.serialized_matchs,
        }

        tournament_progress.serialized_tournament = tournament_progress.serialize()
        self.tournament_table.insert(tournament_progress.serialized_tournament)

        print(f"End of the Round1 at {round1.endtime}.")
        print("\n--------------------------------------\n")

        return tournament_progress

    def handle_score(self, match):
        """ Fonction qui calcule le score d'un match """
        score = vr.enter_score(match)
        while score != "1" and score != "2" and score != "3":
            score = vr.enter_score(match)

        if score == "1":
            return 1, 0
        elif score == "2":
            return 0, 1
        elif score == "3":
            return 0.5, 0.5

    def run_rounds(self, tournament_progress):
        """ Fonction qui fait tourner les rounds suivants """

        for i in range(int(tournament_progress.number_of_rounds) - 1):
            tournament_progress.players.sort(key=lambda x: x.elo)

            tournament_progress.players.sort(key=lambda x: x.score, reverse=True)

            round_name = f"Round {i+2}"
            round_date = vr.get_round_date()
            round_starttime = vr.get_round_starttime()
            next_round = Round(round_name, round_date, round_starttime)
            tournament_progress.add_round(next_round)

            # serialize round
            serialized_next_round = next_round.serialize()

            tournament_progress.serialized_rounds.append(serialized_next_round)
            tournament_progress.serialized_rounds = (
                tournament_progress.serialized_rounds
            )

            self.serialized_tournament = tournament_progress.serialize()
            self.tournament_table.insert(self.serialized_tournament)

            print(f"{round_name} launchment...")

            for i in range(4):
                next_round.add_match(
                    tournament_progress.players[i],
                    tournament_progress.players[i + 1],
                )

            tournament_progress.serialized_players.clear()
            self.tournament_table.truncate()
            for match in tournament_progress.rounds[0].matchs:  # bon indice ?
                print("\n...\n")
                print(
                    f"{match.player1.name} and {match.player2.name} play against each other !"
                )

                match.score_player1, match.score_player2 = self.handle_score(match)
                vr.print_match_result(match)

                match.player1.add_score(match.score_player1)
                match.player2.add_score(match.score_player2)
                serialized_player = match.player1.serialize()
                tournament_progress.serialized_players.append(serialized_player)

                serialized_match = match.serialize()
                next_round.serialized_matchs.append(serialized_match)

                self.tournament_table.update_multiple(
                    [
                        (
                            {"Score": match.player1.score},
                            where("Name") == match.player1.name,
                        ),
                        (
                            {"Score": match.player2.score},
                            where("Name") == match.player2.name,
                        ),
                    ]
                )
            # ajouter score dans db après chaque match
            next_round.endtime = vr.get_round_endtime()

            tournament_progress.serialized_tournament = tournament_progress.serialize()
            self.tournament_table.insert(tournament_progress.serialized_tournament)

            print(f"End of the {round_name} at {next_round.endtime}.")
            print("\n--------------------------------------\n")
            i += 1

            return tournament_progress

        print(
            f"{tournament_progress.name} is over !\n--------------------------------------\n"
        )
        vt.print_players_scores(tournament_progress.players)
