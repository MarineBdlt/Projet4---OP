import view.player as vp
import view.round as vr
import view.tournament as vt
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament

from tinydb import TinyDB, Query, where
from tinydb.operations import delete


class TournamentControler:
    """ Classe qui lance et fait fonctionner le tournoi """

    def __init__(self):
        self.tournament_progress = ""

    def new_tournament_created(self, db):
        self.tournament_progress = Tournament(
            vt.get_tournament_name(),
            vt.get_tournament_place(),
            vt.get_tournament_date(),
            4,
            [],
            [],
            [],
            vt.get_tournament_time_control(),
            vt.get_tournament_description(),
        )

        tournament_table = db.table(f"{self.tournament_progress.name}")

        serialized_tournament = self.tournament_progress.serialize()
        tournament_table.insert(serialized_tournament)

        return tournament_table

    def init_players(self, tournament_table, actors_db):
        """ Fonction qui instancie les joueurs du tournoi """
        for i in range(8):
            input(f"\nEnter player{i+1} informations [ENTER]\n")
            name = vp.get_player_name()
            surname = vp.get_player_surname()
            birthday = vp.get_player_birthday()
            sexe = vp.get_player_sexe()
            elo = vp.get_player_elo()
            score = 0
            player = Player(name, surname, birthday, sexe, elo, score)
            self.tournament_progress.add_player(player)

            serialized_player = player.serialize()
            actor_table = actors_db.table(f"{name}")

            # if actor_table.search(where("Name") == name) = None:
            User = Query()
            actor_table.upsert(serialized_player, User.name == name)

            self.tournament_progress.serialized_players.append(serialized_player)

        self.tournament_progress.serialized_tournament = (
            self.tournament_progress.serialize()
        )

        tournament_table.truncate()
        tournament_table.insert(self.tournament_progress.serialized_tournament)

    def print_all_players(self):
        """ Fonction qui imprime les joueurs d'un tournoi"""
        print(self.tournament_progress.players)

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

    def get_players(self):
        """ Fonction qui tri les players par elo et par score """
        players = []
        for player in self.tournament_progress.players:
            players.append(player)
        players.sort(key=lambda x: x.elo)
        players.sort(key=lambda x: x.score, reverse=True)

        return players

    def make_pairing(self, players, current_round):
        """ Algorithme qui crée les paires de match """
        i = 0
        while len(players) != 0:
            player1 = players[i]
            player1_index = i
            player2 = players[i + 1]
            player2_index = i + 1

            player2_id = player2.surname + player2.elo
            while player2_id in player1.opponents:
                i += 1
                player2 = players[i + 1]
                player2_index = i + 1
                player2_id = player2.surname + player2.elo

            current_round.add_match(player1, player2)

            del players[player2_index]
            del players[player1_index]

            i = 0

    def run_first_round(self, tournament_table, actors_db):
        """ Fonction qui fait tourner le premier round """
        round_name = "Round 1"
        round_date = vr.get_round_date()
        round_starttime = vr.get_round_starttime()
        round1 = Round(round_name, round_date, round_starttime)
        serialized_round1 = round1.serialize()

        self.tournament_progress.serialized_rounds.append(serialized_round1)
        self.tournament_progress.serialized_rounds = (
            self.tournament_progress.serialized_rounds
        )
        vt.print_info(
            f"{self.tournament_progress.name} begins !\n--------------------------------------\n"
        )
        vt.print_info(f"{round_name} launchment...")

        self.tournament_progress.players.sort(key=lambda x: x.elo)
        for i in range(4):
            round1.add_match(
                self.tournament_progress.players[i],
                self.tournament_progress.players[4 + i],
            )
        self.tournament_progress.add_round(round1)

        i = 0
        for match in self.tournament_progress.rounds[0].matchs:
            vt.print_info("\n...\n")
            vt.print_info(
                f"{match.player1.name} and {match.player2.name} play against each other !"
            )
            match.score1, match.score2 = self.handle_score(match)
            i += 1

            vr.print_match_result(match)

            serialized_match = match.serialize()
            round1.serialized_matchs.append(serialized_match)

            match.player1.add_opponent(match.player2)
            match.player2.add_opponent(match.player1)
            match.player1.add_score(match.score1)
            match.player2.add_score(match.score2)

            tournament_table.truncate()
            tournament_table.insert(self.tournament_progress.serialized_tournament)

        round1.endtime = vr.get_round_endtime()
        serialized_round1 = {
            "Round end-time": round1.endtime,
            "Round Matchs": round1.serialized_matchs,
        }
        self.tournament_progress.serialized_tournament = (
            self.tournament_progress.serialize()
        )
        tournament_table.truncate()
        tournament_table.insert(self.tournament_progress.serialized_tournament)

        vt.print_info(f"End of the Round1 at {round1.endtime}.")
        vt.print_info("\n--------------------------------------\n")

    def run_rounds(self, tournament_table, actors_db, next_round_number=2):
        """ Fonction qui fait tourner les rounds suivants """
        for i in range(next_round_number, 5):
            players = self.get_players()
            round_name = f"Round {i}"
            round_date = vr.get_round_date()
            round_starttime = vr.get_round_starttime()
            next_round = Round(round_name, round_date, round_starttime)
            self.tournament_progress.add_round(next_round)

            serialized_next_round = next_round.serialize()

            self.tournament_progress.serialized_rounds.append(serialized_next_round)
            self.tournament_progress.serialized_rounds = (
                self.tournament_progress.serialized_rounds
            )
            self.serialized_tournament = self.tournament_progress.serialize()

            vt.print_info(f"{round_name} launchment...")

            self.make_pairing(players, next_round)
            self.tournament_progress.serialized_players.clear()

            for match in self.tournament_progress.rounds[i - 1].matchs:
                vt.print_info("\n...\n")
                vt.print_info(
                    f"{match.player1.name} and {match.player2.name} play against each other !"
                )

                match.score1, match.score2 = self.handle_score(match)
                vr.print_match_result(match)

                serialized_match = match.serialize()
                next_round.serialized_matchs.append(serialized_match)

                match.player1.add_opponent(match.player2)
                match.player2.add_opponent(match.player1)
                match.player1.add_score(match.score1)
                match.player2.add_score(match.score2)

                serialized_player1 = match.player1.serialize()
                self.tournament_progress.serialized_players.append(serialized_player1)

                serialized_player2 = match.player2.serialize()
                self.tournament_progress.serialized_players.append(serialized_player2)

                self.tournament_progress.serialized_tournament = (
                    self.tournament_progress.serialize()
                )
                tournament_table.update(self.tournament_progress.serialized_tournament)

            next_round.endtime = vr.get_round_endtime()
            vt.print_info(f"End of the {round_name} at {next_round.endtime}.")
            vt.print_info("\n--------------------------------------\n")
            i += 1

        self.tournament_progress.serialized_tournament = (
            self.tournament_progress.serialize()
        )
        vt.print_info(
            f"{self.tournament_progress.name} is over !\n--------------------------------------\n"
        )
        vt.print_players_scores(self.tournament_progress.players)
        return tournament_table, actors_db

    def run_ungoing_tournament(self, db, tournament_name, actors_db):
        """ Fonction qui reprends un tournoi existant non terminé """
        tournament_table = db.table(f"{tournament_name}")

        self.instanciation_tournament(tournament_table, tournament_name)
        self.instanciation_players()
        self.instanciation_rounds()

        last_round_index = 0

        for i in range(len(self.tournament_progress.rounds) - 1):
            self.instanciation_matchs(i)
            last_round_index += 1

        r = len(self.tournament_progress.rounds)
        m = len(self.tournament_progress.rounds[last_round_index].matchs)

        if r == 0 and m < 3:
            self.run_first_round(tournament_table, actors_db)
        elif r == 1 and m < 3:
            self.run_rounds(tournament_table, actors_db, next_round_number=2)
        elif r == 2 and m < 3:
            self.run_rounds(tournament_table, actors_db, next_round_number=3)
        elif r == 3 and m < 3:
            self.run_rounds(tournament_table, actors_db, next_round_number=4)

    def instanciation_tournament(self, tournament_table, tournament_name):
        """ Fonction qui instancie le tournoi à partir du .json """
        liste_tournament = tournament_table.search(where("Name") == tournament_name)
        data = liste_tournament[0]

        self.tournament_progress = Tournament(
            data["Name"],
            data["Place"],
            data["Date"],
            data["Numbers of rounds"],
            data["Rounds"],
            [],
            data["Players"],
            data["Type"],
            data["Description"],
        )

    def instanciation_players(self):
        """ Fonction qui instancie les joueurs du tournoi à partir du .json """
        for serialized_player in self.tournament_progress.serialized_players:

            p = Player(
                serialized_player["Name"],
                serialized_player["Surname"],
                serialized_player["Birthday"],
                serialized_player["Sexe"],
                serialized_player["ELO"],
            )
            self.tournament_progress.add_player(p)

    def instanciation_rounds(self):
        """ Fonction qui instancie les rounds du tournoi à partir du .json """
        for serialized_round in self.tournament_progress.serialized_rounds:

            r = Round(
                serialized_round["Name"],
                serialized_round["Date"],
                serialized_round["Round start-time"],
                serialized_round["Round end-time"],
                [],
            )

            self.tournament_progress.add_round(r)

    def instanciation_matchs(self, i):
        """ Fonction qui instancie les matchs du tournoi à partir du .json """
        round_table = self.tournament_progress.serialized_rounds[i]
        round_matchs = round_table["Round Matchs"]

        for s_match in round_matchs:
            print(s_match)
            m = Match(
                player1=s_match["Player1"],
                player2=s_match["Player2"],
                score1=s_match["Score1"],
                score2=s_match["Score2"],
            )

            self.tournament_progress.rounds[i].add_match(m.player1, m.player2)

    def run_new_tournament(self, db, actors_db):
        """ Fonction qui lance un nouveau tournoi """
        tournament_table = self.new_tournament_created(db)

        self.init_players(tournament_table, actors_db)
        self.run_first_round(tournament_table, actors_db)
        self.run_rounds(tournament_table, actors_db)
