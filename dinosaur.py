class Dinosaur:
    def __init__(self):
        self.name = "T-rex"
        self.health = 100
        self.attack_power = 10
    def attack(self, robot:object):
        print(f"{self.name} attacks {robot.name}!")
        robot.health -= self.attack_power
        print(f"{robot.name} got hit by {self.name}!")
        print(f"{robot.name}'s health: {robot.health}")
        pass


        
    
