# doppl

Fake tweet web app using Markov Chains and Twitter API with Flask backend developed in a weekend at HackMIT.

## Prerequisites 

This app was built using Python 2.7.6, and is not guaranteed to work with other versions.
We recommend using `pip` to install required dependencies. You can obtain `pip` here https://pypi.python.org/pypi/pip.
You will need twitter api keys to run this. They can be obtained here https://apps.twitter.com/.

## Setup

Install required packages by running:

```
git clone https://github.com/tHartman77/doppl.git
cd doppl
sudo pip install -r requirements.txt
```

Set environment variables for twitter api keys.
You will need to create a environment variables named:
  ```
  CONSUMER_KEY
  CONSUMER_SECRET
  ACCESS_TOKEN
  ACCESS_TOKEN_SECRET
  ```
And set them to the corresponding values you obtained from twitter.

Then run using:
```
FLASK_APP=app.py flask run
```
Open http://127.0.0.1:5000 in your browser.


Additionally, you can view our working version hosted by heroku at https://doppl.herokuapp.com.
