from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Wallie"
        self.health = 100
        self.active_weapon = Weapon("Gun", 7)
    def attack(self, dinosaur:object):
        print(f"{self.name} attacks {dinosaur.name}!")
        dinosaur.health_points -= self.active_weapon.attack_power
        print(f"{dinosaur.name} got hit by {self.name}'s {self.active_weapon.name}!")
        print(f"{dinosaur.name}'s health: {dinosaur.health}")
        pass

