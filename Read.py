#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
#
# You should have received a copy of the GNU General Public License
# along with PyBot.  If not, see <http://www.gnu.org/licenses/>.


import string

from Settings import CHANNEL

from time import sleep as t

# Gets the username, without capitals, can be used for detecting if a particular whatever is in the username.
def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

# Gets the message (It's that simple!)
def getMessage(line):
	message = line.split("PRIVMSG #" + CHANNEL + " :", 1)[1]
	return message

# This is used for the RIP command in run.py, you can read it if you want, I don't care
def parseRIP(message):
	seperate = message.split(' ', 1)[1]
	name = seperate.split(':', 1)[0]
	return name

# returns wheter the person is a mod
def getMod(line):
	if not line.startswith('@'): return False
	seperate = line.split(' ')[0]
	index = seperate.find('mod=')
	return seperate[index+4] == '1'

# This returns the User id, it can be used to specify commands to a particular person, like I did with getSheep()
def getUID(line):
	if not line.startswith("@"): return ''
	index = line.find('user-id')
	if index < 0: return ''
	line = line[index + 8: (len(line) - 8)]
	index = line.find(';')
	if ((line.find(' ') < index) or (index < 0)): index = line.find(' ')
	return line[0: index]

# I add kind of just added this for myself, It just checks to see if the user is me
def getSheep(line):
	if not line.startswith("@"): return False
	index = line.find('user-id')
	if index < 0: return ''
	line = line[index + 8: (len(line) - 8)]
	index = line.find(';')
	if ((line.find(' ') < index) or (index < 0)): index = line.find(' ')
	return line[0: index] == '56857526'

# This gets the display name of the user, e.g. sheep44 = user, Sheep44 = display; just used to send messages
def getDisplay(line):
	if not line.startswith("@"): return ''
	index = line.find('display-name')
	if index < 0: return user
	line = line[index + 13: (len(line) - 8)]
	index = line.find(';')
	if ((line.find(' ') < index) or (index < 0)): index = line.find(' ')
	return line[0: index]

# This exists for the sole purpose of spamming your chat, you might want to disable it, I don't know.
def getSPAM(message):
	if message == "!!": print 'Syntax error'; return''
	message = message.strip()
	index = message[2:-1]
	if index == "": print 'Syntax error'; return ''
	index = index.split("(", 1)
	try:
		if index[0] == "": return ''
		if index[1] == "": return ''
	except IndexError:
		print 'Syntax error'; return ''
	word = index[0] + " "
	number = index[1]
	try:
		spam = word * int(number)
	except (TypeError, ValueError, OverflowError):
		print 'Syntax error'; return ''
	t(.1)
	return spam

# This is unfinished, however, in the future wil be used to add commands.
def getCommand(message):
		message = message.strip()
		index = message[3:-1]
		index = index.split("(", 1)
		index[0] = index[0][:-1]
		# o = open(commands.dat, 'w')
		# o.write("				if message.startswith(\"!" + index[0] + "\"):\n")
		# o.write("					t(.75)\n")
		# o.write("					sendMessage(s, \"" + index[1] + "\")\n")
		# o.write("					break\n")
		# o.close()
		return index
def getRequest(Display, message):
	o = open("Requests.txt", a)
	o.write(Display + ": " + message[8:])
	o.close()
