
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.dinosaur_health = 100
    def attack(self, robot):
            print ("")
            robot.robot_health -= self.attack_power
            print(f"{self.name} attacked {robot.name} for {self.attack_power} damage!")
            print(f"{robot.name} has {robot.robot_health} health remaining...")
            print ("")
            pass
        


        
    
