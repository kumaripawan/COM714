from flying_superpower import FlyingSuperpower
from human import Human
from invisibility_super_power import InvisibilitySuperPower

class SuperHuman(Human, FlyingSuperpower, InvisibilitySuperPower):

    def __init__(self):
        pass

    def fly(self):
        print("I am flying!!!")

    def turn_invisible(self):
        print("I am now invisible")

    def turn_visible(self):
        print("I am now visible")