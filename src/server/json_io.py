#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
from backend.chatbot import ChatBotInit

app = Flask(__name__)

cb = ChatBotInit()

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='')

@app.route('/echo', methods = ['POST'])
def worker_postman():

	return request.json['message']

@app.route('/receiver', methods = ['POST'])
def worker():

	message = request.json['message']

	"""
	cb.get_conversation(message)
	# serve index template
	return render_template('index.html', name=c)
	"""
	return cb.get_conversation(message)


@app.route('/receiver_sample', methods = ['POST'])
def worker_sample():
	# read json + reply
	#data = request.get_json()

	data = [
				{ "make":"Porsche", "model":"911S" },
				{ "make":"Mercedes-Benz", "model":"220SE" },
				{ "make":"Jaguar","model": "Mark VII" }
			]

	result = ''
	for item in data:
		# loop over every row
		result += str(item['make']) + ''
	return result

if __name__ == '__main__':
	# run!
	app.run()