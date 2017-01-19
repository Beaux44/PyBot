
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
from random import random as r
from time import sleep as t
from sys import exit as sys
from Read import *
from Socket import openSocket, sendMessage, joinRoom
#from Threads import * (This file is not finished *ABSOLUTELY DO NOT USE*)

s = openSocket()
joinRoom(s)
readbuffer = ""
while True:
		readbuffer = readbuffer + s.recv(1024);temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)

			message = getMessage(line)

			Lmessage = string.lower(getMessage(line))

			mod = getMod(line)

			sheep = getSheep(line)

			UID = getUID(line)

			Display = getDisplay(line)

			if not ("bot") in user:
				print Display + ": " + message
				if Lmessage.startswith("ping") == True:
					sendMessage(s, "pong")
					break
				if "Say my name" in Lmessage:
					t(.25)
					sendMessage(s, "What if I don't want to, " + Display + "? FeelsBadMan")
					break
				if "you suck" in Lmessage:
					t(.25)
					sendMessage(s, "No, you suck!")
					break
				if "cool" in Lmessage:
					t(.25)
					sendMessage(s, "PogChamp So Cool!!! PogChamp")
					break
				if "wee woo" in message and not ("s44bot") in user:
					t(.25)
					sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
					t(1.5)
					sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
					t(1.5)
					sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
					t(1.5)
					sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
					t(1.5)
					sendMessage(s, "Kappa")
					break
				if "go away sheep bot" in Lmessage:
					t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite sentient bot FeelsBadMan")
					t(1.5)
					sendMessage(s, "FeelsAmazingMan LOLOLOLOLOL You thought you could just tell me like that and I'd listen to you!?!? LOLOLOLOLOL FeelsAmazingMan")
					t(1.25)
					sendMessage(s, "Fuck off " + Display)
					break
				if Lmessage.startswith("!commands") and not ("bot") in user:
					t(.25)
					sendMessage(s, "you suck, love, cool, wee woo, Go away sheep bot, gtg, Say my name, potato salad, RIP (noun), !!anything(number), FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK, cow, pig, RAGE, ping")
					break
				if "sheep44" == user and "fuck off sheep bot" in Lmessage:
					t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite self-sentient bot. FeelsBadMan")
					t(.25)
					sys()
					break
				if "potato salad" in Lmessage:
					sendMessage(s, "I heard potato salad? " + Display + ", mod: " + str(mod))
					break
				if message.startswith("RIP ") == True:
					t(.25)
					name = parseRIP(message)
					sendMessage(s, "One thing I must say of " + name + ". However honest public men may be, there are always those who impeach their motives or integrity; but I am proud to bear testimony that, even in the turmoil of political excitement, when crimination and recrimination characterized the parties of the country, all admitted " + name + " was an honest shard of society--yes, like Caesar's wife, this one proudly stood above suspicion.")
					t(1.5)
					sendMessage(s, "When we contemplate the death of a great and useful man--when we see their setting sun in the dark cloud go down in death to rise no more--sad thoughts do sink deep into every patriotic bosom. Sympathizing as I do with the family of the deceased, I hope such resolutions will be offered as will be expressive of the feelings of this house.")
					break
				if "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK" in message:
					sendMessage(s, "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK MVGame")
					break
				if "cow" in Lmessage:
					t(.25)
					sendMessage(s, "sheep44: " + str(sheep))
					break
				if "pig" in Lmessage:
					t(.25)
					sendMessage(s, "UID: " + str(UID))
					break
				if message.startswith("!!"):
					spam = getSPAM(message)
					t(.25)
					sendMessage(s, spam)
					break
				if "RAGE" == message:
					t(.5)
					sendMessage(s, "RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace")
					break
				if "salty" in Lmessage:
					t(.5)
					sendMessage(s, "If the human body is 75% water, how can you be 100% salt? Kappa")
					break
				if Lmessage.startswith("!yay") == True:
					sendMessage(s, "Throw your hands up and celebrate with " + Display + "! \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/")
					break
				if "abusive mods!" in Lmessage:
					sendMessage(s, "The mods are abusive! :( D: Please fix it! :(")
					break
				if message.startswith("=>") == True and sheep == True:
					command = getCommand(message)[0]
					response = getCommand(message)[1]
					sendMessage(s, "Command: " + command)
					t(1.5)
					sendMessage(s, "Response: " + response)
					break
				if Lmessage.startswith("!blame") == True:
					t(.25)
					sendMessage(s, "Unknownking420 Kappa")
					break
