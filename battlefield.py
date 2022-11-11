from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    def run_game(self):
        pass
    def display_welcome(self):
        print("Welcome to the extreme battle of Robot vs. Dinosaur!")
    def battle_phase(self,winner):
        self.winner = winner
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
            elif self.robot.health <= 0:
                self.winner = self.dinosaur.name


    def display_winner(self):
        print(f"{self.winner} won the battle!")
