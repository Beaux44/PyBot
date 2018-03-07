# PyBot is a Twitch IRC chatbot used particularly for spamming your chat, but as well as a general chatbot for doing whatever.
# Copyright (C) 2016-2018 Sheep44
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


# NOTE: Move from username to user ID

import threading
from requests import request as req
from Settings import CHANNEL, PASS
from time import sleep as t
from os.path import isfile


_pointsList = {}
chatInfo = {}
_pointsFileName = "points/" + CHANNEL + ".json"
def points():
	global _pointsList
	global chatInfo
	justStarted = True
	if isfile(_pointsFileName):
		try:
			_pointsList = eval(open(_pointsFileName, 'r'))
		except:
			__ = open(_pointsFileName, 'w')
			__.close()
			del __
	while True:
		chatInfo = eval(
						req(
							method="GET",
							url="https://tmi.twitch.tv/group/user/%s/chatters" % CHANNEL
						).text
					)
		chatters = chatInfo["chatters"]
		if justStarted:
			justStarted = False
		else:
			for x in chatters:
				for i in chatInfo["chatters"][x]:
					if i in _pointsList.keys() and "bot" not in i:
						_pointsList[i] += 5
					elif "bot" not in i:
						_pointsList[i] = 5
			with open(_pointsFileName, 'w') as f:
				f.write(str(_pointsList))
				f.close()
		t(60)


thread = threading.Thread(target=points)
thread.daemon = True
thread.start()
