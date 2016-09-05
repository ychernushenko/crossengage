from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re

# INIT
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:123456@mysql-server:3306/cross_engage'
db = SQLAlchemy(app)

access_token = "18723439-gACBmsUOg02FDfxrocjz1ZEe3ig1E6vtZWqxipx4t"
access_token_secret = "ClHRnNAQZ1MPOqujMpKXWtzQxABPQz7aeEchk1MgtY2aS"
consumer_key = "17ajP3edxCEtj1AV2vTtXGNKK"
consumer_secret = "XvucvItWMkTgQEm7O5Y0oiCjhMRNIqDvzEoLSKR69G2Fv6uLDQ"

search_list = ['python', 'java', 'javascript', 'rust', 'elexir']

class Counter(db.Model):
	__tablename__ = "counter"
	id = db.Column('id',db.Integer , primary_key=True)
	name = db.Column('name', db.String(20), unique=True , index=True)
	value = db.Column('value' , db.Integer)

	def __init__(self, name, value):
		self.name = name
		self.value = value

class StdOutListener(StreamListener):

    def on_data(self, data):
        global search_list

        for item in search_list:
            if word_in_text(item, data):
                counter = Counter.query.filter_by(name=item).first()

                if counter is None:
                    counter = Counter(item, 1)
                    db.session.add(counter)
                else:
                    counter.value += 1

                db.session.commit()
                break

        return True

    def on_error(self, status):
        print status

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=search_list)
