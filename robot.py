from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.robot_health = 100
        self.active_weapon = Weapon("Gun", 7)
    def attack(self, dinosaur):
        print("")
        print(f"T-rex attacks {self.name} for 10 damage!")
        self.robot_health -= 20
        print(f"Wallie's remaining health: {self.robot_health}")
        print("")

        pass

