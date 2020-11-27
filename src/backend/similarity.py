from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance
import math
from utils import save_content_to_log
from settings import * 
import numpy as np

class Similarity:

	def __init__(self, questions: set, answers: set, word_vectors=None):

		self.bow = CountVectorizer()
		self.questions = questions
		self.answers = answers
		self.word_vectors = word_vectors


	def calculate_embedding(self, phrase):
		"""
		Return the mean of embeddings of a phrase
		"""
		
		arr = np.array([self.word_vectors[word] for word in phrase 
							if word in self.word_vectors.vocab])
		
		sum = np.zeros(len(arr[0]))
		for a in arr:
			sum = sum + a

		arr_mean = sum / len(arr) 
	    
		return arr_mean


	def return_conversation_by_cossine_embedding(self, msg, res):
		"""
		Return a dictionary of message and similarity sorted by highter similarity
		"""
		if res >= 0.5:
			msg_list = self.questions
		else:
			msg_list = self.answers       
	    
		msg = msg.split(' ')
	    
		similarity = []
		for m in msg_list:
			m = m.split(' ')		
	        
			try:
				msg_vector_embedding = self.calculate_embedding(msg)
				m_vector_embedding   = self.calculate_embedding(m)
	        
				similarity.append(distance.cosine(msg_vector_embedding, m_vector_embedding))
			except:
				if 'trace' in DEBUG_MODE:
					save_content_to_log("An exception occurred")
					save_content_to_log('> '+ ' '.join(m))
	    
		result = {} 
		for key in msg_list: 
			for value in similarity: 
				result[key] = value
				similarity.remove(value)
				break
	    
		return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=False)}
	    

	def jaccard_similarity(self, f1, f2):	
		"""
		Return the similarity between the messages f1 and f2
		"""

		#save_content_to_log('Calculating Jaccard Similarity.')	

		f1 = set(f1.split(' '))
		f2 = set(f2.split(' '))

		intersecao = f1.intersection(f2)
		uniao = f1.union(f2)

		return len(intersecao) / len(uniao)


	def return_conversation_by_jaccard(self, msg, res):
	    """
	    Return a dictionary of message and similarity sorted by highter similarity
	    """

	    save_content_to_log('Returning conversation by Jaccard Similarity.')

	    if res >= 0.5:
	        msg_list = self.questions
	        similarity = [self.jaccard_similarity(msg, str(m)) for m in self.questions]     
	    else:
	        similarity = [self.jaccard_similarity(msg, str(m)) for m in self.answers]
	        msg_list = self.answers
	    
	    result = {} 
	    for key in msg_list: 
	        for value in similarity: 
	            result[key] = value
	            similarity.remove(value) 
	            break 
	    
	    return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
	    

	def get_the_next_conversation(self, conversations, df):
		"""
		Get the first item in the dict
		"""
		save_content_to_log('Geting the next conversation.')

		keys_view = conversations.keys()
		keys_iterator = iter(keys_view)
		conversation = next(keys_iterator)

		return list(df[df['msg_pre_processed'] == conversation]['msg_2'])[0]


	def normalize_dictionary(self, dic):

		zero_dict = {k: 0.0 for k, v in dic.items()}

		for v in dic.values():
			if not isinstance(v, np.floating):
				return zero_dict

		den = math.fsum(dic.values())

		if den == 0:
			return zero_dict
		
		factor = 1.0 / den
		return {k: (v * factor) for k, v in dic.items()}


	def return_conversation_by_page_rank(self, msg, conversations, page_compute, reverse=True):		
		"""
		Return a dictionary of message and similarity sorted by highter similarity
		"""
		#similarity = [jaccard_similarity(msg, str(m)) for m in questions]  

		save_content_to_log('Returning conversations by Jaccard Similarity based on Page Rank.')
		
		result = self.normalize_dictionary(conversations)

		result = {k: page_compute[k] + v for k, v in result.items()}

		return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=reverse)}


	def return_conversation_by_cossine(self, msg, res):
		"""
		Return a dictionary of message and similarity sorted by highter similarity
		"""
		if res >= 0.5:
			msg_list = self.questions
		else:
			msg_list = self.answers

		similarity = []
		for m in msg_list:
			m = str(m)
			new_msg_list = [msg, m]
			vector_bow = self.bow.fit_transform(new_msg_list)
			msg_bow = vector_bow.todense()[0]
			m_bow   = vector_bow.todense()[1]

			d1_array = (1, 1)

			if m_bow.shape == d1_array and msg_bow.shape == d1_array:
				d = 1 - distance.euclidean(msg_bow, m_bow)
			else:
				d = 1 - distance.cosine(msg_bow, m_bow)

			if math.isnan(float(d)):
				similarity.append(0.0)
			else:
				similarity.append(d)

		result = {}
		for key in msg_list:
			for value in similarity:
				result[key] = value
				similarity.remove(value)
				break

		return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=False)}
	    
 