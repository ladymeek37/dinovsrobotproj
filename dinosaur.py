
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.dinosaur_health = 100
    def attack(self, robot):
            print ("")
            print(f"{self.name} got hit by Wallie's gun for 7 damage!")
            self.dinosaur_health -= 17
            print(f"{self.name} health: {self.dinosaur_health}")
            print ("")
            pass
        


        
    
