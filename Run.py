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
from random import randint as r
from time import sleep as t
from sys import exit as sys
from Read import *
from Socket import openSocket, sendMessage, joinRoom
from Settings import *
#from Threads import * (This file is not finished *ABSOLUTELY DO NOT USE IT WILL IMMEDIATELY BAN YOUR IP FROM CHATTING FOR 8 HOURS*)
s = openSocket()
Meme = [u"~~~~~~~[]=¤ԅ( ◔益◔ )ᕗ The longer you cage us, the harder our arm of righteous spam will smite thee! ~~~~~~~[]=¤ԅ( ◔益◔ )ᕗ", u"୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨ ୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨ ୧༼ಠ益ಠ༽୨ WHY ARE WE RIOTING ୧༼ಠ益ಠ༽୨", "Europe was founded in 1848 by Walker Texas Ranger when he rode a horse across the Atlantic, he called it \"Eastern USA\" which was eventually abbreviated as just \"EU\"", u"———————————————————————— imGlitch You have been gifted the Golden Kappa!————————————————————————", u"PogChamp PogChamp HOLD CTRL AND TYPE \"WTF\" FOR ℱ𝓪𝓷𝓬𝔂 𝓦𝓣ℱ PogChamp PogChamp", u"ヽ༼ ͠ ͠°〜 ͜ʖ〜 ͠ ͠° ༽ﾉ¤=[———— Hello. My name is Inigo Dongtoya. You killed my Kappa. Prepare to die.", "MrDestructoid ban MrDestructoid one MrDestructoid bot MrDestructoid manufacture MrDestructoid another MrDestructoid", "MrDestructoid ME BOT MrDestructoid ME SPAM MrDestructoid NO VIEWERS MrDestructoid IF BAN MrDestructoid", u"FeelsBadMan THIS USED TO BE A 2016 STREAM FeelsBadMan THIS USED TO BE A 2016 STREAM FeelsBadMan", u"୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨ ୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨୧༼ಠ益▀̿༽୨ Pillage and Plunder ୧༼ಠ益▀̿༽୨", u"Hello I am Ka­ppa Ka­pparino. I'm an employee at Twitch and am currently testing changes to the Ka­ppa emote. Can you please type Ka­ppa to confirm that it's working?", u"My Ka­ppa privileges have been revoked. FeelsBadMan", u"~~~~~~~[]=¤ԅ[✖Ĺ̯ಠ]╯ AND NOW WE MUTINY! ~~~~~~~[]=¤ԅ[✖Ĺ̯ಠ]/", u"( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ clickty clack clickty clack with this chant I summon spam to the chat ( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ", u"Tᴏ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ғʀᴏᴍ ᴅᴇᴠᴀsᴛᴀᴛɪᴏɴ. ᴛᴏ ᴜɴɪᴛᴇ ᴀʟʟ sᴘᴀᴍᴍᴇʀs ᴡɪᴛʜɪɴ ᴏᴜʀ ɴᴀᴛɪᴏɴ. ᴛᴏ ᴅᴇɴᴏᴜɴᴄᴇ ᴛʜᴇ ᴇᴠɪʟ ᴏғ Tʀᴜᴍᴘ ᴀɴᴅ ᴍᴏᴅs. ᴛᴏ ᴇxᴛᴇɴᴅ ᴏᴜʀ sᴘᴀᴍ ᴛᴏ ᴛʜᴇ sᴛᴀʀs ᴀʙᴏᴠᴇ. ᴄᴏᴘʏ! ᴘᴀsᴛᴇ! ᴄʜᴀᴛ sᴘᴀᴍ ʙʟᴀsᴛ ᴏғғ ᴀᴛ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ʟɪɢʜᴛ! sᴜʀʀᴇɴᴅᴇʀ ᴍᴏᴅs ᴏʀ ᴘʀᴇᴘᴀʀᴇ ᴛᴏ ғɪɢʜᴛ.", u"H ＥＬＬＯ ＡＭ ４８ ＹＥＡＲ ＭＡＮ ＦＲＯＭ ＳＯＭＡＬＩＡ． ＳＯＲＲＹ ＦＯＲ ＢＡＤ ＥＮＧＬＡＮＤ． Ｉ ＳＥＬＬＥＤ ＭＹ ＷＩＦＥ ＦＯＲ ＩＮＴＥＲＮＥＴ ＣＯＮＮＥＣＴＩＯＮ ＦＯＲ ＰＬＡＹ ＂ｈｅａｒｔｈ ｓｔｏｎｅ＂ ＡＮＤ Ｉ ＷＡＮＴ ＴＯ ＢＥＣＯＭＥ ＴＨＥ ＧＯＯＤＥＳＴ ＰＬＡＹＥＲ ＬＩＫＥ ＹO U", u"° ☾ ☆ ¸. ¸ 　★　 :.　 . • ○ ° ★　 .　 　.　.　　¸ .　　 ° 　¸. * ● ¸ .　...somewhere　　　° ☾ ° 　¸. ● ¸ .　　★　° :.　 . • ° 　 .　 *　:.　.in a parallel universe ● ¸ 　　　　° ☾ °☆ 　. * ¸.　　　★　★ ° . .　　　　.　☾ °☆ 　. * ● chat actually loves spam...° ☾　★ °● ¸ .　　　★　° :.　 . • "]
# Please spam, "To ALL viewers.... To ALL streamers.... To ALL Viewers and Streamers alike.... To ALL whom would be listening.... Please.... Give me your DANKEST memes..... and ONLY your DANKEST memes.... For use in my randomized meme spam bot...! Kappa" into every stream you go into so I can expand my meme list

joinRoom(s)
readbuffer = ""
while True:
	t(3)
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		if "PING :tmi.twitch.tv" in line:
			s.send(line.replace("PING", "PONG"))
			print(line)
			print(line.replace("PING", "PONG"))
			break
		if not ("PING :tmi.twitch.tv") in line:
			Display = getDisplay(line)

			user = getUser(line)

			message = str(getMessage(line))

			Lmessage = str(string.lower(getMessage(line)))

			mod = getMod(line)

			sheep = getSheep(line)

			UID = getUID(line)

			if not ("bot") in user:
				print Display + ": " + message
				o = open("chat.txt", 'a')
				o.write(Display + ": " + message + "\r\n")
				o.close()
				if "!ping" in Lmessage and sheep:
					sendMessage(s, "pong")
					break
				if "say my name" == Lmessage:
					t(.25)
					sendMessage(s, "What if I don't want to, " + Display + "? FeelsBadMan")
					break
				# if "wee woo" in message and not ("s44bot") in user:
				# 	t(.25)
				# 	sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				# 	t(1.5)
				# 	sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				# 	t(1.5)
				# 	sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				# 	t(1.5)
				# 	sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				# 	t(1.5)
				# 	sendMessage(s, "Kappa")
				# 	break
				if "go away sheep bot" in Lmessage:
					t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite sentient bot FeelsBadMan")
					t(1.5)
					sendMessage(s, "FeelsAmazingMan LOLOLOLOLOL You thought you could just tell me like that and I'd listen to you!?!? LOLOLOLOLOL FeelsAmazingMan")
					t(1.25)
					sendMessage(s, "Fuck off " + Display)
					break
				if "!commands" in Lmessage:
					t(.25)
					sendMessage(s, "wee woo, go away sheep bot, Say my name, potato salad, RIP (noun), !!anything(number), FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK, !cow, !pig, RAGE, !ping")
					break
				if "sheep44" == user and ("fuck off sheep bot") in Lmessage:
					t(.25)
					sendMessage(s, "Okay, I'm sorry for being your favorite self-sentient bot. FeelsBadMan")
					t(.25)
					sys()
					break
				if "potato salad" in Lmessage:
					sendMessage(s, "I heard potato salad? " + Display + ", mod: " + str(mod))
					break
				if message.startswith("RIP "):
					t(.25)
					name = parseRIP(message)
					sendMessage(s, "One thing I must say of " + name + ". However honest public men may be, there are always those who impeach their motives or integrity; but I am proud to bear testimony that, even in the turmoil of political excitement, when crimination and recrimination characterized the parties of the country, all admitted " + name + " was an honest shard of society--yes, like Caesar's wife, this one proudly stood above suspicion.")
					t(1.5)
					sendMessage(s, "When we contemplate the death of a great and useful man--when we see their setting sun in the dark cloud go down in death to rise no more--sad thoughts do sink deep into every patriotic bosom. Sympathizing as I do with the family of the deceased, I hope such resolutions will be offered as will be expressive of the feelings of this house.")
					break
				if "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK" in message:
					sendMessage(s, "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK")
					break
				if Lmessage.startswith("!sheep"):
					t(.25)
					sendMessage(s, "sheep44: " + str(bool(sheep)))
					break
				if Lmessage.startswith("!uid"):
					t(.25)
					sendMessage(s, "UID: " + str(int(UID)))
					break
				if message.startswith("!!"):
					spam = getSPAM(message)
					t(.25)
					sendMessage(s, spam)
					break
				if "RAGE" in message:
					t(.5)
					sendMessage(s, "RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace")
					break
				if "salty" in Lmessage:
					t(.5)
					sendMessage(s, "If the human body is 75% water, how can you be 100% salt? Kappa")
					break
				if Lmessage.startswith("!yay"):
					sendMessage(s, "Throw your hands up and celebrate with " + Display + "! \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/")
					break
				if "abusive mods!" in Lmessage:
					sendMessage(s, "The mods are abusive! :( D: Please fix it! :(")
					break
				if message.startswith("=>") and sheep:
					command = getCommand(message)[0]
					response = getCommand(message)[1]
					sendMessage(s, "Command: " + command)
					t(1.5)
					sendMessage(s, "Response: " + response)
					break
				if Lmessage.startswith("!blame"):
					t(.25)
					sendMessage(s, "Unknownking420 Kappa")
					break
				if Lmessage.startswith("!meme"):
					t(.25)
					RI = r(0,17)
					sendMessage(s, Meme[RI].encode("utf-8"))
					break
				if Lmessage.startswith("points") and sheep:
					t(1.5)
					sendMessage(s, "!points")
					break
				if Lmessage.startswith("!request"):
					getRequest(Display, message)
					sendMessage(s, "Thank you for requesting, " + Display)
					break
