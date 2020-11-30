from predict import Prediction
from settings import CHATDATA_DIR
from dataset import Dataset
from tensorflow.keras.models import load_model
import gensim
from utils import save_content_to_log
import sys

class ChatBotInit:

	def __init__(self):		

		#TODO move to outside
		self.model_name = 'chatbot_model.h5'
		self.embedding_file = 'embedding_wiki_100d_pt.txt'
		self.ds = Dataset()
		self.messages = self.ds.import_dataset()
		self.questions = self.ds.get_questions(self.messages) #['why?', 'how?', 'when?, ...']
		self.answers = self.ds.get_answers(self.messages) #['yes', 'no', 'maybe', ...]
		self.model = load_model(CHATDATA_DIR + self.model_name)
		self.pc_questions = self.ds.get_page_compute(qea=1)
		self.pc_answers = self.ds.get_page_compute(qea=0)
		self.tokenizer = self.ds.load_tokenizer()
		self.p = Prediction(model=self.model,
							messages=self.messages,
							questions=self.questions,
							answers=self.answers,
							pc_questions=self.pc_questions,
							pc_answers=self.pc_answers,
							tokenizer=self.tokenizer
							)

	def init_chat_win(self, m):
		return str(self.p.predict(m))


	def init_chat_cmd(self, run_once = False):

		m = None
		you_prefix = '  You: '
		bot_prefix = '  Bot:  '
		exit = 'bye'

		print('I am ready to talk.')
		print(' Tip: You can type \"bye\" anytime to leave.')

		while(m != exit):
			#TODO save conversation to file_timestamp
			try:
				m = input(you_prefix)

				try:
					if m != 'bye':
						r = str(self.p.predict(m))
						print(bot_prefix + r)
				except Exception as e:
					print(bot_prefix + 'I cannot understand it. Try again, please!')
					save_content_to_log(e)

				if run_once == True:
					m = exit
			except KeyboardInterrupt:
				stored_exception=sys.exc_info()
				save_content_to_log(stored_exception)

		print(bot_prefix + 'Bye!')


