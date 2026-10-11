#!/usr/bin/python
import sys
import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('wordnet')
from src.settings import ROOT_DIR

sys.path.append(ROOT_DIR + "/backend/")
sys.path.append(ROOT_DIR + "/frontend/")

from src.backend.chatbot import ChatBotInit

if __name__ == "__main__":
    cb = ChatBotInit()
    cb.init_chat_cmd()
