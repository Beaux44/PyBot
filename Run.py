# !/usr/bin/env python
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

import random
_r =  random.choice
import math
math.phi = (1 + 5**.5) / 2
import time
_t = time.sleep
from Read import *
from Socket import openSocket, sendMessage, joinRoom, Exit
from Settings import CHANNEL, NICK
import Points
_startTime = time.time()

# Load last saved environment
_codeFileName = "code_" + CHANNEL + ".py"
try:
	_codeFile = open(_codeFileName, 'r')
except:
	_codeFile = open(_codeFileName, 'w')
	_codeFile = open(_codeFileName, 'r')

try:
	exec(_codeFile.read())
except Exception as e:
	print(type(e).__name__, *e.args, sep = "\n")
_codeFile = open(_codeFileName, 'a')
# Load last saved environment

# Remove last saved environment
def delEnv():
	global _codeFile
	_codeFile = open(_codeFileName, 'w')
	return "Successfully Deleted"
# Remove last saved environment

Memes = [
	"~~~~~~~[]=¤ԅ( ◔益◔ )ᕗ The longer you cage us, the harder our arm of righteous spam will smite thee! ~~~~~~~[]=¤ԅ( ◔益◔ )ᕗ",
	"୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨ ୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨ ୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨",
	"Europe was founded in 1848 by Walker Texas Ranger when he rode a horse across the Atlantic, he called it \"Eastern USA\" which was eventually abbreviated as just \"EU\"",
	"———————————————————————— imGlitch You have been gifted the Golden Kappa!————————————————————————",
	"PogChamp PogChamp HOLD CTRL AND TYPE \"WTF\" FOR ℱ𝓪𝓷𝓬𝔂 𝓦𝓣ℱ PogChamp PogChamp",
	"ヽ༼ ͠ ͠°〜 ͜ʖ〜 ͠ ͠° ༽ﾉ¤=[———— Hello. My name is Inigo Dongtoya. You killed my Kappa. Prepare to die.",
	"MrDestructoid ban MrDestructoid one MrDestructoid bot MrDestructoid manufacture MrDestructoid another MrDestructoid",
	"MrDestructoid ME BOT MrDestructoid ME SPAM MrDestructoid NO VIEWERS MrDestructoid IF BAN MrDestructoid",
	"FeelsBadMan THIS USED TO BE A 2016 STREAM FeelsBadMan THIS USED TO BE A 2016 STREAM FeelsBadMan",
	"୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨",
	"Hello I am Ka­ppa Ka­pparino. I'm an employee at Twitch and am currently testing changes to the Ka­ppa emote. Can you please type Ka­ppa to confirm that it's working?",
	"My Ka­ppa privileges have been revoked. FeelsBadMan",
	"~~~~~~~[]=¤ԅ[✖Ĺ̯ಠ]╯ AND NOW WE MUTINY! ~~~~~~~[]=¤ԅ[✖Ĺ̯ಠ]/",
	"( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ clickty clack clickty clack with this chant I summon spam to the chat ( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ",
	"Tᴏ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ғʀᴏᴍ ᴅᴇᴠᴀsᴛᴀᴛɪᴏɴ. ᴛᴏ ᴜɴɪᴛᴇ ᴀʟʟ sᴘᴀᴍᴍᴇʀs ᴡɪᴛʜɪɴ ᴏᴜʀ ɴᴀᴛɪᴏɴ. ᴛᴏ ᴅᴇɴᴏᴜɴᴄᴇ ᴛʜᴇ ᴇᴠɪʟ ᴏғ Tʀᴜᴍᴘ ᴀɴᴅ ᴍᴏᴅs. ᴛᴏ ᴇxᴛᴇɴᴅ ᴏᴜʀ sᴘᴀᴍ ᴛᴏ ᴛʜᴇ sᴛᴀʀs ᴀʙᴏᴠᴇ. ᴄᴏᴘʏ! ᴘᴀsᴛᴇ! ᴄʜᴀᴛ sᴘᴀᴍ ʙʟᴀsᴛ ᴏғғ ᴀᴛ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ʟɪɢʜᴛ! sᴜʀʀᴇɴᴅᴇʀ ᴍᴏᴅs ᴏʀ ᴘʀᴇᴘᴀʀᴇ ᴛᴏ ғɪɢʜᴛ.",
	"H ＥＬＬＯ ＡＭ ４８ ＹＥＡＲ ＭＡＮ ＦＲＯＭ ＳＯＭＡＬＩＡ． ＳＯＲＲＹ ＦＯＲ ＢＡＤ ＥＮＧＬＡＮＤ． Ｉ ＳＥＬＬＥＤ ＭＹ ＷＩＦＥ ＦＯＲ ＩＮＴＥＲＮＥＴ ＣＯＮＮＥＣＴＩＯＮ ＦＯＲ ＰＬＡＹ ＂ｈｅａｒｔｈ ｓｔｏｎｅ＂ ＡＮＤ Ｉ ＷＡＮＴ ＴＯ ＢＥＣＯＭＥ ＴＨＥ ＧＯＯＤＥＳＴ ＰＬＡＹＥＲ ＬＩＫＥ ＹＯ U",
	"° ☾ ☆ ¸. ¸ 　★　 :.　 . • ○ ° ★　 .　 　.　.　　¸ .　　 ° 　¸. * ● ¸ .　...somewhere　　　° ☾ ° 　¸. ● ¸ .　　★　° :.　 . • ° 　 .　 *　:.　.in a parallel universe ● ¸ 　　　　° ☾ °☆ 　. * ¸.　　　★　★ ° . .　　　　.　☾ °☆ 　. * ● chat loves spam...° ☾　★ °● ¸ .　　　★　° :.　 . • ",
	"I AM LORD KAPPA. ._.",
	"(╯°□°)╯︵┻━┻                                                     ┬─┬﻿ ノ( ゜-゜ノ) ",
	"╲⎝⧹╲⎝⧹ WutFace ⧸⎠╱⧸⎠╱",
]

s = openSocket()
joinRoom(s)
readbuffer = ""
_numberOfTimesLooped = 0
_lastUsed = time.time()
_lastTimeLooped = time.time()

while True:
	_currentTime = time.time()
	if _currentTime - _lastTimeLooped < 0.5:
		_numberOfTimesLooped += 1
	else:
		_numberOfTimesLooped = 0
	if _numberOfTimesLooped >= 25:
		print("Error, exiting")
		exit()
	_lastTimeLooped = time.time()

	#try:
	readbuffer = s.recv(1024)
	readbuffer = readbuffer.decode()
	temp = readbuffer.split("\n")
	readbuffer = readbuffer.encode()
	readbuffer = temp.pop()

	for line in temp:
		# if int((_currentTime - _startTime)) % 15 == 0 and (_currentTime - _lastUsed) > 3:
		# 	sendMessage(s, "Test event")
		# 	_lastUsed = time.time()
		if "PING :tmi.twitch.tv" == line.strip():
			s.send("PONG :tmi.twitch.tv\r".encode())
			print(line)
			print("PONG :tmi.twitch.tv")
			break
		else:
			Display = getDisplay(line)

			user = getUser(line)

			message = getMessage(line).strip()

			Lmessage = message.lower()

			mod = getMod(line)

			ishost = (user == CHANNEL)

			sheep = getSheep(line)

			UID = getUID(line)

			if "bot" not in user:
				print(Display + ": " + message)
				_o = open("chat.txt", 'a')
				_u = ""
				for i in message:
					_u += i if ord(i) < 128 else "~"
				_o.write(Display + ": " + _u + "\r\n")
				_o.close()
				if "sheep44" == user and "go away sheep bot" in Lmessage:
					_t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite self-sentient bot. FeelsBadMan")
					_t(.50)
					Exit(s)
					break
				if "!ping" == Lmessage:
					sendMessage(s, "pong")
					break
				if "say my name" == Lmessage:
					_t(.25)
					sendMessage(s, "What if I don't want to, " + Display + "? FeelsBadMan")
					break
				if "go away sheep bot" == Lmessage:
					_t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite sentient bot FeelsBadMan")
					_t(1.5)
					sendMessage(s, "FeelsAmazingMan LOLOLOLOLOL You thought you could just tell me like that and I'd listen to you!?!? LOLOLOLOLOL FeelsAmazingMan")
					_t(1.25)
					sendMessage(s, "Fuck off " + Display)
					break
				if "!commands" == Lmessage:
					_t(.25)
					sendMessage(s, "wee woo, go away sheep bot, Say my name, potato salad, RIP (noun), =>anything(number), FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK, !uid, !sheep, RAGE, !ping, !request")
					break
				if "potato salad" in Lmessage:
					sendMessage(s, "I heard potato salad? " + Display + ", mod: " + str(mod))
					break
				if message.startswith("RIP "):
					_t(.25)
					name = parseRIP(message)
					sendMessage(s, "One thing I must say of " + name + ". However honest public men may be, there are always those who impeach their motives or integrity; but I am proud to bear testimony that, even in the turmoil of political excitement, when crimination and recrimination characterized the parties of the country, all admitted " + name + " was an honest shard of society--yes, like Caesar's wife, this one proudly stood above suspicion.")
					_t(1.5)
					sendMessage(s, "When we contemplate the death of a great and useful man--when we see their setting sun in the dark cloud go down in death to rise no more--sad thoughts do sink deep into every patriotic bosom. Sympathizing as I do with the family of the deceased, I hope such resolutions will be offered as will be expressive of the feelings of this house.")
					break
				if "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK" in message:
					sendMessage(s, "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK")
					break
				if "!sheep" == Lmessage:
					_t(.25)
					sendMessage(s, "sheep44: " + str(sheep))
					break
				if "!uid" == Lmessage:
					_t(.25)
					sendMessage(s, "UID: " + str(UID))
					break
				if message.startswith("=>"):
					spam = getSPAM(message)
					_t(.25)
					sendMessage(s, spam)
					break
				if "RAGE" in message:
					_t(.5)
					sendMessage(s, "RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace")
					break
				if "salty" in Lmessage:
					_t(.5)
					sendMessage(s, "If the human body is 75% water, how can you be 100% salt? Kappa")
					break
				if Lmessage.startswith("!yay"):
					sendMessage(s, "Throw your hands up and celebrate with " + Display + "! \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/")
					break
				if "abusive mods!" in Lmessage:
					sendMessage(s, "The mods are abusive! :( D: Please fix it! :(")
					break
				if message.startswith("!!") and sheep:
					command = getCommand(message)[0]
					response = getCommand(message)[1]
					sendMessage(s, "Command: " + command)
					_t(1.5)
					sendMessage(s, "Response: " + response)
					break
				if "!blame" == Lmessage:
					_t(.25)
					sendMessage(s, "Unknownking420 Kappa")
					break
				if "!memeplz" == Lmessage:
					_t(.25)
					sendMessage(s, _r(Memes))
					break
				if Lmessage.startswith("!request"):
					getRequest(Display, message)
					sendMessage(s, "Thank you for requesting, " + Display)
					break
				if "!time" == Lmessage:
					sendMessage(s, time.strftime("It is currently %a, %d %b %Y %H:%M:%S", time.localtime())+ ", " + user)
					break
				if "!points" == Lmessage:
					sendMessage(s, Points._pointsList[user])
					break
				if Lmessage.startswith("py:"):
					_x = message.split(":", 1)[1].strip()
					if not sheep:
						if "exit(" in _x.lower():
							sendMessage(s, "\"exit()\" is a disallowed function")
							break
						if "open(" in _x:
							sendMessage(s, "\"open()\" is a disallowed function")
							break
						if "while" in _x:
							sendMessage(s, "\"while\" is a disallowed keyword")
							break
						if "sys" in _x:
							sendMessage(s, "\"sys\" is a disallowed module")
							break
						if "os" in _x:
							sendMessage(s, "\"os\" is a disallowed module")
							break
						if "shutil" in _x:
							sendMessage(s, "\"shutil\" is a disallowed module")
							break
						if "sleep" in _x:
							sendMessage(s, "\"sleep\" is a disallowed function")
							break
						if "delEnv(" in _x:
							sendMessage(s, "\"delEnv\" is a disallowed function")
					try:
						if _x.find("print(") > 0:
							exec(_x)
							_u = _x.find("print(")
							_u = _x[_u+6:].split(")")[0]
							sendMessage(s, eval(_u))
							break
						_o = eval(_x)
						if type(_o) == int:
							if int(math.log10(_o)) + 1 > 500:
								sendMessage(s, "Output too long, " + str(int(math.log10(_o)) + 1) + " characters")
								break
							else:
								sendMessage(s, _o)
						elif len(str(_o)) > 500:
							sendMessage(s, "Output too long, " + str(len(str(_o))) + " characters")
							break
						else:
							sendMessage(s, _o)
					except Exception as _e:
						if type(_e) in [EOFError, TypeError, NameError]:
							sendMessage(s, type(_e).__name__ + ": " + _e.args[0])
						else:
							try:
								exec(_x)
								_codeFile.write(_x + "\n")
							except Exception as _e:
								sendMessage(s, type(_e).__name__ + ": " + _e.args[0])
					break
	#except Exception as _e:
	#	print(type(_e), *_e.args, sep = "\n")
