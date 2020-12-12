
from game_character import GameCharacter
import random
from datetime import datetime,timedelta
import os
import time

class Medic(GameCharacter):

    def __init__(self, name, health, heal, magic,nanobots):

        super().__init__(name, health, heal, magic)

        print(f"Your medic {self.name}, to the rescue!")

        self.nanobots = nanobots   #defined the attributes nanobots
        self.nanobots_accuracy_level =0  #defined the attributes nanobots_accuracy_level and give it defulte value 0

    def heal(self, character):
        heal_value = (random.randrange(self.strength - 10 , self.strength + 10)/10)
        print(f"> {self.name} is healing {character.name}. {(heal_value)}")

        if character.get_health() + heal_value > character.max_health:
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)

        return heal_value
    
    def attack(self, character):
        self.heal(character)

    def back_to_the_future(self):
        dt = datetime.now()
        td = timedelta(microseconds=50)
        the_date = dt + td
        diff_=the_date - dt
        self.nanobots = self.nanobots + diff_.microseconds
        print(f' now you have number of nanobots equale = {self.nanobots}')
        self.nanobots_accuracy_level = self.nanobots_accuracy_level + 1
        print(f' You have nanobots accuracy level ={self.nanobots_accuracy_level}')
        return self.nanobots_accuracy_level
               
