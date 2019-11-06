from flask import Flask, render_template, request, redirect, url_for

from Code.stochastic_sampling import get_sentence
from Code.analyze_words import histogram_dict
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')


app = Flask(__name__)

@app.route('/')
def index():
    """returns user to the homepage"""
    words = 'Code/txtdocs/fish.txt'
    histogram = histogram_dict(words)
    sentence = get_sentence(histogram, 10)
    return render_template("home.html", tweet=sentence)

if __name__ == "__main__":
    app.run(Debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))