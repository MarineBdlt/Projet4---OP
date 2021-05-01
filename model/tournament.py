from model.player import Player
from view.tournament import *


class Tournament:
    """ Classe qui instancie un tournoi """

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
        self.number_of_rounds = number_of_rounds
        self.players = players
        self.time_control = ""
        self.description = description
        self.rounds = []

    def add_player(self, player):
        """ Méthode qui ajoute un joueur au tournoi """
        self.players.append(player)

    def add_round(self, one_round):
        """ Méthode qui ajoute un round au tournoi """
        self.rounds.append(one_round)

        # match = Match(player1, player2)
        # self.matchs.append(match)
