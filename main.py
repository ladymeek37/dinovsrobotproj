from robot import Robot
from dinosaur import Dinosaur
from battlefield import Battlefield

battlefield = Battlefield
robot = Robot("Wallie")
dinosaur = Dinosaur("T-rex", 7)

robot.attack(Dinosaur)
dinosaur.attack(Robot)
battlefield.display_welcome(Battlefield)
battlefield.battle_phase(Battlefield)
