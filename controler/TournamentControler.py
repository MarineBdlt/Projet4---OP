import view.player as vp
import view.round as vr
import view.tournament as vt
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament

from tinydb import TinyDB, Query, where
from tinydb.operations import delete


# Pour recharger les joueurs sérialisés, tu peux faire ceci :
# serialized_players = players_table.all()
# User = Query()
# db.insert({'name': 'John', 'age': 22})
# db.search(User.name == 'John')


class TournamentControler:
    """ Classe qui lance et fait fonctionner le tournoi """

    def __init__(self):

        self.tournament_progress = ""
        # instanciée dans la classe création"
        # sortir de la classe
        # créer une fonction reprendre le dernier tournoi ou en créer un autre

    def new_tournament_created(self, db):

        # instancier le tournoi en dehors de la classe
        self.tournament_progress = Tournament(
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

        tournament_table = db.table(f"{self.tournament_progress.name}")
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

        serialized_tournament = self.tournament_progress.serialize()
        tournament_table.insert(serialized_tournament)

        return tournament_table

    def init_players(self, tournament_table, actors_db):
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
            self.tournament_progress.add_player(player)

            serialized_player = player.serialize()
            actor_table = actors_db.table(f"{name}")
            actor_table.insert(serialized_player)

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
        players = []
        for player in self.tournament_progress.players:
            players.append(player)
        players.sort(key=lambda x: x.elo)
        players.sort(key=lambda x: x.score, reverse=True)

        return players

    def make_pairing(self, players, current_round):
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

    def update_tournament_table(self, tournament_table, player1, player2):
        """ Fonction qui update scores et opponents dans la table du tournoi """
        tournament_table.update_multiple(
            [
                (
                    {"Score": player1.score},
                    where("Name") == player1.name,
                ),
                (
                    {"Score": player2.score},
                    where("Name") == player2.name,
                ),
            ]
        )

        tournament_table.update_multiple(
            [
                (
                    {"Opponents": player1.opponents},
                    where("Name") == player1.name,
                ),
                (
                    {"Opponents": player2.opponents},
                    where("Name") == player2.name,
                ),
            ]
        )
        '''
        def update_actors_table(self, actors_table, player1, player2):
            """ Fonction qui update scores et opponents dans la table des acteurs """
            actors_table.update_multiple(
                [
                    (
                        {"Score": player1.score},
                        where("Name") == player1.name,
                    ),
                    (
                        {"Score": player2.score},
                        where("Name") == player2.name,
                    ),
                ]
            )
            actors_table.update_multiple(
                [
                    (
                        {"Opponents": player1.opponents},
                        where("Name") == player1.name,
                    ),
                    (
                        {"Opponents": player2.opponents},
                        where("Name") == player2.name,
                    ),
                ]
            )
            '''

    def run_first_round(self, tournament_table, actors_db):
        """ Fonction qui fait tourner le premier round """
        # instancie le round
        round_name = "Round 1"
        round_date = vr.get_round_date()
        round_starttime = vr.get_round_starttime()
        round1 = Round(round_name, round_date, round_starttime)

        # serialize le round
        serialized_round1 = round1.serialize()
        # self.rounds_table.insert(serialized_round1)

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

        # ajoute le round au tournoi
        self.tournament_progress.add_round(round1)

        # instancie les matchs dans la classe Round
        i = 0

        for match in self.tournament_progress.rounds[0].matchs:
            vt.print_info("\n...\n")
            vt.print_info(
                f"{match.player1.name} and {match.player2.name} play against each other !"
            )
            # input et print les résultats du match
            match.score1, match.score2 = self.handle_score(match)
            i += 1

            vr.print_match_result(match)

            serialized_match = match.serialize()
            round1.serialized_matchs.append(serialized_match)

            match.player1.add_opponent(match.player2)
            match.player2.add_opponent(match.player1)

            match.player1.add_score(match.score1)
            match.player2.add_score(match.score2)

            """
            actor_table = actors_db.table(f"{match.player1.name}")
            actor_table.insert_multiple(
                [
                    {f"Score {self.tournament_progress.name}": match.player1.score},
                    {
                        f"Opponents {self.tournament_progress.name}": match.player1.opponents
                    },
                ]
            )
            """

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
            # pourquoi fonction inconnue ?

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

            """
            Tournament = Query()
            tournament_table.upsert(
                {"Rounds": self.tournament_progress.serialized_rounds},
                Tournament.name == self.tournament_progress.name,
            )
            """

            vt.print_info(f"{round_name} launchment...")

            self.make_pairing(players, next_round)
            self.tournament_progress.serialized_players.clear()

            for match in self.tournament_progress.rounds[i - 1].matchs:  # bon indice ?
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

                """

                actor_table = actors_db.table(f"{match.player1.name}")
                actor_table.update(
                    {f"Score {self.tournament_progress.name}": match.player1.score}
                )
                actor_table.update(
                    {
                        f"Opponents {self.tournament_progress.name}": match.player1.opponents
                    }
                )
                """

            # ajouter score dans db après chaque match
            next_round.endtime = vr.get_round_endtime()

            # tournament_table.update()

            vt.print_info(f"End of the {round_name} at {next_round.endtime}.")
            vt.print_info("\n--------------------------------------\n")
            i += 1

        self.tournament_progress.serialized_tournament = (
            self.tournament_progress.serialize()
        )

        vt.print_info(
            f"{self.tournament_progress.name} is over !\n--------------------------------------\n"
        )
        vt.print_players_scores(self.tournament_progress.players)  # winners

        return tournament_table, actors_db

    def run_ungoing_tournament(self, db, tournament_name, actors_db):
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

        """
        def run_new_tournament():

        lancement1 = TournamentControler()

        tournament_table = lancement1.new_tournament_created(db)

        lancement1.init_players(tournament_table, actors_db)
        lancement1.run_first_round(tournament_table, actors_db)
        lancement1.run_rounds(tournament_table, actors_db)
        """
