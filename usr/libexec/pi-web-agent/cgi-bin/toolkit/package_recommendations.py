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
<<<<<<< HEAD
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
=======
PACKAGES_LIST_PATH=\
"/usr/libexec/pi-web-agent/etc/config/pm/recommendationsList.txt"
def checkBusy(view) :
    a, errorcode_apt_get = execute('pgrep apt-get')
    a, errorcode_aptitude = execute('pgrep aptitude')
    if errorcode_apt_get == 0 or errorcode_aptitude == 0 :
        view.setContent('Package Management',\
         'The package manager is busy right now. . . Try again later!' )
        view.output()
        return True
        
def checkFlags(text):
    lines = text.split('\n')
    del lines[-1]
    package_line = lines[-1]
    flags = package_line.split()[0]
    if flags.find('r') >= 0:
        return False
    return True
def main():
    '''
    Application to manage all the most used packages using apt-get.
    Unfinished.
    '''
    config=Configuration()
    view = View(config.system.actions)
    form = cgi.FieldStorage()
    if (checkBusy(view)):
        return
    sm=serviceManagerBuilder()
    

>>>>>>> upstream/master

  sm=serviceManagerBuilder()
  config=Configuration()
  view = View(config.system.actions)

<<<<<<< HEAD
  htmlcode = ''
  htmlcode += doAptGetUpdateIfNecessary()

  packages = []
  packages = readFileToList("recommendationsList.txt")

  allPackages = [[]]
  allPackages = buildPackageInformationToList( packages )

  htmlcode += HTML.table( allPackages, header_row=['Package Name', 'Status', 'Description', 'Version'] )
  htmlcode += DivManager.getOverlayProggressBarDiv()#used for the proggress bar
=======
    ins = open( PACKAGES_LIST_PATH, "r" )
    packages = []
    for line in ins:
      line = line.rstrip() # strip the new line
      packages.append( line )

    allPackages = [[]]
    
    for pName in packages :
        checkedText = createOnOffSwitch( pName )
        descriptionText = getDpkgInfo( pName, "Description" )
        versionText = getDpkgInfo( pName, "Version" )
        allPackages.append( [ pName, checkedText, descriptionText, versionText ] )
    
    htmlcode += "\n<div id='packages-table'>"
    htmlcode += HTML.table( allPackages, header_row=['Package Name', 'Status', 'Description', 'Version'] )
    htmlcode += "\n</div>"
>>>>>>> upstream/master

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
    bashCommand = "dpkg-query -l " + pName
    output, errorcode = execute( bashCommand )

    text = '<div class="on_off_switch">\n'
    text +='<input type="checkbox" name="'+pName+'" onclick="submit_package(this)" class="on_off_switch-checkbox" id="'+pName 
    if errorcode != 0:
        checkedText = text + '" checked>'
    elif errorcode == 0 and checkFlags(output):
        checkedText = text + '">'
    else:
        checkedText = text + '" checked>'
    checkedText += '<label class="on_off_switch-label" for="'+pName+'">\n'
    checkedText += '<div class="on_off_switch-inner"></div>\n'
    checkedText += '<div class="on_off_switch-switch"></div>\n'
    checkedText += '</label>\n'
    checkedText += '</div>\n'
    return checkedText

if __name__ == '__main__':
  main()

