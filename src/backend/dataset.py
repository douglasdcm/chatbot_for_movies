from settings import DATA_FILE, PAGE_RANK_QUESTIONS, PAGE_RANK_ANSWERS, TOKENIZER_FILE
import pandas as pd
import ast
import pickle


class Dataset:

	def import_dataset(self):
		return pd.read_csv(DATA_FILE, 
			delimiter="\t", quoting=3, encoding='ISO-8859-2')


	def get_questions(self, messages):
		return set(messages[messages['target'] == 1]['msg_pre_processed'].astype(str))


	def get_answers(self, messages):
		return set(messages[messages['target'] == 0]['msg_pre_processed'].astype(str))


	def get_page_compute(self, qea=0):

		pc = None
		file = None

		if qea == 0:
			file = PAGE_RANK_QUESTIONS
		else:
			file = PAGE_RANK_ANSWERS

		f = open(file, "r")
		pc = f.read()
		f.close()

		return ast.literal_eval(pc)


	def load_tokenizer(self):
		with open(TOKENIZER_FILE, 'rb') as handle:
		    tokenizer = pickle.load(handle)
		return tokenizer