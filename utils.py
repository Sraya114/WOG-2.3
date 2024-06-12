import app
SCORES_FILE_NAME = "game_scores_sorted.csv"
BAD_RETURN_CODE = "Eror0703"







def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()


def continue_play():
    while True:
        user_play = input("Do you want to continue play?\n"
                          "type Yes [Y] or No [N]")
        if user_play not in ("Y", "Yes", "N", "No"):
            print("invalid request, please try agen")
        else:
            break
    if user_play == ("Y", "Yes"):
        app.start_play()
    elif user_play == ("N", "No"):
        print("Bye Bye")
        exit()
