from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# from Code.sentence import get_sentence
# from Code.cleanup import *
# from Code.word_count import histogram_dict
# from Code.sample import sample_weight
# from Code.tokenize import read_file
# from Code.dictogram import Dictogram, read_file
from Code.markov_chain import Markov
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')


app = Flask(__name__)

@app.route('/')
def index():
    """returns user to the homepage"""
    word_doc = 'Code/txtdocs/sherlock.txt'
    markov = Markov(word_doc, 20)
    sentence = markov.main()
    return render_template("home.html", tweet=sentence)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))