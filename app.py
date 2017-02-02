
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import Flask, request, redirect
app = Flask(__name__)


@app.route("/sms/reply", methods=["GET", "POST"])
def reply():
	"""Respond to incoming texts with an echo"""
	resp = twilio.twiml.Response()
	print request.values
	resp.message(str(request.values))
	return str(resp)


if __name__ == "__main__":
	app.run()

# http://is-it-trump.herokuapp.com/sms/reply
# http://is-it-trump.herokuapp.com/sms/reply/