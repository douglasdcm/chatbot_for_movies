import math

from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
from src.backend.utils import naive_massage, save_content_to_log

from src.settings import *
from src.backend.pre_processing import PreProcessing


class Similarity:

    def __init__(self, questions: set, answers: set, word_vectors=None):

        self.bow = CountVectorizer()
        self.questions = questions
        self.answers = answers
        self.word_vectors = word_vectors
        self.pp = PreProcessing()

    def get_the_next_conversation(self, conversations, df):
        """
        Get the first item in the dict
        """

        keys_view = conversations.keys()
        keys_iterator = iter(keys_view)
        try:
            conversation = next(keys_iterator)
        except Exception as e:
            save_content_to_log(e)
            return naive_massage()

        return list(df[df["msg_pre_processed"] == conversation]["msg_2"])[0]

    def return_conversation_by_page_rank(self, msg, conversations, page_compute, reverse=True):
        """
        Return a dictionary of message and similarity sorted by highter similarity
        """

        conversations = self.pp.normalize_dictionary(conversations)

        conversations = {k: page_compute[k] + v for k, v in conversations.items()}

        return {
            k: v
            for k, v in sorted(conversations.items(), key=lambda item: item[1], reverse=reverse)
        }

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
            msg_bow = vector_bow[0].toarray().ravel()
            m_bow = vector_bow[1].toarray().ravel()

            # d1_array = (1, 1)

            # if m_bow.shape == d1_array and msg_bow.shape == d1_array:
            #     d = 1 - distance.euclidean(msg_bow, m_bow)
            # else:
            d = 1 - distance.cosine(msg_bow, m_bow)

            if math.isnan(float(d)):
                similarity.append(0.0)
            else:
                similarity.append(d)

        result = dict(zip(msg_list, similarity))

        return result
