from game_character import GameCharacter
from medic import  Medic
from warrior import Warrior
from explorer import Explorer
import random



print('a new game has been started\n' )

#define player
W1=Warrior('W1',100,80,50,0)
M1=Medic('M1',100,70,60,20)
E1=Explorer('E1',100,60,40,0)
print('\n')
W2=Warrior('W2',100,80,50,0) 
M2=Medic('M2',100,70,60,20)
E2=Explorer('E2',100,60,40,0)
print('\n') 
   

#add player to teams
# def add_player_to_team():
team1=[]
team2=[]
team1.append(W1)
team1.append(M1)
team1.append(E1)
team2.append(W2)
team2.append(M2)
team2.append(E2)
    
#choose character from team to start the game
def choose_character():
    # i=1
    if i%2==0:
        print(f'>>>Round {i}\n')
        print('team2 it is  your turn ')
        print('which character do you wish to choose ')
        print('0-W2 \n1-M2\n2-E2')
        choose = int(input('choose character:'))
        while True:
            if choose==0:
               print("You have choosen 'W2'\n")
               print(" Warrior can do the following:\n")
               print('0-attack - attacks an enemy character\n1-cast spell - casts a spell on an enemy character ')
               chosse_action_worrior()  #call the function chosse_action_worrior() to choose the action 
               return choose
            elif choose==1:
               print("You have choosen 'M2'\n")
               print('Medic can do the following:\n ')
               print('0-heal -  heal other characters on the team.\n1-back to the future - increase the nanobots')
               choose_action_Medic()  #call the function chosse_action_Medic() to choose the action
               return choose
            elif choose==2:
               print("You have choosen 'E2'\n")
               print('Explorer can helps other characters find gold')
               return choose
            # else:
            #   choose=int(input('please chosse 0 or 1 or 2 :'))
    else:
        print(f'>>>Round {i}\n')
        print('team1 it is  your turn ')
        print('which character do you wish to choose ')
        print('0-W1 \n1-M1\n2-E1')
        choose = int(input('choose character:'))
        while True:
            if choose==0:
               print("You have choosen 'W1'\n")
               print(" Warrior can do the following:\n")
               print('0-attack - attacks an enemy character\n1-cast spell - casts a spell on an enemy character ')
               chosse_action_worrior() #call the function chosse_action_worrior() to choose the action 
               return choose
            elif choose==1:
               print("You have choosen 'M1'\n")
               print('Medic can do the following:\n ')
               print('0-heal -  heal other characters on the team.\n1-back to the future - increase the nanobots')
               choose_action_Medic() #call the function chosse_action_Medic() to choose the action
               return choose
            elif choose==2:
               print("You have choosen 'E1'\n")
               print('Explorer can helps other characters find gold') 
               return choose
            # else:
            #   choose=int(input('please chosse 0 or 1 or 2 :'))

#choose action
def chosse_action_worrior():
    action_warrior= int(input('choose action:'))
    if action_warrior ==0:
        print('which opponent do you wish to attack?')
        choose_opponent_for_attack() #call the function choose_opponent_for_attack() to choose the opponent
    elif action_warrior==1:
        print('casts a spell on an enemy character')
        choose_opponent_for_cast_spell_on()  #call the function choose_opponent_for_cast_spell_on() to cast spell on

# to choose opponent
def choose_opponent_for_attack():
    if i%2==0:
        print('0-W1 \n1-M1\n2-E1')
        opponent = int(input('choose opponent:'))
        if opponent==0:
            opponent=W1
            W2.attack(opponent)
            W1.get_health()
            print(f'{team1[0]} {team2[0]}') #to print the stats after the action
        elif opponent==1:
            opponent=M1
            W2.attack(opponent)
            M1.get_health()
            print(f'{team1[1]} {team2[0]}')
        elif opponent==2:
            opponent=E1
            W2.attack(opponent)
            E1.get_health()
            print(f'{team1[2]} {team2[0]}')
        else:
            print('please choose 0 or 1 or 2')
            opponent=int(input('choose opponent:'))
            choose_opponent_for_attack()
    else:
        print('0-W2 \n1-M2\n2-E2')
        opponent =int(input('choose opponent:'))
        if opponent==0:
            opponent=W2
            W1.attack(opponent)
            W2.get_health()
            print(f'{team1[0]} {team2[0]}')
        elif opponent==1:
            opponent=M2
            W1.attack(opponent)
            print(f'{team1[0]} {team2[1]}')
        elif opponent==2:
            opponent=E2
            W1.attack(opponent)
            print(f'{team1[0]} {team2[2]}')
        else:
            print('please choose 0 or 1 or 2')
            opponent=int(input('choose opponent:'))
            choose_opponent_for_attack()


def choose_opponent_for_cast_spell_on():
    if i%2==0:
        print('0-W1 \n1-M1\n2-E1')
        opponent = int(input('choose opponent:'))
        if opponent==0:
            opponent=W1
            W2.cast_spell_on(opponent)
        elif opponent==1:
            opponent=M1
            W2.cast_spell_on(opponent)
        elif opponent==2:
            opponent==E1
            W2.cast_spell_on(opponent)
        else:
            print('please choose 0 or 1 or 2')
            opponent=int(input('choose opponent:'))
            choose_opponent_for_cast_spell_on()
    else:
        print('0-W2 \n1-M2\n2-E2')
        opponent =int(input('choose opponent:'))
        if opponent==0:
            opponent=W2
            W1.cast_spell_on(opponent)
        elif opponent==1:
            opponent=M2
            W1.cast_spell_on(opponent)
        elif opponent==2:
            opponent==E2
            W1.cast_spell_on(opponent)
        else:
            print('please choose 0 or 1 or 2')
            opponent=int(input('choose opponent:'))
            choose_opponent_for_cast_spell_on()


def choose_action_Medic():
    action_medic=int(input('choose action:'))
    if action_medic==0:
        print('which member do you want to heal')
        choose_character_to_medic()
    elif  action_medic==1:
        print('Now medic will travel to the futuer to increase nanobots')
        M1.back_to_the_future()

def choose_character_to_medic():
    if i%2==0:
        print('0-W2 \n1-E2')
        character = int(input('choose character:'))
        if  character==0:
            character=W2
            M2.heal(character)
        elif  character==1:
            character=E2
            M2.heal(character)
        else:
            print('please choose 0 or 1 or 2')
            character=int(input('choose character:'))
            choose_character_to_medic()
    else:
        print('0-W1 \n1-E1')
        character =int(input('choose character:'))
        if character==0:
            character=W1
            M1.heal(character)
        elif character==1:
            character=E1
            M1.heal(character)
        else:
            print('please choose 0 or 1 or 2')
            character=int(input('choose character:'))
            choose_character_to_medic()
# define function to check the winner
def check_winner():
    health_W1=W1.get_health()
    health_M1=M1.get_health()
    health_E1=E1.get_health()
    health_team1=health_W1 + health_M1 + health_E1

    health_W2=W2.get_health()
    health_M2=M2.get_health()
    health_E2=E2.get_health()
    health_team2=health_W2 + health_M2 + health_E2
    if health_team1==0:
        print(f'**team2 is the winner**')
    elif health_team2==0:
        print(f'**team1 is the winner**')


if __name__ == "__main__":
    i=1 # number of round
    for i in range(1,26):
        choose_character()
        check_winner()
        i=i+1
        
        
   



