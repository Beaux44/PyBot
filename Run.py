# !/usr/bin/env python
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
import random
import math
import time
from re import findall
from Read import *
from Socket import openSocket, sendMessage, joinRoom, Exit
from Settings import CHANNEL, NICK
import Points

_r =  random.choice
math.phi = (1 + 5**.5) / 2
sleep = time.sleep
_startTime = time.time()

# Load last saved environment
_codeFileName = "code/" + CHANNEL + ".py"
try:
	_codeFile = open(_codeFileName, 'r')
except:
	_codeFile = open(_codeFileName, 'w')
	_codeFile = open(_codeFileName, 'r')

for i in _codeFile.read().split("\n"):
	try:
		exec(i)
	except:
		pass
_codeFile = open(_codeFileName, 'a')
# Load last saved environment

# Remove last saved environment
def delEnv():
	open(_codeFileName, 'w').close()
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
readbuffer = b""
_numberOfTimesLooped = 0
_lastUsed = time.time()
_lastTimeLooped = time.time()

while True:
	# HACK
	_currentTime = time.time()
	if _currentTime - _lastTimeLooped < 0.5:
		_numberOfTimesLooped += 1
		if _numberOfTimesLooped > 100:
			_codeFile.close()
			_POINTS_LIST_ = open(Points._pointsFileName, "w")
			_POINTS_LIST_.write(str(Points._pointsList))
			_POINTS_LIST_.close()
			from os import system
			try:
				system("py Run.py " + CHANNEL)
			except KeyboardInterrupt:
				pass
			exit()
		_lastTimeLooped = time.time()
	else:
		_numberOfTimesLooped = 0

	#try:
	readbuffer = s.recv(1024)
	temp = readbuffer.decode().split("\n")
	readbuffer = temp.pop()

	for line in temp:
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
			noot = getNoot(line)
			UID = getUID(line)

			if "bot" not in user:
				print(Display + ": " + message)
				_o = open("chat.txt", 'ab')
				_o.write((Display + ": " + message + "\r\n").encode())
				_o.close()
				if noot and "!reload" == Lmessage:
					_codeFile.close()
					_POINTS_LIST_ = open(Points._pointsFileName, "w")
					_POINTS_LIST_.write(str(Points._pointsList))
					_POINTS_LIST_.close()
					from os import system
					try:
						system("py Run.py " + CHANNEL)
					except KeyboardInterrupt:
						pass
					exit()
				if len(findall(r"(?:hi|hello|hey)\,?\s?noot\s?bot", Lmessage)):
					sendMessage(s, "Hi, " + Display)
					break
				if noot and "go away noot bot" in Lmessage:
					sleep(.25)
					sendMessage(s,
						"Okay, I'm sorry for being your favorite sentient bot. FeelsBadMan")
					sleep(.50)
					Exit(s, _codeFile, Points._pointsFileName, Points._pointsList)
					break
				if "!ping" == Lmessage:
					sendMessage(s, "pong")
					break
				if "say my name" == Lmessage:
					sleep(.25)
					sendMessage(s, "What if I don't want to, " + Display + "? FeelsBadMan")
					break
				if "go away noot bot" == Lmessage:
					sleep(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite sentient bot FeelsBadMan")
					sleep(1.5)
					sendMessage(s, "FeelsAmazingMan LOLOLOLOLOL You thought you could just tell me like that and I'd listen to you!?!? LOLOLOLOLOL FeelsAmazingMan")
					sleep(1.25)
					sendMessage(s, "Fuck off " + Display)
					break
				if "!commands" == Lmessage:
					sleep(.25)
					sendMessage(s, "go away noot bot, Say my name, potato salad, RIP (noun), =>anything(number), FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK, !uid, !sheep, RAGE, !ping, !request, !memeplz, !yay, !time, !points, salty, !help")
					break
				if "potato salad" in Lmessage:
					sendMessage(s, "I heard potato salad? " + Display + ", mod: " + str(mod))
					break
				if message.startswith("RIP "):
					sleep(.25)
					name = parseRIP(message)
					sendMessage(s, "One thing I must say of " + name + ". However honest public men may be, there are always those who impeach their motives or integrity; but I am proud to bear testimony that, even in the turmoil of political excitement, when crimination and recrimination characterized the parties of the country, all admitted " + name + " was an honest shard of society--yes, like Caesar's wife, this one proudly stood above suspicion.")
					sleep(1.5)
					sendMessage(s, "When we contemplate the death of a great and useful man--when we see their setting sun in the dark cloud go down in death to rise no more--sad thoughts do sink deep into every patriotic bosom. Sympathizing as I do with the family of the deceased, I hope such resolutions will be offered as will be expressive of the feelings of this house.")
					break
				if "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK" in message:
					sendMessage(s, "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK")
					break
				if "!sheep" == Lmessage:
					sleep(.25)
					sendMessage(s, "sheep44: " + str(noot))
					break
				if "!uid" == Lmessage:
					sleep(.25)
					sendMessage(s, "UID: " + str(UID))
					break
				if message.startswith("=>"):
					_spam = getSPAM(message)
					sleep(.25)
					try:
						if Points._pointsList[user] < _spam.count(message.rsplit("(", 1)[0][2:]) * 5 and not noot:
							sendMessage(s, "Not enough points")
							break
						elif not noot:
							Points._pointsList[user] -= _spam.count(message.rsplit("(", 1)[0][2:]) * 5
					except:
						if not noot:
							sendMessage(s, "Not enough points")
							break
					sendMessage(s, _spam)
					break
				if "RAGE" in message:
					sleep(.5)
					sendMessage(s, "RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace")
					break
				if "salty" in Lmessage:
					sleep(.5)
					sendMessage(s, "If the human body is 75% water, how can you be 100% salt? Kappa")
					break
				if Lmessage == "!yay":
					sendMessage(s, "Throw your hands up and celebrate with " + Display + "! \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/")
					break
				if "abusive mods!" in Lmessage:
					sendMessage(s, "The mods are abusive! :( D: Please fix it! :(")
					break
				if message.startswith("!!") and noot:
					command = getCommand(message)[0]
					response = getCommand(message)[1]
					sendMessage(s, "Command: " + command)
					sleep(1.5)
					sendMessage(s, "Response: " + response)
					break
				if "!blame" == Lmessage:
					sleep(.25)
					sendMessage(s, "Unknownking420 Kappa")
					break
				if "!memeplz" == Lmessage:
					sleep(.25)
					sendMessage(s, _r(Memes))
					break
				if Lmessage.startswith("!request"):
					if Display != "ChrisarN":
						getRequest(Display, message)
						sendMessage(s, "Thank you for requesting, " + Display)
					else:
						sendMessage(s, "You have been banned from requesting")
					break
				if "!time" == Lmessage:
					sendMessage(s,
								time.strftime("It is currently %a, %d %b %Y %H:%M:%S",
								time.localtime()) + ", " + Display)
					break
				if "!points" == Lmessage:
					try:
						sendMessage(s, Points._pointsList[user])
					except:
						sendMessage(s, "not found")
					break
				if "!help" == Lmessage:
					sendMessage(s, "You can do everything listed here excluding a few except cases: https://docs.python.org/3.6/ SeemsGood")
					break
				if Lmessage.startswith("+<"):
					addCommand(message)
					break
				if Lmessage.startswith("-<"):
					delCommand(message)
					break
				if message.startswith("!"):
					try:
						sendMessage(s, runCommand(Lmessage,
										**{'line':line,
											'display':Display,
											'user':user,
											'mod':mod,
											'ishost':ishost,
											'noot':noot,
											'UID':UID,
											'channel':CHANNEL
										}
									)
						)
					except:
						sendMessage(s, "Command could not be run.")
					break

				# NOTE: Move this to an external file at some point
				if Lmessage.startswith("py:"):
					_x = message.split(":", 1)[1].strip()
					_mem = _x
					if not noot:
						if "exit" in _x.lower():
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"exit()\" is a disallowed function")
							break
						if "socket" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"socket\" is a disallowed module")
							break
						if "sys" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"sys\" is a disallowed module")
							break
						if " os" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"os\" is a disallowed module")
							break
						if " shutil" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"shutil\" is a disallowed module")
							break
						if "global" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"globals()\" is a disallowed function")
							# else:
							# 	sendMessage(s, "\"global\" is a disallowed keyword")
							break
						if "open" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"open()\" is a disallowed function")
							break
						if "del" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"del\" is a disallowed keyword")
							break
						if "while" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"while\" is a disallowed keyword")
							break
						if "sleep" in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "\"sleep\" is a disallowed function")
							break
						if "Points." in _x:
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "editing points is disallowed")
							break
						if findall(r"\s+s\s*[\.=]{1}", _x) or _x == "s":
							sendMessage(s, "I'm sorry {} but I can't let you do that".format(Display))
							# sendMessage(s, "DON'T FUCK WITH S!!!")
							break
					try:
						if _x.find("print(") >= 0:
							exec(_x.replace(findall(r"print[(].+[)]", _x)[0], "pass"))
							_u = _x.find("print(")
							_u = eval(_x[_u+6:].split(")", 1)[0])
							if type(_u) != int:
								if len(str(_u)) < 450:
									sendMessage(s, _u)
								else:
									sendMessage(s, "Output too long, " + str(len(str(_u))) + " characters")
							else:
								if int(math.log10(_u)) + 1 < 450:
									sendMessage(s, _u)
								else:
									sendMessage(s, "Output too long, " + str(int(math.log10(_u)) + 1) + " characters")
							break
						_o = eval(_x)
						if type(_o) == int:
							if int(math.log10(_o)) + 1 > 450:
								sendMessage(s, "Output too long, " + str(int(math.log10(_o)) + 1) + " characters")
								break
							else:
								sendMessage(s, _o)
						elif len(str(_o)) > 450:
							sendMessage(s, "Output too long, " + str(len(str(_o))) + " characters")
							break
						else:
							sendMessage(s, _o if type(_o).__name__.lower() not in ["module"] else "")
					except Exception as _e:
						if type(_e) in [EOFError, TypeError, NameError, MemoryError]:
							sendMessage(s, type(_e).__name__ + (": " + _e.args[0] if len(_e.args) else ""))
						else:
							try:
								exec(_x)
								if "print(" not in _mem:
									_codeFile.write(_x + "\n")
									_codeFile.close()
									_codeFile = open(_codeFileName, 'a')
							except Exception as _e:
								sendMessage(s, type(_e).__name__ + (": " + _e.args[0] if len(_e.args) else ""))
					break
	#except Exception as _e:
	#	print(type(_e), *_e.args, sep = "\n")
