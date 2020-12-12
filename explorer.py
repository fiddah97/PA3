from game_character import GameCharacter
import random

class Explorer(GameCharacter):

    def __init__(self, name, health, attack_max, magic,gold):

        super().__init__(name, health, attack_max, magic)

        print(f"Commander '{self.name}' at your service.")
        self.gold = gold
        self.foresight = 1

# try to write a map for the explorer
from csv import writer,reader  
fp = open('random.csv','w',newline='')
csv_writer = writer(fp)
random_map = [
        ['$', 'X', '$', '$'],
        ['$', '$', 'X', 'X'],
        ['X', 'X', '$', 'X'],
        ['$', 'X', 'X', '$'],
      ]
csv_writer.writerows(random_map)
fp.close()







