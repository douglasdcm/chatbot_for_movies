from settings import ROOT_DIR, EMERGENCY_MSG, NAIVE_MSG, LOG_FILE
import random

def save_content_to_log(text: str):
    file = open(LOG_FILE,'a') 
    file.write('\n--------------\n')
    file.write( repr(text) )
    file.close()

def save_content_to_file(text: str, file):
    file = open(file,'a') 
    file.write('\n--------------\n')
    file.write( repr(text) )
    file.close()

def emergency_message():
	return random.choice(EMERGENCY_MSG)

def naive_massage():
	return random.choice(NAIVE_MSG)