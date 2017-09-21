from flask import Flask, jsonify, render_template, request
from markov import get_markov_tweet, get_rand_id 
app = Flask(__name__)

@app.route('/_get_tweet')
def get_tweet():
    handle = request.args.get('handle', '', type=str)
    return jsonify(result=get_markov_tweet(handle), rand_id=get_rand_id(handle))

@app.route('/')
def index():
    return render_template('index.html')
