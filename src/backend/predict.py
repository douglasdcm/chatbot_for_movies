from pre_processing import PreProcessing
from similarity import Similarity

class Prediction:

	def __init__(self, messages, model, questions: set, answers: set,
				 pc_questions: dict, pc_answers: dict, tokenizer):

		self.questions = questions
		self.answers = answers
		self.pc_questions = pc_questions
		self.pc_answers = pc_answers	
		self.tokenizer = tokenizer	
		self.model = model
		self.messages = messages
		self.pp = PreProcessing()		
		self.s = Similarity(questions=self.questions,
							answers=self.answers
							)


	def predict(self, msg):

		#print('Predicting next conversation.')
		msg = self.pp.pre_processing_text(msg)
		
		p = self.tokenizer.texts_to_matrix([msg])

		res = self.model.predict(p)

		if res >= 0.5:
			pc = self.pc_questions
		else:
			pc = self.pc_answers

		conversations = self.s.return_conversation_by_cossine(msg, res)

		conversations = self.s.return_conversation_by_page_rank(msg, conversations,
																page_compute=pc,
																reverse=True)		
		
		return self.s.get_the_next_conversation(conversations, self.messages)