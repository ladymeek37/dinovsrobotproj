from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Wallie")
        self.dinosaur = Dinosaur("T-rex", 7)

    def display_welcome(self):
        print("")
        print("Welcome to the extreme battle of Robot vs. Dinosaur!")
        print("Only one side will take the victory!")
        print("")
        pass

    def battle_phase(self):
        self.robot = Robot("Wallie")
        self.dinosaur = Dinosaur("T-rex", 7)
        while self.robot.robot_health > 0 and self.dinosaur.dinosaur_health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            if self.dinosaur.dinosaur_health <= 0:
                self.winner = self.robot.name
            elif self.robot.robot_health <= 0:
                self.winner = self.dinosaur.name
            pass

    def display_winner(self):
        print(f"{self.winner} took the victory, winning the epic battle of Dinosaur vs. Robot!!!")
        print("")
        pass

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


