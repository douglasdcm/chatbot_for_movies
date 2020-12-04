import os

ROOT_DIR = os.getcwd()+'/'
BACKEND_DIR = ROOT_DIR + '/backend/'
FRONTEND_DIR = ROOT_DIR + '/frontend/'
CHATDATA_DIR = ROOT_DIR + '/chatdata/'

DATA_FILE = CHATDATA_DIR + 'movie_lines_pre_processed.tsv'  #_for_test.tsv'
PAGE_RANK_ANSWERS = CHATDATA_DIR + 'page_rank_answers.txt'
PAGE_RANK_QUESTIONS = CHATDATA_DIR + 'page_rank_questions.txt'
TOKENIZER_FILE = CHATDATA_DIR + 'tokenizer.pickle'
LOG_FILE = ROOT_DIR + 'log.txt'

DEBUG_MODE = ['info']

EMERGENCY_MSG = ['I cannot understand it. Try again, please!',
				'I would like to hear more about it',
				'Sorry, my Spanish is not good... Can you explain it in English?',
				'Talk more about it',
				'Can you explain it?',
				'My brain could not process this message... Try again, please!',
				'If you are lost you can type "bye" anytime to leave'
				]

NAIVE_MSG = ['I could not find a good answer for your message...',
			'42',
			'Your message is very clever to my poor processor...',
			'I cannot answer this',
			'My friend, I am just chat bot, not a human...']

BOT_PREFIX = '  Bot:  '
YOU_PREFIX = '  You: '