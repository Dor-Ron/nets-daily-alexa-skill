from bs4 import BeautifulSoup
from flask import Flask
from flask_ask import Ask, statement, question
import requests

app = Flask(__name__)
ask = Ask(app, "/")


def get_headlines():
    ''' gets html for daily news and returns headlines as a list of string '''
    html_doc = requests.get("https://www.netsdaily.com").text
    soup = BeautifulSoup(html_doc, "html.parser")
    headline_tags = soup.findAll("h2", {"class": "c-entry-box--compact__title"})
    return [tag.getText() for tag in headline_tags]


@ask.launch
def start_skill():
    ''' Function runs when you tell Alexa to invoke the skill '''
    verification = "Hello, would you like your Brooklyn Nets daily scoop?"
    return question(verification)


@ask.intent("YesIntent")
def share_scoop():
    ''' Makes Alexa share the Brooklyn Nets daily headlines with the user '''
    headlines = get_headlines()[:10]
    return statement("".join(headlines))


@ask.intent("NoIntent")
def terminate_skill():
    ''' Ends execution of app, in case user accidently invoked it '''
    farewell = "Brooklyn Nets related news is important... shalom"
    return statement(farewell)


if __name__ == "__main__":
    app.run(debug=True)
