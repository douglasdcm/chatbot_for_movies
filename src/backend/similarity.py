from sklearn.feature_extraction.text import CountVectorizer

class Similarity:

	def jaccard_similarity(self, f1, f2):		
		"""
		Return the similarity between the messages f1 and f2
		"""

		f1 = set(f1)
		f2 = set(f2)

		intersecao = f1.intersection(f2)
		uniao = f1.union(f2)

		return len(intersecao) / len(uniao)


	def return_conversation_by_jaccard(self, msg, res, questions, answers):
	    """
	    Return a dictionary of message and similarity sorted by highter similarity
	    """
	    if res >= 0.5:
	        msg_list = questions
	        similarity = [self.jaccard_similarity(msg, str(m)) for m in questions]     
	    else:
	        similarity = [self.jaccard_similarity(msg, str(m)) for m in answers]
	        msg_list = answers
	    
	    result = {} 
	    for key in msg_list: 
	        for value in similarity: 
	            result[key] = value
	            similarity.remove(value) 
	            break 
	    
	    return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
	    

	def get_the_next_conversation(self, conversations):
		"""
		Get the first item in the dict
		"""
		keys_view = conversations.keys()
		keys_iterator = iter(keys_view)
		conversation = next(keys_iterator)
		return conversation