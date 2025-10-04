from flask import Flask, render_template
import json
import random

app = Flask(__name__)

def get_random_quote():
    with open("quotes.json", "r") as file:
        quotes = json.load(file)
    return random.choice(quotes)

@app.route("/")
def home():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)