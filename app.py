from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/_get_tweet')
def get_tweet():
    handle = request.args.get('handle', '', type=str)
    return jsonify(result=get_markov(handle))

@app.route('/')
def index():
    return render_template('index.html')
