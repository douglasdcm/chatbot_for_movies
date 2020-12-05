from settings import ROOT_DIR, EMERGENCY_MSG, NAIVE_MSG, LOG_FILE
import random
from datetime import datetime

def save_content_to_log(text: str):
    now = datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S") + ' --------------\n')
    print(text)

def save_content_to_log_file(text: str):
    file = open(LOG_FILE,'a') 

    now = datetime.now()
    file.write(now.strftime("%d/%m/%Y %H:%M:%S") + ' --------------\n')

    file.write( repr(text) )
    file.close()

def emergency_message():
	return random.choice(EMERGENCY_MSG)

def naive_massage():
	return random.choice(NAIVE_MSG)