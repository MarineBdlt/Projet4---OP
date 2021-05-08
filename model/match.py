class Match:
    """ Classe qui instancie un match """

    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        # self.serialized_match = []

    def serialize(self):
        serialized_match = {
            "Player1": self.player1.name,
            "Score1": self.score1,
            "Player2": self.player2.name,
            "Score2": self.score2,
        }
        return serialized_match
