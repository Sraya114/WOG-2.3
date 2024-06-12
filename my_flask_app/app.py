# import pandas as pd
# df = pd.read_csv('game_scores_sorted.csv')
# df.to_html('templates/game_scores_sorted.html')
#
# # app.py
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('game_scores_sorted.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('game_scores_sorted.csv')
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('game_scores_sorted.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)


