
class Dinosaur:
    def __init__(self):
        self.name = "T-rex"
        self.health = 100
        self.attack_power = 10
    def attack(self, robot_health):
        print(f"{self.name} attacks Wallie!")
        robot_health = 100
        robot_health -= self.attack_power
        print(f"Wallie got hit by {self.name}!")
        print(f"Wallie's health: {robot_health}")
        pass


        
    
