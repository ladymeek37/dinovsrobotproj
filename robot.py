from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Wallie"
        self.health = 100
        self.active_weapon = Weapon("Gun", 7)
    def attack(self, dinosaur_health):
        print(f"{self.name} attacks T-rex!")
        dinosaur_health = 100
        dinosaur_health -= self.active_weapon.attack_power
        print(f"T-rex got hit by {self.name}'s {self.active_weapon.name}!")
        print(f"T-rex's health: {dinosaur_health}")
        pass

