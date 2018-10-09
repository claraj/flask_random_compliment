from flask import Flask, render_template, jsonify
from compliments import random_compliment

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/random')
def random():
    compliment = random_compliment()
    return jsonify(compliment)


if __name__ == '__main__':
    app.run()
