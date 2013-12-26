#!/usr/bin/python
from live_info import execute
from DivManager import *
import time
class CommandLogger() :
  @staticmethod
  def executeCommand( command ) :
    errorMessage = ''
    output, errorcode = execute( command )
    if errorcode != 0 :
      #TODO We need something here to display the stack trace... maybe a terminal css
      # use terminal css to display error in an overlay
      errorMessage += DivManager.getStackTrace( output + "<br>ErrorCode: " + str( errorcode ) )
    #date, command, errorcode
    todayDate = (time.strftime( "%d/%m/%Y" ))
    output, errorcode = execute( "sudo echo '" + todayDate + ", \"" + command + "\", " + str( errorcode ) + "' >> dateCommandErrorLog.csv" )
    return errorMessage

  @staticmethod
  def readLastDateRecordLogOf( command ) :
    ins = open( "dateCommandErrorLog.csv", "r" )
    line = ''
    lastRecordOf = []
    for line in ins : 
      record = line.split(',')
      if record[1] == command :
        lastRecordOf = record
    ins.close( )
    if len(lastRecordOf) > 0 :
      return lastRecordOf[0]
    return None
