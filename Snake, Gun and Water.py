import random

def game_functions ():
    game_skills = ["Snake", "Gun", "Water"] 
    computer = random.choice(game_skills)
    return computer

def logic (computer, a):
    if computer == "Snake" and a == "Gun":
        print(f'You selected {a} and the computer selected {computer} \n You Won!!!!!')
        
    elif computer == "Snake" and a == "Snake":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
    
    elif computer == "Water" and a == "Water":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
        
    elif computer == "Gun" and a == "Gun":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
    
    elif computer == "Gun" and a == "Water":
        print(f'You selected {a} and the computer selected {computer} \n You won.')
    
    elif computer == "Snake" and a == "Water":
        print(f'You selected {a} and the computer selected {computer} \n You lost.')
        
    elif computer == "Water" and a=="Gun":
        print(f'You selected {a} and the computer selected {computer} \n You lost.')
        
    elif computer == "Water" and a == "Snake":
        print(f'You selected {a} and the computer selected {computer} \n You won.')
        
    elif computer == "Gun" and a == "Snake":
        print(f'You selected {a} and the computer selected {computer} \n You won.')
    


print( " WELCOME TO THE SNAKE, Water AND Gun GAME ")

a = input("Choose 1 from the following: \n \t Snake   \t   Water   \t   Gun \n Type Here: \t")

computer = game_functions()

logic(computer,a)
