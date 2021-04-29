from model.player import Player
from view.tournament import *


class Tournament:
    def __init__(
        self,
        name,
        place,
        date,
        number_of_rounds,
        players,
        time_control,
        description,
    ):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.players = players
        self.time_control = ""
        self.description = description
        self.rounds = []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, one_round):
        self.rounds.append(one_round)

        # match = Match(player1, player2)
        # self.matchs.append(match)
