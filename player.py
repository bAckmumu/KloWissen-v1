#!/usr/bin/python2.7

import RPi.GPIO as GPIO
from subprocess import call
from subprocess import check_output
from time import sleep


def MpdStop():
    print "MpdStop"
    call(["mpc", "stop"])

def MpdPlay():
    print "MpdPlay"
    call(["mpc", "play"])

def MpdNext():
    print "MpdNext"
    call(["mpc", "next"])

def MpdAdd( file ):
    print "MpdAdd: ", file
    call(["mpc", "clear"])
    call(["mpc", "add", file])

def MpdState():
    state = check_output(["mpc"])
    print "MpdState: ", state 
    if state.find("[playing]") == -1:
        print "MpdState: ", False
        return False
    else:
        print "MpdState: ", True
        return True


def PlayRadio():
    if MpdState():
        MpdStop()
    else:
        MpdAdd("http://detektor.fm/stream/aac/musik/")
        MpdPlay()
        
def PlayPodcast():
    if MpdState() == False:
        call(["mpc", "listall"])
        MpdAdd("/")
        MpdPlay()


def Main():
    chainPin = 24
    chainValueOld = False
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chainPin, GPIO.IN)
    
    while True:
        chainValueNew = GPIO.input(chainPin)
        if (chainValueNew != chainValueOld):
            PlayRadio()
            chainValueOld = chainValueNew
        sleep(.5)
            


# def Main():
#     isPodcast = False
#     while True:
#         if( serialFromArduino.inWaiting() > 0 ):
#             input = serialFromArduino.read( 1 )

#             inputValue = ord( input )
#             print "serial value from arduino: ", inputValue

#             #if inputValue == 0:
#                 #StopMpd()
#             if inputValue == 1:
#                 print "somebody pulls the chain"
#                 if isPodcast:
#                     MpdNext()
#                 else:
#                     PlayRadio()
#             elif inputValue == 2:
#                 print "somebody leafs the toilet"
#                 isPodcast = False
#             elif inputValue == 3:
#                 print "somebody sits on the toilet"
#                 isPodcast = True
#                 PlayPodcast()
#             else:
#                 print "error invalide inputValue: ", inputValue
                
#         sleep(.5)


Main()

