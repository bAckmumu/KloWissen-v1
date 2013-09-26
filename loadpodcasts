#!/usr/bin/python2.7

from subprocess import call
from time import sleep

def DownloadPodcasts():
    print "update podcast list"
    call(["gpo", "update"])

    print "download podcast list"
    call(["gpo", "download"])

    print "update music lib"
    call(["mpc", "update"])
    
DownloadPodcasts()
