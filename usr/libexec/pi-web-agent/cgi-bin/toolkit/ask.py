#!/usr/bin/python
from live_info import execute
import os, sys
import cgi

if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin')
from HTMLPageGenerator import composeJSONDocument

def find_answer(question):
    
    script = os.environ['MY_HOME'] + "/scripts/ask.py"
    output, err_code = execute(script + " " + question)
    json_dictionary = {'question':question, 'answer':output,\
                       'exit_code':err_code}
    
    composeJSONDocument(json_dictionary)
    
def main():
    
    fs = cgi.FieldStorage()
    if 'question' not in fs:
        composeJSONDocument({'question':"", 'answer':'No question asked',\
                       'exit_code':'0'})
        return
    question = fs['question'].value

    find_answer(question) 


if __name__ == '__main__':
    main()    
