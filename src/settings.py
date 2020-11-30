import os

ROOT_DIR = os.getcwd()
BACKEND_DIR = ROOT_DIR + '/backend/'
FRONTEND_DIR = ROOT_DIR + '/frontend/'
CHATDATA_DIR = ROOT_DIR + '/chatdata/'

DATA_FILE = CHATDATA_DIR + 'movie_lines_pre_processed.tsv'  #_for_test.tsv'
PAGE_RANK_ANSWERS = CHATDATA_DIR + 'page_rank_answers.txt'
PAGE_RANK_QUESTIONS = CHATDATA_DIR + 'page_rank_questions.txt'
TOKENIZER_FILE = CHATDATA_DIR + 'tokenizer.pickle'

DEBUG_MODE = ['info']