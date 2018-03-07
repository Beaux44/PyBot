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
import sys
import socket
import string
from time import sleep as t
from Settings import *



try:
	_reload = sys.argv[1]
except IndexError:
	_reload = ""

# opens the socket to the Twitch IRC, used whenever a message is sent
def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(("PASS " + PASS + "\r\n").encode())
	s.send(("NICK " + NICK + "\r\n").encode())
	s.send(("CAP REQ :twitch.tv/tags\r\n").encode()) # requests Twitch send you more information
	s.send(("JOIN #" + CHANNEL + "\r\n").encode())
	return s

# Exits the chat room
def Exit(s, _codeFile, _pFN, _pL):
	s.send(("PART #" + HOST).encode())
	_codeFile.close()
	_POINTS_LIST_ = open(_pFN, "w")
	_POINTS_LIST_.write(str(_pL))
	_POINTS_LIST_.close()
	t(0.5)
	exit()

# sends the specified message to the Twitch IRC
def sendMessage(s, message):
	message = " ".join(str(message).split())
	if message:
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + str(message)
		s.send((messageTemp + "\r\n").encode())
		print("Sent:", message)

# used to join the Twitch IRC chat room
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = s.recv(1024)
		temp = readbuffer.decode().split("\n")
		readbuffer = temp.pop()

		for line in temp:
			if _reload == "":
				print(line)
			Loading = loadingComplete(line)
	if _reload == "":
		sendMessage(s, "Hello :) /")

# defines when connected to the IRC
def loadingComplete(line):
	return "End of /NAMES list" not in line
