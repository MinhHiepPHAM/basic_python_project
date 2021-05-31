from flask import Flask, request
from pymessenger.bot import Bot
import random


class Messenger_Bot:
    VERIFY_TOKEN = "VERIFY"
    ACCESS_TOKEN = "ACCESS"
    flask = Flask(__name__)
    def __init__(self):
        self.token_sent = ""
        self.bot = Bot(self.ACCESS_TOKEN)
        self.output = ""

    @flask.route("/", methods=['GET', 'POST'])
    def receive_message(self):
        # GET: The browser tells the server to just get the information stored on that page and send it
        if request.method == 'GET':
            # confirm all requests that your bot receives came from Facebook
            self.token_sent = request.args.get("hub.verify_token")
            return self.verify_token(self.token_sent)

        elif request.method == 'POST':
            # The browser tells the server that it wants to post some new information to that URL
            # and that the server must ensure the data is stored and only stored once.
            # This is how HTML forms usually transmit data to the server.
            self.output = request.get_json()
            for event  in self.output['entry']:
                messaging = event['messaging']
                for mess in messaging:
                    if mess.get('message'):
                        recipient_id = mess['sender']['id']
                        if mess['message'].get('text'):
                            text_sent = self.get_rand_message()
                            self.bot.send_text_message(recipient_id, text_sent)

                        if mess['message'].get('attachments'):
                            # it message is non-text (ex. photo, video, etc.)
                            non_text_sent = self.get_rand_message()
                            self.bot.send_message(recipient_id, non_text_sent)

                        else:
                            pass

        return "Success"

    def verify_token(self, token):
        if token == self.VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification'

    def get_rand_message(self):
        random_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!",
                            "We're greatful to know you :)"]
        return random.choice(random_responses)


if __name__ == '__main__':
    app = Messenger_Bot()
    app.flask.run()