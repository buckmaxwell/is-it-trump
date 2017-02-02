
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import Flask, request, redirect
app = Flask(__name__)


@app.route("/sms/reply", methods=["GET", "POST"])
def reply():
	 """Respond to incoming texts"""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)


if __name__ == "__main__":
    app.run()