# This function takes a person's name as input and displays a personalized welcome message
from games import currency_roulette_game, memory_game, guess_game
import os
import utils
os.system('pip install pyfiglet')
os.system('pip install colorama')
os.system('pip install termcolor')


def welcome():
    utils.clear_screen()
    import sys

    from colorama import init
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    from termcolor import cprint
    from pyfiglet import figlet_format

    cprint(figlet_format('WORLD OF GAME', font='starwars'),
           'yellow', 'on_red', attrs=['bold'])

    print(f'welcome to the World of Games: The Epic Journey')








def start_play():
    user_name = input("please eneter your name: ")


    game = ["none","Memory Game", "Guess Game", "Currency Roulette"]
    while True:

     choose_game = input("Please choose a game to play:\n" 
                            "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.[1]\n"
                            "Guess Game - guess a number and see if you chose like the computer.[2]\n"
                            "Currency Roulette - try and guess the value of a random amount of USD in ILS.[3]\n")

     if choose_game not in ('1', '2', '3'):
         print("invalid request, please try agen")
     else:
         break




    your_game = game[int(choose_game)]
    print(f'you choose {your_game}!\n \n')

    # the user choose the difficulty level

    level_index = ['none', 'baby level', 'Childrens level', 'medium level', 'hard level', 'Super hard level']
    while True:
     difficulty_level = input ("Please select a difficulty level you would like to play\n"
                                     "baby level[1]\n"
                                     "Children's level level[2]\n"
                                     "medium level[3]\n"
                                     "hard level[4]\n"
                                     "super hard level[5]\n" )
     if difficulty_level not in ('1', '2', '3', '4', '5'):
         print("invalid request, please try agen")
     else:
         break




    print(f'you choose {your_game} in {level_index[int(difficulty_level)]}, lets play!')


    difficulty_level = int(difficulty_level)


    if choose_game == '2':
        guess_game.play(difficulty_level, user_name)
    elif choose_game == '1':
     memory_game.play(difficulty_level, user_name)

    elif choose_game == '3':
        currency_roulette_game.play(difficulty_level, user_name)



    # return choose_game, int(difficulty_level)

def continue_play():
    while True:
     user_play = input("Do you want to continue play?\n"
                              "type Yes [Y] or No [N]")
     if user_play not in ("Y", "Yes","yes", "N", "No", "no"):
            print("invalid request, please try agen")
     else:
            break
    if user_play == ("Y"or "Yes" or "yes"):
            start_play()
    elif user_play == ("N" or "No" or "no"):
            print("Bye Bye")
            exit()


