import pandas as pd

class Dataset:

	def import_dataset(self):
		return pd.read_csv('./chatdata/movie_lines_pre_processed.tsv', 
			delimiter="\t", quoting=3, encoding='ISO-8859-2')


	def get_questions(self, messages):
		return set(messages[messages['target'] == 1]['msg_pre_processed'])


	def get_answers(self, messages):
		return set(messages[messages['target'] == 0]['msg_pre_processed'])