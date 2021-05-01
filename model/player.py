class Player:
    """ Classe qui instancie un joueur """

    def __init__(self, name, surname, birthday, sexe, elo, score=0):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.sexe = sexe
        self.elo = elo
        self.score = 0

    def print_player(self):
        """ Méthode qui imprime un les attributs d'un joueur """
        print(f"name : {self.name}")
        print(f"surname : {self.surname}")
        print(f"birthday : {self.birthday}")
        print(f"sexe : {self.sexe}")
        print(f"elo : {self.elo}")

    def add_score(self, score):
        """ Méthode qui ajoute des points au score du joueur """
        self.score += score
