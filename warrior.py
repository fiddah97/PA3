from game_character import GameCharacter
import random
class Warrior(GameCharacter):

    def __init__(self, name, health, attack_max, magic,popularity):

        super().__init__(name, health, attack_max, magic)

        print(f"{self.name} is ready to fight! ")
        self.popularity= int(popularity)

    
    def buy_armor(self,gold):
        print('Which member you want to buy armor for him \n0-M\n1-E')
        member=int(input('please choose  member'))
        if member==0:
            increase_in_health=random.randint(0, 21)
            health_= self.health+increase_in_health
            popularity_= self.popularity+1
            return health_ ,popularity_
            
        elif member==1:
            increase_in_health=random.randint(0, 21)
            health_= self.health+increase_in_health
            popularity_= self.popularity+1
            return health_,popularity_
        
   
        

