import os
os.system("pip install requests")
import requests
import random
import score


def convert_currency(secret_number):
        url = 'https://v6.exchangerate-api.com/v6/2f5f9323020573362e1c0f25/latest/USD'

        response = requests.get(url)
        data = response.json()
        exchange_rate = data["conversion_rates"]["ILS"]
        secret_number * exchange_rate
        return secret_number
def get_guess_from_user(random_number):
    while True:
            print(f"Enter your guess for the converted {random_number} in ILS:")
            guess = float(input())
            return guess


def get_money_interval(difficulty_level):
        random_number = random.randint(1, 100)
        guess = get_guess_from_user(random_number)
        usd_to_ils_rate = convert_currency(random_number)
        difference = 10 - difficulty_level
        lower_bound = usd_to_ils_rate - difference
        upper_bound = usd_to_ils_rate + difference
        compare_results(lower_bound, upper_bound, guess, difficulty_level)




        return lower_bound, upper_bound, difficulty_level

def compare_results(lower_bound, upper_bound, guess, difficulty_level):

    if lower_bound <= guess  <= upper_bound:


        print("Congratulations! Your guess was correct.")
        score.score(difficulty_level)




    else:
                print("Sorry, your guess was incorrect.")


def play(difficulty_level, user_name):
    get_money_interval(difficulty_level)
    score.score(difficulty_level, user_name)





