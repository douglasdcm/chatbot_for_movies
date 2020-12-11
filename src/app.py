#!flask/bin/python
import os, sys
from settings import ROOT_DIR, BOT_PREFIX
sys.path.append(ROOT_DIR + '/backend/')
sys.path.append(ROOT_DIR + '/frontend/')

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
	return BOT_PREFIX + cb.get_conversation(message)

if __name__ == '__main__':
	# run!
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', threaded=True, port=port)