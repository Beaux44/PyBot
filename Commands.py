# PyBot is a Twitch IRC chatbot used particularly for spamming your chat, but as well as a general chatbot for doing whatever.
# Copyright (C) 2016 Beaux
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


s = openSocket()
joinRoom(s)
readbuffer = ""
while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			mod = getMod(line)
			sheep = getSheep(line)
			UID = getUID(line)
			spam = getSPAM(message)
			Display = getDisplay(line)
			print Display + ": " + message
			if message.startswith("ping"):
				sendMessage(s, "pong")
				break
			if "Say my name" in message:
				time.sleep(.25)
				sendMessage(s, "What if I don't want to, " + Display + "? FeelsBadMan")
				break
			if "you suck" in message:
				time.sleep(.25)
				sendMessage(s, "No, you suck!")
				break
			if "love" in message:
				time.sleep(.25)
				sendMessage(s, "<3 <3 <3")
				break
			if "cool" in message:
				time.sleep(.25)
				sendMessage(s, "PogChamp So Cool!!! PogChamp")
				break
			if "bot" not in user and "wee woo" in message:
				time.sleep(.25)
				sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				time.sleep(1.5)
				sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				time.sleep(1.5)
				sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				time.sleep(1.5)
				sendMessage(s, "wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo wee woo")
				time.sleep(1.5)
				sendMessage(s, "Kappa")
				break
			if "gtg" in message:
				time.sleep(.25)
				sendMessage(s, "See you later, then! Hope you have a great time doing whatever you'll be doing! Kappa /")
				break
			if "Go away sheep bot" in message:
				time.sleep(.25)
				sendMessage(s, "Okay, I'm sorry for being your favorite self-sentient bot FeelsBadMan :(")
				time.sleep(1.5)
				sendMessage(s, "FeelsAmazingMan LOLOLOLOLOL You thought you could just tell me like that and I'd listen to you!?!? LOLOLOLOL FeelsAmazingMan")
				time.sleep(.5)
				sendMessage(s, "Fuck off " + Display)
				break
			if "what are the commands" in message:
				time.sleep(.25)
				sendMessage(s, "you suck, love, cool, wee woo, Go away sheep bot, gtg, Say my name, potato salad, RIP (noun), !!anything(number), FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK, cow, pig, RAGE, ping")
				time.sleep(1.5)
				sendMessage(s, "you can say these in a sentence and most of them will work just the same. Also, they are case-sensitive, I'm working on fixing that.")

				break
			if "sheep44" == user and "Fuck off sheep bot" in message:
				time.sleep(.25)
				sendMessage(s, "Okay, I'm sorry for being your favorite self-sentient bot. FeelsBadMan")
				time.sleep(.25)
				sys()
				break
			# if "sheep44" in user and "Kappa" in message:
				# time.sleep(1.5)
				# sendMessage(s, "Kappa")
				# time.sleep(1.5)
				# sendMessage(s, "Kappa Kappa")
				# time.sleep(1.5)
				# sendMessage(s, "Kappa Kappa Kappa")
				# time.sleep(1.5)
				# sendMessage(s, "Kappa Kappa")
				# time.sleep(1.5)
				# sendMessage(s, "Kappa")
				# break
			if "***" in message:
				time.sleep(.25)
				sendMessage(s, "Hey, " + Display + "!")
				break
			if "potato salad" in message:
				sendMessage(s, "I heard potato salad? " + Display + ", mod: " + str(mod))
				break
			if message.startswith("RIP ") == True:
				time.sleep(.25)
				name = parseRIP(message)
				sendMessage(s, "One thing I must say of " + name + ". However honest public men may be, there are always those who impeach their motives or integrity; but I am proud to bear testimony that, even in the turmoil of political excitement, when crimination and recrimination characterized the parties of the country, all admitted " + name + " was an honest shard of society--yes, like Caesar's wife, this one proudly stood above suspicion.")
				time.sleep(1.5)
				sendMessage(s, "When we contemplate the death of a great and useful man--when we see their setting sun in the dark cloud go down in death to rise no more--sad thoughts do sink deep into every patriotic bosom. Sympathizing as I do with the family of the deceased, I hope such resolutions will be offered as will be expressive of the feelings of this house.")
				break
			if "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK" in message:
				sendMessage(s, "FFFFFFFFFFUUUUUUUUUUUUCCCCCCCCCCCCCCKKKKKKKKKKK you, too MVGame")
				break
			if "cow" in message:
				time.sleep(.25)
				sendMessage(s, "sheep44: " + str(sheep))
				break
			if "pig" in message:
				time.sleep(.25)
				sendMessage(s, "UID: " + str(UID))
				break
			if message.startswith("!!"):
				sendMessage(s, spam)
				break
			if "RAGE" in message:
				sendMessage(s, "RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace RageFace")
				break
