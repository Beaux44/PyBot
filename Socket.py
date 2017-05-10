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


import socket

import string

from time import sleep as t

from Settings import *

# opens the socket to the Twitch IRC, used whenever a message is sent
def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("CAP REQ :twitch.tv/tags \r\n") # requests Twitch sends you more information.
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s

# Exits the chat room
def Exit():
	s = socket.socket()
	s.send("PART" + HOST)
	t(0.5)
	dednow()


# sends the specified message to the Twitch IRC
def sendMessage(s, message):
	if message == "": return
	messageTemp = "PRIVMSG #" + CHANNEL + str(message)
	s.send(messageTemp + "\r\n")
	print("Sent: " + str(message))
	return

# used to join the Twitch IRC chat room
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Hello :) /")

# defines when connected to the IRC
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
