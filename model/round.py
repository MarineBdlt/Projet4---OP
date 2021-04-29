from model.match import Match


class Round:
    def __init__(self, name, date, starttime, endtime=None, matchs=None):
        self.name = name
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.matchs = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matchs.append(match)