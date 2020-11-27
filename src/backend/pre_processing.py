import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk.corpus import wordnet




class PreProcessing:
		
	def get_wordnet_pos(self, word):
	    """Map POS tag to first character lemmatize() accepts"""
	    tag = nltk.pos_tag([word])[0][1][0].upper()
	    tag_dict = {"J": wordnet.ADJ,
	                "N": wordnet.NOUN,
	                "V": wordnet.VERB,
	                "R": wordnet.ADV}

	    return tag_dict.get(tag, wordnet.NOUN)

	def __init__(self):
		self.lemmatizer = WordNetLemmatizer()

	def pre_processing_text(self, corpus):
	    #remove html tags
	    corpus = re.sub(r'<.*?>', '', str(corpus))
	    
	    #remove non-alphanumeric characters
	    corpus = re.sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
	    
	    #remove duplicated spaces
	    corpus = re.sub(r' +', ' ', str(corpus))
	    
	    #capitalization
	    corpus = corpus.lower()
	    
	    #tokenization
	    corpus = re.findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
	    
	    #lammatization
	    corpus = [self.lemmatizer.lemmatize(c, self.get_wordnet_pos(c)) for c in corpus]
	    
	    #remove punctuation
	    corpus = [t for t in corpus if t not in string.punctuation]
	    
	    #remove stopwords
	    #it makes the model worst
	    #stopwords_ = stopwords.words("english")
	    #corpus = [t for t in corpus if t not in stopwords_]
	    
	    corpus = ' '.join(corpus)

	    return corpus