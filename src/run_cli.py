#!/usr/bin/python
import os, sys
from settings import ROOT_DIR
sys.path.append(ROOT_DIR + '/backend/')
sys.path.append(ROOT_DIR + '/frontend/')

from backend.chatbot import ChatBotInit

if __name__ == "__main__":
	cb = ChatBotInit()
	cb.init_chat_cmd()