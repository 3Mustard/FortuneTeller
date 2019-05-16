#import for flask and flask's render_template method
from flask import Flask, render_template
#import Resoursce and API to make HTTP requests
from flask_restful import Resource, Api
#import the tarot card JSON
import tarotCards
#import for random integer
import random

#make this a Web-App
app = Flask(__name__)
#gives the ability to make HTTP requests
api = Api(app)

#return the entire deck as JSON array with HTTP request http://127.0.0.1:5002/Deck
class Deck(Resource):
    def get(self):
        return tarotCards.tarotcards

#return the top card as JSON object with HTTP request http://127.0.0.1:5002/DrawOne
class DrawOne(Resource):
    def get(self):
        cards = tarotCards.tarotcards
        random.shuffle(cards)
        return cards[0]

#return the top three cards as JSON array with HTTP request http://127.0.0.1:5002/DrawOne
class DrawThree(Resource):
    def get(self):
        cards = tarotCards.tarotcards
        random.shuffle(cards)
        cardsdrawn = [cards[0], cards[1], cards[3]]
        return cardsdrawn

#displays the index.html as the homepage
@app.route("/")
def home():
    return render_template("index.html")

#route for calling HTTP request http://127.0.0.1:5002/Deck
api.add_resource(Deck, '/Deck')
#route for calling HTTP request http://127.0.0.1:5002/DrawOne
api.add_resource(DrawOne, '/DrawOne')
#route for calling HTTP request http://127.0.0.1:5002/DrawThree
api.add_resource(DrawThree, '/DrawThree')

#make this file the main method that needs to be run
if __name__ == '__main__':
    app.run(port="5002")
