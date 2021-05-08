from model.match import Match


class Round:
    """ Classe qui instancie un round """

    def __init__(self, name, date, starttime, endtime=None, matchs=None):
        self.name = name
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.matchs = []
        self.serialized_matchs = []

    def add_match(self, player1, player2):
        """ Méthode qui ajoute un match au round """
        match = Match(player1, player2)
        self.matchs.append(match)

    def serialize(self):
        serialized_round = {
            "Name": self.name,
            "Date": "date",  # self.date not JSON serializable
            f"Round start-time": self.starttime,
            f"Round end-time": self.endtime,
            f"Round Matchs": self.serialized_matchs,
        }
        return serialized_round
