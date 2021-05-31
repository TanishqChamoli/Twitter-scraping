from flask import Flask, render_template, request
from flask import jsonify
from tweet_api import key_search

app = Flask(__name__)


@app.route('/', methods=["GET"])
def homepage():
    return render_template('home.html')

@app.route('/search', methods=["POST", "GET"])
def display_page():
    if request.method == "POST":
        data = request.form.get("data")
        if data=="":
            return "<h1>Please enter some data</h1><br><a href='/'>Go back</a>"
        tweets = key_search(data)
        return render_template('display.html', tweets = tweets,key=data)
    else:
        return "<h1>Please use the form!</h1><br><a href='/'>Go back</a>"
@app.route('/api/<data>')
def api_page(data):
    tweets = key_search(data)
    return jsonify(tweets)
if __name__ == '__main__':
    app.run()