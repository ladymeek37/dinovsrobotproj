from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.robot_health = 100
        self.active_weapon = Weapon("Gun", 7)
    def attack(self, dinosaur):
        print("")
        dinosaur.dinosaur_health -= self.active_weapon.attack_power  
        print(f"{self.name} hit {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!")
        print(f"{dinosaur.name} has {dinosaur.dinosaur_health} health remaining...")
        print("")


    