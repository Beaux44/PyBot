#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from Settings import CHANNEL
from time import sleep as _t

_commands = eval(open("commands/" + CHANNEL + ".json", 'w+').read() or "{}")

# Gets the username, without capitals, can be used for detecting if a particular whatever is in the username.
def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

# Gets the message (It's that simple!)
def getMessage(line):
	try:
		message = line.split("PRIVMSG #" + CHANNEL + " :", 1)[1]
	except:
		message = ""
	return message or None

# This is used for the RIP command in run.py, you can read it if you want, I don't care
def parseRIP(message):
	seperate = message.split(' ', 1)[1]
	name = seperate.split(':', 1)[0]
	return name

# returns whether the person is a mod
def getMod(line):
	if not line.startswith('@'):
		return False
	seperate = line.split()[0]
	index = seperate.find('mod=')
	return seperate[index+4] == '1'

# This returns the User id, it can be used to specify commands to a particular person, like I did with getNoot()
def getUID(line):
	if not line.startswith("@"):
		return ''
	index = line.find('user-id')
	if index < 0: return ''
	line = line[index + 8: (len(line) - 8)]
	index = line.find(';')
	if ((line.find(' ') < index) or (index < 0)): index = line.find(' ')
	return line[0: index]

# I kind of just added this for myself, It just checks to see if the user is me
def getNoot(line):
	if not line.startswith("@"):
		return False
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
	if message == "=>":
		print('Syntax error')
		return ''
	index = message[2:-1].strip()
	if index == "":
		print('Syntax error')
		return ''
	index = index.rsplit("(", 1)
	try:
		if index[0] == "": return ''
		if index[1] == "": return ''
	except IndexError:
		print('Syntax error')
		return ''
	word = index[0] + " "
	number = index[1]
	try:
		spam = word * int(number)
	except (TypeError, ValueError, OverflowError, MemoryError):
		print('Syntax error')
		return ''
	_t(.1)
	return spam

# This is unfinished, however, in the future will be used to add commands.
def addCommand(message):
	global _commands
	index = message[2:-1]
	index = index.split("(", 1)
	name = index[0].strip(" (!")
	response = index[1].strip()

	with open("commands/" + CHANNEL + ".json", 'w+') as o:
		_commands[name] = response
		o.write(str(_commands))
		o.close()
	return

def delCommand(message):
	global _commands
	name = message[2:].strip(" (!")
	o = open("commands/" + CHANNEL + ".json", 'w+')
	del _commands[name]
	o.write(str(_commands))
	o.close()
	return

def runCommand(Lmessage,
				line=None,
 				display=None,
				user=None,
				mod=None,
				ishost=None,
				noot=None,
				UID=None,
				channel=None):
		cmd = Lmessage[1:]
		if cmd in _commands.keys():
			return _commands[cmd].format(
										**{'line':line,
											'display':display,
											'user':user,
											'Lmessage':Lmessage,
											'mod':mod,
											'ishost':ishost,
											'noot':noot,
											'UID':UID,
											'channel':CHANNEL
										}
			)
		else:
			return "Command not recognized."

def getRequest(Display, message):
	o = open("Requests.txt", "a")
	a = ""
	for i in message:
		a += i if ord(i) < 128 else "~"
	o.write(Display + ": " + a[8:] + "\n")
	o.close()
	return
