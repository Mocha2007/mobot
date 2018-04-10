from mochaxyz import quit
commands = ('drop','gaze','get','grab','help''look','pickup','see','take')

def llama(room,state,inv,message):
	mcl = message.content.lower()
	o = ''
	mc = message.channel
	player = message.author #NOTE THIS IS NOT AUTHOR NAME
	if mcl in quit: # not in original
		return -1,-1,'Goodbye!'
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
		elif 'go' in mcl:
			if room == 0:
				if state == 3:
					o+='TODO'
					o+='\n\nHere is where we start our experiment, Llama. I have made you seven rooms fit for llama exploration and triumph. Do you understand?'
					room = 1
					state = 0
				else:
					o+='Sorry, I don\'t quite understand that.'
		# TODO take
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
				o+='Good Llama! Obeying is the key to survival!\n\n'
				o+='Now as the 44th creature to enter this facility your job is to **get** past **room** 7. Each **room** has a puzzle the next **room** will open. If you fail the puzzle then you will most certainly die a terrible death! But that is all semantics and nothing to worry about!\n\nIs that clear?'
			else:
				o+='TODO'
			state = 1
		elif state == 1:
			if 'yes' in mcl:
				o+='Fantastic.\n\n'
				o+='If you need **help** at any time feel free to **use** that command. I\'ll be looking at you funny behind that mirrored one-way glass that all test facilities of this nature have! Fell free to **look around** you! Always **look** at everything! It will **help** you last longer than the others!'#orig. anytime
			else:
				o+='TODO'
			state = 2
	#NEXT: TODO
	return room,state,inv,o