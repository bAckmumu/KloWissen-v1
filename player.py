#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import smbus 
from subprocess import call
from subprocess import check_output
from time import sleep


bus = smbus.SMBus(1) 
sensorAddress = 0x70
chainPin = 24

chainOldValue = False
distanceOldValue = 120
isPlayingPodcast = False

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


def ReadChainSwitch():
    chainNewValue = GPIO.input(chainPin)
    if chainNewValue != chainOldValue:
        chainOldValue = chainNewValue
        return True
    else:
        return False

def ReadUltraSonicSensor():
    bus.write_byte_data(address, 0, 0x51)
    sleep(0.5)
    range1 = bus.read_byte_data(address, 2) 
    range2 = bus.read_byte_data(address, 3) 
    distanceNewValue = (range1 << 8) + range2
    
    print "ReadUltraSonicSensor: ", distance
    if distanceNewValue < distanceOldValue - 5 || distanceNewValue > distanceOldValue + 5 :
        "ReadUltraSonicSensor: has changed"
        distanceOldValue = distanceNewValue
        return True
    else:
        return False


def Main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chainPin, GPIO.IN)
    
    while True:
        if ReadChainSwitch():
            print "somebody pulls the chain"
            if isPlayingPodcast:
                MpdNext()
            else:
                PlayRadio()
        elif ReadUltraSonicSensor():
            print "somebody sits on the toilet"
            isPodcast = True
            PlayPodcast()
        #sleep(.5)
            


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

