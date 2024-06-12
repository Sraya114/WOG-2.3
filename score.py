import os
import datetime
os.system("pip install --pre --extra-index https://pypi.anaconda.org/scientific-python-nightly-wheels/simple pandas")
def user_name (user_name):
    return user_name
def score(difficulty_level, user_name):
    POINTS_OF_WINNING = (difficulty_level*3) + 5
    add_score(POINTS_OF_WINNING, user_name)

def add_score(POINTS_OF_WINNING, user_name):
    import pandas as pd
    from datetime import datetime

    now = datetime.now()

    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print(dt_string)


    def add_user_score(username, score):


        try:
            df = pd.read_csv('my_flask_app/game_scores_sorted.csv')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['username', 'score', 'time'])


        new_entry = pd.DataFrame({'username': [username], 'score': [score], 'time': [now]})
        df = df._append(new_entry, ignore_index=True)


        df_sorted = df.sort_values(by='score', ascending=False)


        df_sorted.to_csv('my_flask_app/game_scores_sorted.csv', index=False)


    add_user_score(user_name, POINTS_OF_WINNING)

