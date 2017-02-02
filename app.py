
import csv
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import Flask, request, redirect
import random
from fuzzywuzzy import fuzz

# Constants

TRUMP_LOVERS = "trump-lovers.csv"
TRUMP_EH = "trump-eh.csv"
TRUMP_HATERS = "trump-haters.csv"
PERCENT_MATCHING = 85
NAMES_FOR_TRUMP = ['Orange Boy', 'Agent Orange', 'the Zen Master of Hate', 'the Short-Fingered Vulgarian',
'Pixie Fingers', 'that Unrepentant Narcissistic Asshole', 'the Hair Furor', 'the Cheeto-Dusted Bloviator']


app = Flask(__name__)


@app.route("/sms/reply", methods=["GET", "POST"])
def reply():
	"""Respond to incoming texts with an echo"""
	resp = twilio.twiml.Response()
	company = request.values.get('Body').title()
	r_message = "As far as we know, nothing is wrong with {}".format(company)

	# good guys
	with open(TRUMP_HATERS, 'rb') as csvfile:
		trump_reader = csv.reader(csvfile)
		for row in trump_reader:
			
			if fuzz.partial_ratio(company.decode('utf8'), row[0].decode('utf8').title()) >= PERCENT_MATCHING:
				r_message = "{} has taken a stance against {}.  Go for it!".format(
					row[0].title(), random.choice(NAMES_FOR_TRUMP))
				break

	# eh guys
	with open(TRUMP_EH, 'rb') as csvfile:
		trump_reader = csv.reader(csvfile)
		for row in trump_reader:
			
			if fuzz.partial_ratio(company.decode('utf8'), row[0].decode('utf8').title()) >= PERCENT_MATCHING:
				r_message = "{} is not on the grabyourwallet boycott list.  Here's what we know: {}".format(
					row[0].title(), row[1])
				break

	# bad guys
	with open(TRUMP_LOVERS, 'rb') as csvfile:
		trump_reader = csv.reader(csvfile)
		for row in trump_reader:

			if fuzz.partial_ratio(company.decode('utf8'), row[0].decode('utf8').title()) >= PERCENT_MATCHING:
				r_message = "Ugg, {} kinda supports {}.  Reason? {}".format(
					row[0].title(), random.choice(NAMES_FOR_TRUMP), row[1])
				break


	
	
	resp.message(r_message)
	return str(resp)


if __name__ == "__main__":
	app.run()
