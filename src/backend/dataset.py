from settings import DATA_FILE, PAGE_RANK_QUESTIONS, PAGE_RANK_ANSWERS, TOKENIZER_FILE
import pandas as pd
import ast
import pickle
from pre_processing import PreProcessing


class Dataset:

    def __init__(self):
        self.pp = PreProcessing()

    def import_dataset(self):
        messages = pd.read_csv(DATA_FILE, delimiter="\t", quoting=3, encoding="ISO-8859-2")
        messages.columns = ['msg_line', 'user_id', 'movie_id', 'msg', 'msg_pre_processed', 'msg_2', 'target']
        return messages

    def get_questions(self, messages):
        return set(messages[messages["target"] == 1]["msg_pre_processed"].astype(str))

    def get_answers(self, messages):
        return set(messages[messages["target"] == 0]["msg_pre_processed"].astype(str))

    def get_page_compute(self, qea=0):

        pc = None
        file = None

        if qea == 0:
            file = PAGE_RANK_ANSWERS
        else:
            file = PAGE_RANK_QUESTIONS
            
        pc = self.pp.pre_processing_page_rank_file(file)

        return self.pp.normalize_dictionary(pc)

    def load_tokenizer(self):
        with open(TOKENIZER_FILE, "rb") as handle:
            tokenizer = pickle.load(handle)
        return tokenizer
