#!/usr/bin/python
import sys
import os
import time
if 'MY_HOME' not in os.environ:
  os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin')
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin/chrome')
sys.path.append(os.environ['MY_HOME'] + '/etc/config')
from services import *
from view import *
from cern_vm import Configuration
import cgi
import cgitb
from subprocess import Popen, PIPE
import HTML
cgitb.enable()
from live_info import execute
from DivManager import *
from CommandLogger import *
'''
def checkError(view, errorcode) :
  if errorcode != 0 :
    view.setContent('Package Management', 'Something weird happened. . Try refreshing the page. .' )
    exit('Something weird happened')
'''
def main():
  '''
  Application to manage all the most used packages using apt-get.
  Unfinished.
  '''
  form = cgi.FieldStorage()

  sm=serviceManagerBuilder()
  config=Configuration()
  view = View(config.system.actions)

  htmlcode = ''
  htmlcode += doAptGetUpdateIfNecessary()

  packages = []
  packages = readFileToList("recommendationsList.txt")

  allPackages = [[]]
  allPackages = buildPackageInformationToList( packages )

  htmlcode += HTML.table( allPackages, header_row=['Package Name', 'Status', 'Description', 'Version'] )
  htmlcode += DivManager.getOverlayProggressBarDiv()#used for the proggress bar

  view.setContent('Package Management', htmlcode )
  view.output()

def doAptGetUpdateIfNecessary() :
  errorMessage = ''
  lastRecord = CommandLogger.readLastDateRecordLogOf( "apt-get update" )
  errorMessage += 'lastRecord = ' + str(lastRecord) + '.<br>'
  # dd/mm/yyyy format
  todayDate = (time.strftime( "%d/%m/%Y" ))
  errorMessage += 'todayDate = ' + str(todayDate) + '.<br>'
  if lastRecord != str( todayDate ) :
    errorMessage = CommandLogger.executeCommand("apt-get update")
  return errorMessage

def readFileToList( fileName ) :
  ins = open( fileName, "r" )
  packages = []
  for line in ins :
    line = line.rstrip() # strip the new line
    packages.append( line )
  return packages

def buildPackageInformationToList( packages ) :
  allPackages = [[]]  
  for pName in packages :
    checkedText = createOnOffSwitch( pName )
    descriptionText = getDpkgInfo( pName, "Description" )
    versionText = getDpkgInfo( pName, "Version" )
    allPackages.append( [ pName, checkedText, descriptionText, versionText ] )
  return allPackages

def getDpkgInfo(pName, fieldName) :
  bashCommand = "apt-query " + pName + " " + fieldName
  output, errorcode = execute( bashCommand )
  if output == "" :
    return fieldName + " not available"
  return output
        
def createOnOffSwitch( pName ) :
  checkedText = ""
  bashCommand = "dpkg-query -l | grep '" + pName + " '"
  output, errorcode = execute( bashCommand )
  #checkError(view, errorcode)

  text = '<div class="on_off_switch">\n'
  text +='<input type="checkbox" name="'+pName+'" onclick="submit_package(this)" class="on_off_switch-checkbox" id="'+pName 
  if output == "" :
    checkedText = text + '" checked>'
  else :
    checkedText = text + '">'
  checkedText += '<label class="on_off_switch-label" for="'+pName+'">\n'
  checkedText += '<div class="on_off_switch-inner"></div>\n'
  checkedText += '<div class="on_off_switch-switch"></div>\n'
  checkedText += '</label>\n'
  checkedText += '</div>\n'
  return checkedText

if __name__ == '__main__':
  main()

