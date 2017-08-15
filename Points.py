# PyBot is a Twitch IRC chatbot used particularly for spamming your chat, but as well as a general chatbot for doing whatever.
# Copyright (C) 2016 Sheep44
#
# This file is part of PyBot.
#
# PyBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# PyBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.



# This is an unfinished file and is not for use until it is patched up.
import threading
from Settings import CHANNEL
from time import sleep as t
import urllib.request
from os.path import isfile
printLock = threading.Lock()
_pointsList = {}
def points():
    justStarted = True
    global _pointsList
    _pointsFileName = "points_" + CHANNEL + ".json"
    if isfile(_pointsFileName):
        _pointsFileRead = open(_pointsFileName, 'r')
        _pointsList = eval(_pointsFileRead.read())
    while True:
        chatInfo = eval(urllib.request.urlopen("https://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters").read())
        chatters = chatInfo["chatters"]
        mods = chatters["moderators"]
        staff = chatters["staff"]
        admins = chatters["admins"]
        gMods = chatters["global_mods"]
        viewers = chatters["viewers"]
        if justStarted:
            justStarted = False
        else:
            for i in viewers:
                if i in _pointsList.keys():
                    _pointsList[i] += 5
                else:
                    _pointsList[i] = 0
            for i in mods:
                if i in _pointsList.keys():
                    _pointsList[i] += 5
                else:
                    _pointsList[i] = 0
            for i in staff:
                if i in _pointsList.keys():
                    _pointsList[i] += 5
                else:
                    _pointsList[i] = 0
            for i in admins:
                if i in _pointsList.keys():
                    _pointsList[i] += 5
                else:
                    _pointsList[i] = 0
            for i in gMods:
                if i in _pointsList.keys():
                    _pointsList[i] += 5
                else:
                    _pointsList[i] = 0

            _pointsFileWrite = open(_pointsFileName, 'w')
            _pointsFileWrite.write(str(_pointsList))
        t(60)


thread = threading.Thread(target=points)
thread.daemon = True
thread.start()
