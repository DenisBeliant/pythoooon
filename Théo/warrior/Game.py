from Character import Character
from window import Window
from PyQt5.QtWidgets import QApplication

class Game(object):
    TEAM_SIZE = 5

    def __init__(self):
        self._teams = [
            [0 for x in range(0, self.TEAM_SIZE)],
            [0 for x in range(0, self.TEAM_SIZE)]
        ]

    def place(self, team: int, position: int, player: Character):
        if team in range(0, 2) and position in range(0, self.TEAM_SIZE):
            if self.teams[team][position]:
                self.replace(team, position, player)
            else:
                self.teams[team][position] = player
        else:
            raise ValueError('equipe 1 ou 2 - position entre 0 et 4')

    def replace(self, team, position, player):
        choice = "a"
        while not (choice == "Y" or choice == "N"):
            choice = input(f"Veux-tu remplacer {self.teams[team][position].nom} equipe {team}, position {position} ?  Y/N")
            choice = choice.upper()
        if choice == "Y":
            self.teams[team][position] = player

    @property
    def teams(self):
        return self._teams

    def pop_char(self, team: int, position: int):
        if team in range(0, 2) and position in range(0, self.TEAM_SIZE):
            if self.teams[team][position]:
                self.teams[team][position] = 0
        else:
            raise ValueError('equipe 1 ou 2 - position entre 0 et 4')

    def print_teams(self):
        [print(f"{self.teams[0][i].nom if self.teams[0][i] else 0}   vs   {self.teams[1][i].nom if self.teams[1][i] else 0}\n") for i in range(0, self.TEAM_SIZE)]

    def display(self):
        app = QApplication([])
        w = Window(self.teams)
        w.show()
        app.exec_()

