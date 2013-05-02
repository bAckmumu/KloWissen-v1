#!/usr/bin/python2.7

import os
import datetime

def DeleteOldFiles( path, age ):
    print "deleting, path: ", path
    for dirpath, dirname, filenames in os.walk(path):
        for old_file in filenames:
            curpath = os.path.join(dirpath, old_file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(hours=age):
                os.remove(curpath)

def CleanPodcastDir():
    DeleteOldFiles( "/home/pi/podcast/Nachrichten", 1 )
    DeleteOldFiles( "/home/pi/podcast/Hoersuppe", 24 )
    DeleteOldFiles( "/home/pi/podcast/Ombudsmann", 24 )
    DeleteOldFiles( "/home/pi/podcast/Mahlzeit", 24 )
    DeleteOldFiles( "/home/pi/podcast/ScienceBusters", 24 )

CleanPodcastDir()
