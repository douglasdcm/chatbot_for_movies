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
	return render_template('index.html')

@app.route('/receiver', methods = ['POST'])
def worker():

	message = request.json['message']
	return cb.get_conversation(message)

if __name__ == '__main__':
	# run!
	app.run()