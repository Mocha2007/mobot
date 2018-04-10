from mochaxyz import quit
from random import choice
commands = ('drop','eat','gaze','get','go','grab','help','john','look','muffin','open','pickup','see','take','tasselfoot','use')

def llama(room,state,inv,message):
	mcl = message.content.lower()
	o = ''
	mc = message.channel
	player = message.author #NOTE THIS IS NOT AUTHOR NAME
	if mcl in quit: # not in original
		return -1,-1,False,'Goodbye!'
	elif room == -2:
		if state == 0:
			return -2,0,inv,'Meow '*14
		elif state == 1:
			return -2,1,inv,choice(['Mr Rubix SHUFFLE! >->->^^>->','Everybody DANCE!!!!!!!!!!'])
	iscommand = False
	for c in commands:
		if c in mcl:
			iscommand = True
			break
	if iscommand:
		if 'help' in mcl:
			o+='A bit lost are we llama?\n\n'
			o+='Here are some keywords you can think about using:\n'
			o+='**open use go look see gaze take grab pickup drop\n\n**'
			o+='If you want to **get** a sense of what\'s in the room, **use** the phrase **look around**. Build short sentences!\n\n'
			o+='Also remember that new words will crop up as you explore more.\n\n'
			o+='You can always find **help** by mashing that term here!'
		elif 'john' in mcl:
			o+='That\'s me!'
		elif 'mocha' in mcl:
			o+='That\'s *also* me!'
		elif 'muffin' in mcl:
			room = -2
			state = 0
			o+='Meow '*14
		elif 'tasselfoot' in mcl:
			room = -2
			state = 1
			o+=choice(['Mr Rubix SHUFFLE! >->->^^>->','Everybody DANCE!!!!!!!!!!'])
		elif 'look' in mcl or 'see' in mcl or 'gaze' in mcl:
			if room == 0:
				if 'around' in mcl or 'room' in mcl:
					o+='I **see** you looking at my study! It has that stuffy fragrance of old man and olive oil, not from me mind you! My bookshelf reaches the ceiling from the floor and is stacked with several old **books** I have acquired through the many years I have seen come and go. That **door** behind you leads to the first **room** of your adventure, so stop dawdling and **go** through it!'#orig. are
				elif 'books' in mcl:
					o+='My **books** are arranged haphazardly across the shelves for my pleasure. Some **books** even face backwards so that the spine rests against the back of the bookshelf, got to protect the spine!. My favorite book is a title called **computering** over there.'
				elif 'computering' in mcl:
					o+='Here llama, I\'ll read you the intro. \'Hello computer user. The first step to setup your account is to set several five digit passwords on your documents. This way you can protect yourself in case of computer attack or snooping onlookers...\' tist tisk llama, we have work to do. Let\'s **get** going through that door over there!'
				elif 'door' in mcl:
					o+='The wooden **door** has a small bolt on it, easy enough to slide **open** with little effort. The hinge pushes outward away from the door.'
				else:
					o+='I\'m not quite sure what you are looking at.'
			elif room == 1:
				if 'around' in mcl or 'room' in mcl:
					o+='This **room** is nothing like the **room** you were just in. The floors to walls are a blinding white, with florescent lights behind metal grates filling the **room** with an immense about of illumination. Feel like a test subject yet llama?'
					o+='\n\nRight here is a **table** I bought from the neighbors during a garage sale. Across the **room** is a similar **door** to the one your just passed through, this time with a lock.'
				elif 'door' in mcl:
					o+='What a fine door. It has a **lock** on it.'
				elif 'lock' in mcl:
					o+='This **lock** looks like it could **take** a key. Imagine that.'
				elif 'table' in mcl:
					o+='On my **table** is a white cloth with three keys... a **badkey** - a **tastykey** - a **goodkey** - I named those myself! Next to the cloth is an unfolded note with writing on it and just so you know I don\'t have handwriting like my fellow doctors.'
				elif 'note' in mcl:
					o+='I\'ll read you the **note** llama. You can\'t read! You can mash that button board, but a llama reading!\nImpossible.'
					o+='\n\n\'The **badkey** is good and the **goodkey** is bad. The **badkey** can get you through the door. That **tastykey**... you can **eat** that. It\'s made of alfalfa.\''
				elif 'badkey' in mcl:
					o+='This key is my heaviest key, given the extra metal keychain attached to it. The metal keychain has a large smiley face on it, so smile llama!'
				elif 'goodkey' in mcl:
					o+='This key is a pale blue with cracked paint all over it. Spatters of fresh red material give the eerie impression that the last user of this key is **no** longer around. Disregard that unpleasantness, llama!'
				elif 'tastykey' in mcl:
					o+='This beautiful green key shows intricate craftmanship with delicate swoops and curves **around** the handle and key blade. Wow, I couldn\'t have said it any better!'
				else:
					o+='I\'m not quite sure what you are looking at.'
		elif 'get' in mcl or 'take' in mcl or 'pickup' in mcl or 'grab' in mcl:
			if inv:
				o+='You already have **'+inv+'** in your mouth! You need to **drop** that before you **grab** something else.'
			else:
				if room == 0:
					if 'around' in mcl or 'room' in mcl:
						o+='That makes **no** sense llama! You are full of silly. In fact I would almost say you\'re distilled down to a pure sense of silly, like a fine coffee or tea!'
					elif 'books' in mcl:
						o+='You can\'t have **ALL** my books llama.'
					elif 'computering' in mcl:
						o+='You have picked up the **computering** book! Don\'t lick the pages unless you are turning them.'
						inv = 'computering'
					elif 'door' in mcl:
						o+='It\'s too heave llama. Plus I lost my tools a while back and haven\'t been able to do any maintenance for some time.'
					else:
						o+='What are you going on about llama? There\'s nothing to **'+mcl+'** of that nature **around** here!'
				elif room == 1:
					if 'tastykey' in mcl:
						o+='You pick up the **tastykey** in your mouth. It tastes delicious, so much that you want to **eat** it.'
						inv = 'tastykey'
					elif 'goodkey' in mcl:
						o+='You have picked up the **goodkey**! It tastes of a sweet, sweet honey. This key is so nice, isn\'t it? Better than those other keys!'
						inv = 'goodkey'
					elif 'badkey' in mcl:
						o+='You have picked up the **badkey**! It tastes slightly sour, of course! It\'s got bad in the title for a reason!'
						inv = 'badkey'
					else:
						o+='What are you going on about llama? There\'s nothing to **'+mcl+'** of that nature **around** here!'
		elif 'drop' in mcl:
			if inv:
				o+='You put back the **'+inv+'** where you found it.'
				inv = False
			else:
				o+='Your mouth is empty, you don\'t have anything to drop!'
		elif 'open' in mcl or 'use' in mcl: # apparently, these are functionally equivalent...?
			if room == 0:
				if 'door' in mcl:
					state = 3
					o+='You opened the door, and you\'re off to the next room! Just go through now and you\'re on your way.'
				else:
					o+='What are you trying to do llama? When you utilize the word **use** make sure you follow up with a noun such as **door** or **books**... if you need **help** finding words **look around** or something!'
			elif room == 1:
				if 'goodkey' in mcl:
					if 'lock' in mcl:
						o+='Bad news. It\'s not anything you saw. Rather, it was what you felt. 10,000 Volts of electricity can kill a Llama fairly quickly, especially when transferred between your mouth and the **door** through that bad key! Luckily your death was over before you knew it, unluckily you have **no** more life to account for.'
						o+='\n\nLet\'s try this **room** again, llama.'
						state = 0
					else:
						o+='You should probably **use** the **goodkey** with the lock!'
				elif 'badkey' in mcl:
					if 'lock' in mcl:
						o+='Carefuylly turning the **badkey** into the **lock** on the **door** the key suddenly vanishes. Now what? Where did you put my key?!'
						# note: the original game never removes badkey from your inventory. I'm not sure why this is the case.
						# Additionally, the tastykey RETURNS when you use the badkey!
						state = 3
					else:
						o+='You should probably **use** the **badkey** with the lock!'
				else:
					o+='What are you trying to do llama? When you utilize the word **use** make sure you follow up with a noun such as **door** or **books**... if you need **help** finding words **look around** or something!'
		elif 'go' in mcl:
			if room == 0:
				if state == 3:
					o+='I\'ll **see** you in the next **room** Llama. Tally-ho!'
					room = 1
					state = 0
					o+='\n\nHere is where we start our experiment, Llama. I have made you seven rooms fit for llama exploration and triumph. Do you understand?'
				else:
					o+='Sorry, I don\'t quite understand that.'
			elif room == 1:
				if state == 3:
					o+='I\'ll **see** you in the next **room** Llama. Tally-ho!'
					room = 2
					state = 0
					o+='\n\nNow that we have met in person I\'m going to be typing to you on this monitor located in each room.'
					o+='\n\nI\'m not sure if this text is coming through, can you **see** it?'
				else:
					o+='Sorry, I don\'t quite understand that.'
		elif 'eat' in mcl:
			if 'tastykey' in mcl:
				if inv == 'tastykey':
					o+='You ate the tastykey and it was delicious! What a great snack, Llama. Now I\'m going to have to make another.'
					inv = False
				else:
					o+='You don\'t have **tastykey** right now, maybe you should **pickup** that object?'
			elif inv:
				o+='You can\'t **eat** that llama. That\'s not a llama chew thing.'
			else:
				o+='What do you want to**eat** llama?'
	elif room == -1:
		if state == 0:
			o+='Llama Adventure\nA Text Adventure to Greener Pastures\n'
			o+='Write a word to start:\n\n**start**\nBegin the game!\n\n**credits**\nSee who made the game!'
			state = 1
		elif state == 1:
			if 'start' in mcl:
				o+='Good call, let\'s start!\n'
				room = 0
				state = 0
				o+='Hello you! I am so glad they finally shipped you here.\nA spot of bother with the street address, but that was fixed I assure you!\n\nAside from that, what is your name?'
			elif 'credits' in mcl:
				o+='Original game programmed and written by jmtb02.\n\nMobot port written by mocha2007.'
			else:
				o+='That statement does not make sense to me.\n'
	elif room == 0:
		if state == 0:
			o+='Oh ho! '+mcl+'! Such a ghastly thing to call yourself! I will call you Llama. You are a Llama right?'
			state = 1
		elif state == 1:
			if 'yes' in mcl:
				o+='Of course you are, I am always right! You will learn that soom enough.'
			else:
				o+='Cheeky Llama! You know what you are and I do too! Got some humor we do!'#orig. to humour
			o+='\nWell then Llama, we\'re going to start right away. If you would **open** the **door** we can start. You can do that by typing that into your magical button board! Or you can **look around** first! always **look around** in every room!'
			state = 2
	elif room == 1:
		if state == 0:
			if 'yes' in mcl:
				o+='Good Llama! Obeying is the key to survival!'
			else:
				o+='Ah, the rebellious teenage llama. Too good for their house and home. Wants their individualism! Moon and dad always keeping you down! Well we won\'t keey you long.'
			o+='\n\nNow as the 44th creature to enter this facility your job is to **get** past **room** 7. Each **room** has a puzzle the next **room** will open. If you fail the puzzle then you will most certainly die a terrible death! But that is all semantics and nothing to worry about!'
			o+='\n\nIs that clear?'
			state = 1
		elif state == 1:
			if 'yes' in mcl:
				o+='Fantastic.'
			else:
				o+='I know you know what I meant. Stop acting dumb.'
			o+='\n\nIf you need **help** at any time feel free to **use** that command. I\'ll be looking at you funny behind that mirrored one-way glass that all test facilities of this nature have! Feel free to **look around** you! Always **look** at everything! It will **help** you last longer than the others!'#orig. anytime
			state = 2
	elif room == 2:
		if state == 0:
			if 'yes' in mcl:
				o+='Good Llama! Obeying is the key to survival!'
			else:
				o+='TODO'
			o+='\n\nI quite admire your ability to **get** through a simple **room** like that, but can you **get** through a simple **room** such as this one? I am tickled by the idea that you can win such an easy **room** as the last but you cannot win an even easier **room** such as this one! All you have to do is stop that **clock** between after it ticks 14-15 seconds!'
			o+='\n\nDo you understand?'
			state = 1
		elif state == 1:
			if 'yes' in mcl:
				o+='Fair enough.'
			else:
				o+='TODO'
			o+='\n\nSpeaking of which, did you know that you can **look** at specific items for clues to the puzzle rooms? Anyway... carry on.'
			state = 2
	#NEXT: TODO
	if o == '':o = 'I don\'t quite understand what you mean.'
	return room,state,inv,o