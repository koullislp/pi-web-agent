#!/usr/bin/python
import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin/chrome')
sys.path.append(os.environ['MY_HOME']+'/objects')
from live_info import execute
from services import *
from view import *
from cern_vm import Configuration
import cgi
import cgitb
from subprocess import Popen, PIPE
cgitb.enable()
from framework import output

def main():
    '''
Application for camera module
'''
    form = cgi.FieldStorage()
    
    sm=serviceManagerBuilder()
    config=Configuration()
    view = View(config.system.actions)
            
    f = open(os.environ['MY_HOME'] + '/html/camera_interface.html', 'r')
    html_interface= f.read()
    f.close()

    view.setContent('Camera Viewer', html_interface)
    output(view, cgi.FieldStorage())

if __name__ == '__main__':
    main()
