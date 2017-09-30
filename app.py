from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from markov import get_markov_tweet, get_rand_id, check_handle
app = Flask(__name__)

@app.route('/_get_tweet')
def get_tweet():
    handle = request.args.get('handle', '', type=str)
    if check_handle(handle) == False:
        return jsonify(result='error')
    return jsonify(result=get_markov_tweet(handle), rand_id=get_rand_id(handle))

@app.route('/')
def index():
    return render_template('index.html')
