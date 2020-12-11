import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk.corpus import wordnet
import numpy as np
import math


class PreProcessing:
    def get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV,
        }

        return tag_dict.get(tag, wordnet.NOUN)

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def pre_processing_text_for_similarity(self, corpus):
        #remove html tags
        corpus = re.sub(r'<.*?>', '', str(corpus))
        
        #remove non-alphanumeric characters
        corpus = re.sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
        
        #remove duplicated spaces
        corpus = re.sub(r' +', ' ', str(corpus))

        #remove numbers
        corpus = re.sub("\d+", "", corpus)
        
        #capitalization
        corpus = corpus.lower()
        
        #tokenization
        corpus = re.findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
        
        #lammatization
        corpus = [self.lemmatizer.lemmatize(c, self.get_wordnet_pos(c)) for c in corpus]
        
        #remove punctuation
        corpus = [t for t in corpus if t not in string.punctuation]

        #remove stopwords
        stopwords_ = stopwords.words("english")
        corpus = [t for t in corpus if t not in stopwords_]
        
        corpus = ' '.join(corpus)

        return corpus

    def pre_processing_text_for_neural_network(self, corpus):
        #remove html tags
        corpus = re.sub(r'<.*?>', '', str(corpus))
        
        #remove non-alphanumeric characters
        corpus = re.sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
        
        #remove duplicated spaces
        corpus = re.sub(r' +', ' ', str(corpus))

        #remove numbers
        corpus = re.sub("\d+", "", corpus)
        
        #capitalization
        corpus = corpus.lower()
        
        #tokenization
        corpus = re.findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
        
        #lammatization
        corpus = [self.lemmatizer.lemmatize(c, self.get_wordnet_pos(c)) for c in corpus]
        
        #remove punctuation
        corpus = [t for t in corpus if t not in string.punctuation]
        
        corpus = ' '.join(corpus)

        return corpus

    def pre_processing_page_rank_file(self, file):
        f = open(file, "r")
        pc = f.read()

        pc = pc.replace('}','')
        pc = pc.replace('{','')
        pc = pc.replace('\'','')
        pc = pc.split(', ')

        f.close()


        d = dict()
        for line in pc:
        	(key, val) = line.split(': ')
        	d[key] = float(val)

        return d

    def normalize_dictionary(self, dic):

        zero_dict = {k: 0.0 for k, v in dic.items() if not isinstance(v, np.floating) }

        for v in dic.values():
            if not isinstance(v, np.floating):
                return zero_dict

        den = math.fsum(dic.values())

        if den == 0:
            return zero_dict
        
        factor = 1.0 / den

        return {k: (v * factor) for k, v in dic.items()}