import random
import time
import utils
import score


def generate_sequence(difficulty_level):
    generate_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
    return generate_numbers




def get_list_from_user(difficulty_level):
        user_input = input(f"Enter the sequence of {difficulty_level} numbers separated by spaces: ")
        user_guess = list(map(int, user_input.split()))
        return user_guess





def is_list_equal(user_guess, generate):
    if user_guess == generate:
        print(True)
    else:
        print(False)





def play(difficulty_level, user_name):
    generate = generate_sequence(difficulty_level)
    print(f"Memorize the sequence:  {generate}")
    time.sleep(0.7)
    utils.clear_screen()
    user_guess = get_list_from_user(difficulty_level)
    is_list_equal(user_guess, generate)
    score.score(difficulty_level, user_name)



