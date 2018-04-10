from mochaxyz import quit
commands = ('look','take')

def llama(room,state,message):
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
		if 'look' in mcl:
			if room == 0:
				if 'around' in mcl or 'room' in mcl:
					o+='I **see** you looking at my study! It has that stuffy fragrance of old man and olive oil, not from me mind you! My bookshelf reachers the ceiling from the floor and are stacked with several old **books** I have acquired through the many years I have seen come and go. That **door** behind you leads to the first **room** of your adventure, so stop dawdling and **go** through it!'
				elif 'books' in mcl:
					o+='My **books** are arranged haphazardly across the shelves for my pleasure. Some **books** even face backwards so that the spine rests against the back of the bookshelf, got to protect the spine!. My favorite book is a title called **computering** over there.'
				elif 'computering' in mcl:
					o+='Here llama, I\'ll read you the intro. \'Hello computer user. The first step to setup your account is to set several five digit passwords on your documents. This way you can protect yourself in case of computer attack or snooping onlookers...\' tist tisk llama, we have work to do. Let\'s **get** going through that door over there!'
				elif 'door' in mcl:
					o+='The wooden **door** has a small bolt on it, easy enough to slide **open** with little effort. The hinge pushes outward away from the door.'
				else:
					o+='I\'m not quite sure what you are looking at.'
		# do take too!!!
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
				o+='Of course you are, I am always right! You will learn that soom enough.\n'
			else:
				o+='TODO\n'
			o+='Well then Llama, we\'re going to start right away. If you would **open** the **door** we can start. You can do that by typing that into your magical button board! Or you can **look around** first! always **look around** in every room!'
			state = 2
	return room,state,o