from settings import ROOT_DIR

def save_content_to_log(text: str):
    file = open(ROOT_DIR + 'log.txt','a') 
    file.write('\n--------------\n')
    file.write( repr(text) )
    file.close()