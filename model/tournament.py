class Tournament:
    """ Classe qui instancie un tournoi """

    def __init__(
        self,
        name,
        place,
        date,
        number_of_rounds,
        serialized_rounds,
        players,
        serialized_players,
        time_control,
        description,
    ):
        self.name = name
        self.place = place
        self.date = str(date)
        self.serialized_tournament = ""

        self.number_of_rounds = number_of_rounds

        self.rounds = []
        self.serialized_rounds = serialized_rounds

        self.players = []
        self.serialized_players = serialized_players

        self.time_control = time_control
        self.description = description

    def add_player(self, player):
        """ Méthode qui ajoute un joueur au tournoi """
        self.players.append(player)

    def add_round(self, one_round):
        """ Méthode qui ajoute un round au tournoi """
        self.rounds.append(one_round)

    def serialize(self):
        serialized_tournament = {
            "Name": self.name,
            "Place": self.place,
            "Date": self.date,
            "Type": self.time_control,
            "Description": self.description,
            "Players": self.serialized_players,
            "Numbers of rounds": self.number_of_rounds,
            "Rounds": self.serialized_rounds,
        }
        return serialized_tournament

    def print_players(self):
        """ Fonction qui imprime les joueurs et leurs attributs """
        for player in self.players:
            print(f"Name : {player.name}")
            print(f"Surname : {player.surname}")
            print(f"Birthday : {player.birthday}")
            print(f"Sexe : {player.sexe}")
            print(f"Elo : {player.elo}")
            print(f"Score : {player.score}")
