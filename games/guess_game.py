from random import randint
import score


def generate_number(difficulty_level,guess):
    secret_number = randint(1, difficulty_level)
    compare_results(secret_number,guess)




def get_guess_from_user(difficulty_level):
    guess = input(f"please enter number between 1-{difficulty_level}:\n")
    generate_number(difficulty_level, guess)




def compare_results(secret_number, guess):
    # print(secret_number)
    # print(guess)
    if secret_number == guess:

       print("TRUE")
       return True
    else:
       print("FALSE")



def play(difficulty_level, user_name):
    get_guess_from_user(difficulty_level)
    score.score(difficulty_level, user_name)









