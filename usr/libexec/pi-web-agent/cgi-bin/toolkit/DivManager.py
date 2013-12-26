#!/usr/bin/python
class DivManager() :
  @staticmethod
  def getTerminalDiv() :
    terminalStringDiv = open('terminalDiv.html', 'r').read()
    return terminalStringDiv
    
  @staticmethod    
  def getOverlayProggressBarDiv() :
    htmlOverlay ='<div id="overlay">\n' \
                            +'<div class="progress progress-striped active" '\
                              +'style ="width: 400px; height: 80px; margin: auto; margin-top: 80px">\n'\
                              +'<div class="progress-bar" role="progressbar" aria-valuenow="100" '\
                                +'aria-valuemin="0" aria-valuemax="100" style="width: 100%">\n'\
                                +'<span class="sr-only">100% Complete</span>\n'\
                              +'</div>\n'\
                            +'</div>\n'\
                          +'</div>\n'
    return htmlOverlay

  @staticmethod
  def createCustomOverlay(width_in, height_in) :
    htmlOverlay ='<div id="overlay">\n' \
                    +'<div class="progress progress-striped active" '\
                      +'style ="width: ' + width_in + 'px; height: ' + height_in + 'px; margin: auto; margin-top: 80px">\n'\
                      +'<div class="progress-bar" role="progressbar" aria-valuenow="100" '\
                        +'aria-valuemin="0" aria-valuemax="100" style="width: 100%">\n'\
                        +'<span class="sr-only">100% Complete</span>\n'\
                      +'</div>\n'\
                    +'</div>\n'\
                  +'</div>\n'
    return htmlOverlay

  @staticmethod
  def getStackTrace( output ) :
    terminalStringDiv = open('terminalDiv.html', 'r' ).read()
    locationToInputText = "<span id=\"end\""
    return terminalStringDiv.replace(locationToInputText, output + locationToInputText )

