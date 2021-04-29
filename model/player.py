class Player:
    def __init__(self, name, surname, birthday, sexe, elo):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.sexe = sexe
        self.elo = elo

    def print_player(self):
        print(f"name : {self.name}")
        print(f"surname : {self.surname}")
        print(f"birthday : {self.birthday}")
        print(f"sexe : {self.sexe}")
        print(f"elo : {self.elo}")