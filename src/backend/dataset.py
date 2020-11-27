import pandas as pd
from settings import CHATDATA_DIR

class Dataset:

	def import_dataset(self):
		return pd.read_csv(CHATDATA_DIR + 'movie_lines_pre_processed_for_test.tsv', 
			delimiter="\t", quoting=3, encoding='ISO-8859-2')


	def get_questions(self, messages):
		return set(messages[messages['target'] == 1]['msg_pre_processed'].astype(str))


	def get_answers(self, messages):
		return set(messages[messages['target'] == 0]['msg_pre_processed'].astype(str))


	def get_page_compute(self, qea=0):

		pc = None
		file = None

		if qea == 0:
			file = CHATDATA_DIR + 'page_rank_answers.txt'
		else:
			file = CHATDATA_DIR + 'page_rank_questions.txt'

		f = open(file, "r")
		pc = f.read()
		f.close()

		return ast.literal_eval(pc)


	def load_tokenizer(self):
		with open(CHATDATA_DIR + 'tokenizer.pickle', 'rb') as handle:
		    tokenizer = pickle.load(handle)
		return tokenizer