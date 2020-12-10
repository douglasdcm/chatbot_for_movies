from predict import Prediction
from settings import CHATDATA_DIR, BOT_PREFIX, YOU_PREFIX
from dataset import Dataset
from tensorflow.keras.models import load_model
from utils import save_content_to_log, emergency_message, save_content_to_log_file
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

	def init_chat_cmd(self, run_once = False):

		m = None
		exit = 'exit'

		print('I am ready to talk.')
		print(' Tip: You can type \"exit\" (lowercase) anytime to leave.')

		while(m != exit):
			#TODO save conversation to file_timestamp
			try:
				m = input(YOU_PREFIX)
				save_content_to_log_file(YOU_PREFIX + str(m))

			except KeyboardInterrupt:
				print(BOT_PREFIX + emergency_message())
				save_content_to_log(sys.exc_info())				

			if m != exit:
				r = str(self.p.predict(m))
				print(BOT_PREFIX + r)
				save_content_to_log_file(BOT_PREFIX + str(r))

			if run_once == True:
				m = exit

		print(BOT_PREFIX + 'Bye!')

	def get_conversation(self, message):
		return str(self.p.predict(message))


