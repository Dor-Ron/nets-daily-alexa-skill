from bs4 import BeautifulSoup
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def start_skill():
    ''' Function runs when you tell Alexa to invoke the skill '''
    verification = "Hello, would you like your Brooklyn Nets daily scoop?"
    return question(verification)


@ask.intent("YesIntent")
def share_scoop():
    ''' Makes Alexa share the Brooklyn Nets daily headlines with the user '''
    headlines = ""
    return statement(headlines)


@ask.intent("NoIntent")
def terminate_skill():
    ''' Ends execution of app, in case user accidently invoked it '''
    farewell = "Brooklyn Nets related news is important... shalom"
    return statement(farewell)


if __name__ == "__main__":
    app.run(debug=True)
