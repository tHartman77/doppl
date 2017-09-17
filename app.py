from flask import Flask, jsonify, render_template, request
from markovtest import get_markov_tweet, get_rand_tweet_id
app = Flask(__name__)

@app.route('/_get_tweet')
def get_tweet():
    handle = request.args.get('handle', '', type=str)
    print(get_markov_tweet(handle), get_rand_tweet_id(handle))    
    return jsonify(result=get_markov_tweet(handle), id=get_rand_tweet_id(handle))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
