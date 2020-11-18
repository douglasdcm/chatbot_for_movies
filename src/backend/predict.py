import pickle
from pre_processing import PreProcessing
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from similarity import Similarity
from dataset import Dataset

class Prediction:

	def __init__(self, messages=None):
		if not messages:
			print('Loading brain...')

			ds = Dataset()

			self.messages = ds.import_dataset()
			self.questions = ds.get_questions(self.messages) #['why?', 'how?', 'when?']
			self.answers = ds.get_answers(self.messages) #['yes', 'no', 'maybe']
			print('Done.')

	def predict(self, msg):

		pp = PreProcessing()

		msg = pp.pre_processing_text(msg)

		# loading
		with open('tokenizer.pickle', 'rb') as handle:
		    tokenizer = pickle.load(handle)
		p = tokenizer.texts_to_matrix([msg])

		model = load_model('chatbot_model.h5')
		res = model.predict(p)

		s = Similarity()

		conversations = s.return_conversation_by_jaccard(msg, res, self.questions, self.answers)
		return s.get_the_next_conversation(conversations)