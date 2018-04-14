# TODO
# random fact
from discord.ext.commands import Bot
import discord

from datetime import timezone
from random import choice as c
from random import randint,shuffle
from math import ceil,gcd,hypot,pi
from time import time,sleep
from re import compile,search
from statistics import median,mode,stdev
from winsound import PlaySound,SND_FILENAME
import mochaastro,mochabf,mochagolfscript,mochalang,mochallama,mochamath,mocharpn,mochastargen,mochattt
from mochaxyz import *

# CODE SHIT
def help(command):
	doc = open("help.txt", "r").read()
	doclines = doc.split('\n')
	if command == '':return open("help2.txt", "r").read()
	clen = len(command)
	relevant = '```\n'
	begin = 0
	# try to find command
	depth = 0 # to prevent UnboundLocalError on a wrong command
	for i in range(len(doclines)):
		begin = i
		line = doclines[i]
		if line[0]!='\t':lastmajor = line
		if line[:clen] == command: # MAJOR command, not minor
			depth = 1
			break
		elif line[:clen+1] == '\t'+command: # MINOR command, not major
			depth = 2
			break
	if depth>1:relevant+=lastmajor+'\n' #print overcommand
	while 1:
		relevant += doclines[i]+'\n'
		i+=1
		try:
			if doclines[i][:depth] != '\t'*depth:break # must be another command or end
		except IndexError:break
	return relevant+'```'

quotefiles = [
'bee',
'hi',
'info',
'link',
'moquote',
'prequel',
'spidey',
'tng'
]

def play(x):
	PlaySound(x,SND_FILENAME)

def product(numlist):
	if len(numlist) == 0:return 0
	if len(numlist) == 1:return numlist[0]
	return numlist[0] * product(numlist[1:])

def momath(string):
	arg = string.lower().split(' ')

	# simple

	if arg[0] in ('circumference','perimeter'):
		if arg[1] == 'circle':
			return float(arg[2])*pi
	elif arg[0] == 'ecc':
		a = float(arg[1])
		b = float(arg[2])
		return (1-b**2/a**2)**.5
	elif arg[0] == 'hypot':
		return hypot(float(arg[1]),float(arg[2]))

	# complex

	elif arg[0][:3] == 'ack':
		return mochamath.ack(int(arg[1]),int(arg[2]))
	elif arg[0][:-4] == 'area':
		if arg[1] == 'circle':
			r = float(arg[2])
			return mochamath.areacircle(r)
		elif arg[1] == 'cone':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.areacone(r,h)
		elif arg[1] == 'cylinder':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.areacone(r,h)
		elif arg[1] == 'hexagon':
			return 3/2*3**.5*float(arg[2])**2
		elif arg[1] == 'octagon':
			return (2+2*2**.5)*float(arg[2])**2
		elif arg[1] == 'pentagon':
			return ((25+10*5**.5)**.5)/4*float(arg[2])**2
		elif arg[1] == 'sphere':
			r = float(arg[2])
			return mochamath.areasphere(r)
		elif arg[1] == 'square':
			return float(arg[2])**2
		elif arg[1] == 'triangle':
			a = arg[2]
			b = arg[3]
			c = arg[4]
			s = (a+b+c)/2
			return (s*(s-a)*(s-b)*(s-c))**.5
		elif arg[1] == 'trigon':
			return 3**.5/4*float(arg[2])**2
	elif arg[0] == 'd':
		d = arg[1]
		poly = arg[2:]
		return mochamath.dpoly(poly,d)
	elif arg[0] == 'i':
		i = arg[1]
		poly = arg[2:]
		return mochamath.ipoly(poly,i)
	elif arg[0] == 'frac':
		neg = False
		floating = float(arg[1])
		if floating < 0:
			floating = -floating
			neg = True
		d = 0
		while floating != int(floating):
			floating = floating*10
			d+=1
		floating = int(floating)
		d = 10**d
		g = gcd(floating,d)
		floating = int(floating/g)
		d = int(d/g)
		return int(('-' if neg else '')+str(floating)),d
	elif arg[0] == 'gcd':
		return gcd(int(arg[1]),int(arg[2]))
	elif arg[0] == 'lcm':
		a = int(arg[1])
		b = int(arg[2])
		return int(abs(a*b)/gcd(a,b))
	#elif arg[0] == 'map':
	#	a = list(map(float,arg[2:]))
	#	f = arg[1]
	#	return eval('list(map('+f+',a))')
	elif arg[0] == 'max':
		return max(map(float,arg[1:]))
	elif arg[0] == 'mean':
		a = list(map(float,arg[1:]))
		return sum(a)/len(a)
	elif arg[0] == 'min':
		return min(map(float,arg[1:]))
	elif arg[0] == 'nroot':
		return float(arg[1])**(1/float(arg[2]))
	elif arg[0] == 'linear':
		m = float(arg[1])
		b = float(arg[2])
		return -b/m
	elif arg[0] == 'product':
		return product(list(map(float,arg[1:])))
	elif arg[0] == 'root':
		a = float(arg[1])
		b = float(arg[2])
		c = float(arg[3])
		d = (b**2-4*a*c)**.5
		return (-b+d)/2,(-b-d)/2
	elif arg[0] == 'random':
		if arg[1] == 'card':
			return mochamath.card()
		elif arg[1] == 'mnm' or arg[1] == 'm&m':
			return mochamath.mnm()
	elif arg[0] == 'sqrt':
		return float(arg[1])**.5
	elif arg[0] == 'sum':
		return sum(map(float,arg[1:]))
	elif arg[0][:3] == 'vol':
		if arg[1] == 'cone':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.volumecone(r,h)
		elif arg[1] == 'cylinder':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.volumecylinder(r,h)
		elif arg[1] == 'sphere':
			r = float(arg[2])
			return mochamath.volumesphere(r)

	return ':/'

def moastro(string):
	arg = string.lower().split(' ')

	if arg[0] == 'density' or arg[0] == 'rho':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.density(mass,radius)
	elif arg[0] == 'escapevelocity' or arg[0] == 've':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.vescape(mass,radius)
	elif arg[0] == 'g' or arg[0] == 'grav' or arg[0] == 'gravity':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.surfacegravity(mass,radius)
	elif arg[0] == 'goldilocks' or arg[0] == 'habitablezone':
		m = float(arg[1])
		return mochaastro.habitablezone(m)
	elif arg[0] == 'hohmann':
		i = float(arg[1])
		o = float(arg[2])
		m = float(arg[3])
		return mochaastro.hohmann(i,o,m)
	elif arg[0] == 'p' or arg[0] == 'period':
		mass = float(arg[1])
		sma = float(arg[2])
		return mochaastro.p(mass,sma)
	elif arg[0] == 'roche':
		m = float(arg[1])
		d = float(arg[2])
		return mochaastro.roche(m,d)
	elif arg[0] == 'soi':
		m = float(arg[1])
		M = float(arg[2])
		a = float(arg[3])
		return mochaastro.roche(m,M,a)
	elif arg[0] == 'star':
		m = float(arg[1])
		s = mochaastro.star(m)
		return '```\nMass: '+str(m)+' kg\nRadius: '+str(s[0])+' m\nLuminosity: '+str(s[1])+' W\nTemperature: '+str(s[2])+' K\nLifespan: '+str(s[3])+' s```'
	elif arg[0] == 'stargen':
		try:
			m = float(arg[1])
			return mochastargen.stargen(m)
		except (IndexError,ValueError):return mochastargen.stargen('r')
	elif arg[0] == 'synodic':
		a = float(arg[1])
		b = float(arg[2])
		return mochaastro.synodic(a,b)

	try:return object[arg[0]][arg[1]]
	except:return ':/'

def moling(string):
	arg = string.split(' ')

	if arg[0] == 'ipa':
		if arg[1] == 'en':
			return mochalang.ipa(arg[2])
		elif arg[1] == 'de':
			return mochalang.germanipa(arg[2])
		elif arg[1] == 'es':
			return mochalang.spanishipa(arg[2])
		elif arg[1] == 'fr':
			return mochalang.frenchipa(arg[2])
		elif arg[1] == 'hu':
			return mochalang.hungarianipa(arg[2])
		elif arg[1] == 'it':
			return mochalang.italianipa(arg[2])
		elif arg[1] == 'po':
			return mochalang.polishipa(arg[2])
	elif arg[0] == 'pie':
		try:return pie(arg[1])
		except:return 'https://en.wikipedia.org/wiki/Proto-Indo-European_phonology'
	elif arg[0] == 'scrabble':
		try:m = int(arg[2])
		except:m = 1
		return mochalang.scrabble(arg[1])*m
	elif arg[0] == 'soundex':
		return mochalang.soundex(arg[1])
	elif arg[0] == 'x-sampa' or arg[0] == 'xsampa':
		try:return xsampa(arg[1])
		except:return 'https://en.wikipedia.org/wiki/X-SAMPA'

	return ':/'

def sto(string):
	arg = string.split(' ')
	try:
		if arg[0] == 'search':return qfsearch(arg[1],'temp')
	except IndexError:pass

	if arg[0] == 'sto':
		inputendo = ' '.join(arg[1:])
		if '<@!' in inputendo:return 'Not happening.'
		if 'm!' == inputendo[:2]:return 'Not happening.'
		for line in open("temp.txt", "r").read():
			if inputendo == line:return 'Quote Already Stored.'
		open("temp.txt", "a").write('\n'+inputendo)
		return 'Success!'

	try:return quotefile(arg[0],'temp')
	except:return quotefile('','temp')

def bug(string):
	try:
		open("bug.txt", "a").write(string+'\n')
		print('\a')
		try:play('../bug.wav')
		except:pass
		return 'Success!\nhttps://youtu.be/bLHL75H_VEM'
	except:
		return ':/'

def quotefile(line,file):
	l = line.split(' ')
	if l[0] == 'search':return qfsearch(l[1],file)
	if line == '':
		q = c(open(file+".txt", "r").read().split('\n'))
		return q
	q = open(file+".txt", "r").read().split('\n')[int(line)]
	return quotefile('',file) if q=='' else q

def qfsearch(pattern,file):
	p = compile(pattern)
	q = open(file+".txt", "r").read().split('\n')
	l = []
	r = ''
	for i in range(len(q)):
		line = q[i]
		if search(p,line)!=None:l.append((i,line))
	for m in l:
		r+=str(m[0])+' '+m[1]+'\n'
	return 'No Match' if r=='' else r

def zodiac(arg):
	signs = ['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces','coffee']
	signelements = ['Fire (Enthusiasm; drive to express self; faith)','Earth (Practicality; caution; material world)','Air (Communication; socialization; conceptualization)','Water (Emotion; empathy; sensitivity)']
	signqualities= ['Cardinal (active; self-motivated; insightful; ambitious)','Fixed (stabilization; determination; depth; persistence)','Mutable (adaptability; flexibility; sympathy)']
	signrulers= ['Mars','Venus','Mercury','Moon','Sun','Mercury','Venus','Mars','Jupiter','Saturn','Saturn','Jupiter','Starbucks']
	vernal = 6884100

	if len(arg):n = signs.index(arg.lower())
	else:n = int(((time()-vernal)%31556952000)/2629746000); # sign number 0-11

	return '**'+signs[n].title()+'**\nElement: '+signelements[n%4]+'\nQuality: '+signqualities[n%3]+'\nRuler: '+signrulers[n]

def mbti(arg):
	arg = arg[:4].lower()
	ids = (('e','i'),('s','n'),('t','f'),('j','p'))
	idz = (('extroverted','introverted'),('sensing','intuition'),('thinking','feeling'),('judging','perceiving'))

	string = ''
	for i in range(4):
		try:string+=idz[i][ids[i].index(arg[i])]+'\n'
		except (IndexError,ValueError):pass

	try:string+='\nDom: '+functions[arg][0]+'\nAux: '+functions[arg][1]+'\n'
	except (IndexError,KeyError,ValueError):pass

	return '**'+arg.upper()+'**\n```\n'+string+'```\nhttps://www.personalityclub.com/wp-content/uploads/2015/05/'+arg+'-profile.png'

def coffee(arg):
	try:return '```\n'+coffees[arg]+'```'
	except KeyError:return ':/'

def convert(uwaa):
	arg = uwaa.lower().split(' ')

	if arg[1] in religions or arg[2] in religions:return 'No, I meant the **other** kind of convert!'
	
	try:return float(arg[0]) * units[arg[1]] / units[arg[2]]
	except KeyError:return 'invalid unit... did you try using its abbreviation?'

def religion(uwaa):
	try:return '**'+uwaa.title()+'**```\nPart of: '+religions[uwaa]['partof']+'\nMembers: '+str(religions[uwaa]['members'])+'```'+religions[uwaa]['url']
	except KeyError:return ':/'

def xsampa(string):
	for replacement in xskey:
		string = string.replace(replacement[0],replacement[1])
	return string

def pie(string):
	for replacement in piekey:
		string = string.replace(replacement[0],replacement[1])
	return string

def rword(lang,min):
	replace = '\n.?,!0123456789[]()":;'
	if lang == 'la':corpus = open("cdbg.txt", "r").read()
	elif lang == 'fr':corpus = open("lg.txt", "r").read()
	else:corpus = open("bee.txt", "r").read()
	for char in replace:
		corpus = corpus.replace(char,' ')
	corpus = corpus.split(' ')
	while 1:
		attempt = c(corpus).lower()
		if len(attempt)>=min:#obeys min
			if not compile("[^a-z-']").search(attempt):#must only contain a-z, hyphens, or apostrophes
				return attempt
	
def d(m,n):
	if m<0:return -d(-m,n)
	if n<0:return -d(m,-n)
	s = 0
	for i in range(m):
		s+=c(range(n))+1
	return s

def dice(m,n):
	rolls = []
	for i in range(1000):
		rolls += [d(m,n)]
	mean = sum(rolls)/1000
	try:mmmm = str(mode(rolls))
	except:mmmm = 'No Unique Mode'
	ssss = stdev(rolls)
	return '```\nMean: '+str(mean)+'\nMedian: '+str(median(rolls))+'\nMode: '+mmmm+'\nσ: '+str(ssss)+'\n\tm-2σ: '+str(mean-2*ssss)+'\n\tm+2σ: '+str(mean+2*ssss)+'\n\nSample: '+str(d(m,n))+'```'

def dicemat(x):
	x = x.split(' ')
	m = int(x[0])
	n = int(x[1])
	if abs(m)<99>abs(n):return dice(m,n)
	return 'Too High'

# GAMES
	
async def g23(mc):
	timer = 30
	await client.send_message(mc, 'Start guessing! You have **'+str(timer)+'** seconds! Clock starts *now*!~')
	start = time()
	guesses = []
	while time()<start+timer:#30s should be enough
		msg = await client.wait_for_message(timeout=1,channel=mc)
		try:
			guesses.append((float(msg.content),msg.author.name))
			await client.delete_message(msg)
		except:pass
	a1 = list(map(lambda x:x[0],guesses))
	try:
		avg23 = sum(a1)*2/3/len(a1)
		a2 = list(map(lambda x:abs(x-avg23),a1))
		winner = a2.index(min(a2))
		await client.send_message(mc, guesses[winner][1]+', you won with your guess of '+str(guesses[winner][0])+' (2/3 of the mean was actually '+str(avg23)+')! ^o^')
		return False
	except ZeroDivisionError:
		await client.send_message(mc, 'N-nobody??? ;-;')
		return True

async def gtn(args,mc):
	try:
		minn = int(args[1])
		maxn = int(args[2])
	except:
		minn = 0
		maxn = 99
	answer = randint(minn,maxn)
	msg = False
	while 1:
		if msg:
			try:
				if int(msg.content) < answer:
					await client.send_message(mc, '>')
				else:
					await client.send_message(mc, '<')
			except:pass
		else:
			await client.send_message(mc, 'Guess a number between '+str(minn)+' and '+str(maxn)+'!')
		msg = await client.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await client.send_message(mc, 'o oki ;-;')
			return True
		elif msg.content == str(answer):
			await client.send_message(mc, msg.author.name+', you win! ^o^')
			return False
	return True

async def word(args,message):
	mc = message.channel
	try:
		word = args[1].lower()
		await client.delete_message(message)
		if word == 'latin':word = rword('la',1)
	except:word = rword('en',4)
	await client.send_message(mc, 'A new game of **Word** has begun:\n**'+'X'*len(word)+'**')
	while 1:
		msg = await client.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await client.send_message(mc, 'c r i e ;-;\nthe word was **'+word+'**.')
			return True
		pips = ''
		if msg.author.name!='Mobot':
			try:
				guess = msg.content.lower()
				if len(guess) == len(word): # NO CHEATING
					if guess == word:
						await client.send_message(mc, msg.author.name+', you won with your guess of '+guess+'! ^o^')
						return False
					mr = range(min(len(word),len(guess)))
					#look for EXACT matches
					for i in mr:
						if guess[i]==word[i]:pips+='x'
					for i in mr:
						if guess[i] in word and guess[i]!=word[i]:pips+='*'
					await client.send_message(mc, msg.author.name+', your guess of '+guess+' resulted in:\n'+pips)
			except:pass
	return True

async def hangman(args,mc):
	try:lang = args[1]
	except:lang = 'en'
	word = rword(lang,4)
	#print('\t\t'+lang,word)
	known = 'X'*len(word)
	await client.send_message(mc, 'A new game of **Hangman** has begun:\n**'+known+'**')
	fails = 0
	faill = ''
	while fails<10:
		msg = await client.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await client.send_message(mc, 'c r i e ;-;\nthe word was **'+word+'**.')
			return True
		if msg.author.name!='Mobot':
			try:
				guess = msg.content.lower()
				if len(guess) == 1:
					if guess in word:
						#replace letters in known
						for i in range(len(word)):
							if guess == word[i]:
								known = list(known)
								known[i] = guess
								known = ''.join(known)
						#won?
						if 'X' not in known:
							await client.send_message(mc, '**'+msg.author.name+'**, you won! The word was **'+word+'**! ^o^')
							return False
					else:
						fails+=1
						faill+=guess+' '
						await client.send_message(mc, '**'+guess+'** is not in the word.')
				elif guess == word:
					await client.send_message(mc, '**'+msg.author.name+'**, you won! The word was **'+word+'**! ^o^')
					return False
				#display word
				await client.send_message(mc, '**'+known+'**\n'+faill)
			except:pass
	await client.send_message(mc, 'You lost. The word was **'+word+'**. uwu')
	return False

def vrleaderboard(lang,verb,n):
	#[(lang,verb,##,user),...]
	wholelist = list(map(lambda x:(x[0],x[1],int(x[2]),x[3]),map(lambda x:x.split('\t'),open("vrleaderboard.txt", "r").read().split('\n'))))
	#the above is CONFIRMED to work correctly. the problem is below this point
	#find relevant entries
	o = []
	for entry in wholelist:
		if entry[0] == lang and entry[1] == verb:o.append((entry[2],entry[3]))
	#sort by time
	o = sorted(o,key=lambda x:x[0])
	#now turn to text
	oo = ''
	for i in range(min(len(o),n+1)):
		entry = o[i]
		oo+=str(entry[0])+'\t'+entry[1]+'\n'
	return '```\ns \tusername\n'+oo+'```'

async def verbrace(args,mc):
	forms = pronouns[args[1]]
	word = c(verbs[args[1]])
	limit = 30
	await client.send_message(mc, 'A new game of **Verb Race** has begun! You have **'+str(limit)+'** seconds to type `join`!')
	form = 0
	start = time()
	players = []
	finalform = len(forms)
	while time()<start+limit:
		msg = await client.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() == 'join' and msg.author.name!='Mobot':
				players.append(msg.author)
				await client.delete_message(msg)
				await client.send_message(mc, '**'+msg.author.name+'** has joined!')
		except:pass
	if len(players)<finalform: # for small games
		players = players*ceil(finalform/len(players))
	shuffle(players)
	pbu = players[:] # player backup
	choice = False
	start = time()
	await client.send_message(mc, 'A new game of **Verb Race** has begun!\nYour verb is: **'+word[finalform]+'**!')
	allcorrect = True
	while form<finalform:
		if choice:
			msg = await client.wait_for_message(channel=mc)
			if msg.content.lower() in quit and msg.author in players:
				await client.send_message(mc, 'c r i e ;-;')
				break#return True
			elif msg.author == choice:
				await client.delete_message(msg)
				if msg.content == word[form]:
					await client.send_message(mc, 'Correct!')
				else:
					await client.send_message(mc, 'Incorrect! The correct form was **'+word[form]+'**')
					allcorrect = False
				form+=1
				choice = False
		else:
			choice = players.pop()
			await client.send_message(mc, '**'+choice.name+'**, conjugate **'+word[finalform]+'** for **'+forms[form]+'**!')
	await client.send_message(mc, 'The game of **Verb Race** has ended! You took '+str(int(time()-start))+' seconds!')
	#check to see if eligible for leaderboard
	if allcorrect and len(set(pbu[:finalform])) == 1:
		open("vrleaderboard.txt", "a").write('\n'+'\t'.join([args[1],word[finalform],str(int(time()-start)),pbu[0].name]))
	#print leaders
	await client.send_message(mc, 'Leaderboard for **'+word[finalform]+'**:\n'+vrleaderboard(args[1],word[finalform],5))
	return False

async def numbers(mc):
	limit = 45
	ops = '+-*/'
	minn = 2
	maxn = 20
	nn = 6
	ns = []
	for i in range(nn):
		ns.append(randint(minn,maxn))
	target = 0.5
	whatsthis = ' '.join(map(str,ns))
	while target != int(target) or target>1000 or target<10:
		owo = whatsthis
		for i in range(len(ns)-1):
			owo += c(ops)
		target = mocharpn.rpn(owo)[0]
	# now a valid target is established
	target = int(target)
	#shuffle again to prevent exploit
	shuffle(ns)
	#Begin!
	await client.send_message(mc, 'A new game of **Numbers** has begun!\nYour target is **'+str(target)+'**, and your numbers are **'+' '.join(map(str,ns))+'**!')
	await client.send_message(mc, 'You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time()<start+limit:
		msg = await client.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() in quit:
				await client.send_message(mc, 'c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name!='Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await client.delete_message(msg)
					await client.send_message(mc, '**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await client.send_message(mc, 'u already gone shoo shoo')
		except AttributeError:pass
		if time()+5>start+limit and not warned:
			await client.send_message(mc, 'You have **5** seconds left to solve!')
			warned = True
	await client.send_message(mc, 'The game of **Numbers** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await client.send_message(mc, guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await client.send_message(mc, 'The Math Corner notes that **'+str(target)+'** was achievable using the following solution:\n`'+owo+'`')
	return False

async def twentyfour(mc):
	limit = 30
	ops = '+-*/'
	#generate numbers until it works dammit
	target = 0
	while target!=24:
		start = time()
		ns = []
		for i in range(4):
			ns.append(randint(1,10))
		whatsthis = ' '.join(map(str,ns))
		while target != 24:
			owo = whatsthis
			for i in range(len(ns)-1):
				owo += c(ops)
			target = mocharpn.rpn(owo)[0]
			if time()-start>1:break
	# now a valid sample is established
	#Begin!
	await client.send_message(mc, 'A new game of **24** has begun!\nYour numbers are **'+whatsthis+'**!')
	await client.send_message(mc, 'You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time()<start+limit:
		msg = await client.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() in quit:
				await client.send_message(mc, 'c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name!='Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await client.delete_message(msg)
					await client.send_message(mc, '**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await client.send_message(mc, 'u already gone shoo shoo')
		except AttributeError:pass
		if time()+5>start+limit and not warned:
			await client.send_message(mc, 'You have **5** seconds left to solve!')
			warned = True
	await client.send_message(mc, 'The game of **24** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await client.send_message(mc, guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await client.send_message(mc, 'The Math Corner notes that **24** was achievable using the following solution:\n`'+owo+'`')
	return False

async def llama(message):
	mc = message.channel
	room = -1
	state = 0
	inv = False
	await client.send_message(message.channel, 'A new emulation of **Llama Adventure** has been initiated! Type anything to begin, and have fun!~ ^_^')
	while 1:
		msg = await client.wait_for_message(channel=mc,author=message.author)
		if room == -1 == state:return True # exit
		ml = mochallama.llama(room,state,inv,msg)
		await client.send_message(mc, ml[3])
		room = ml[0]
		state = ml[1]
	return False

# ACUTAL BOT SHIT

bot_prefix = "m! "
token = open("../token.txt", "r").read()

client = Bot(command_prefix = bot_prefix)

@client.event
async def on_message(message):
	global lastmessage
	m = message.content
	n = m.lower()
	try:qf = n.split(' ')
	except: qf = False

	if message.content.startswith(bot_prefix):
		loglook = str(message.timestamp)[:19]+' - @'+str(message.author)+' (#'+str(message.channel)+' in '+str(message.server)+')\n\t'+message.content
		try:print(loglook)
		except UnicodeEncodeError:
			try:print(str(message.timestamp)[:19]+'\n\t'+message.content)
			except UnicodeEncodeError:print(str(message.timestamp)[:19]+' [Unable to read message]')
		try:open("log.txt", "a").write(loglook+'\n')
		except UnicodeEncodeError as e:open("log.txt", "a").write(str(e)+'\n')

	try:
		if 'right, mobot' in m.lower() or 'right mobot' in m.lower():
			try:await client.send_message(message.channel, c(['ya!~','ofc!~','yayaya ^3^']))
			except:pass
		elif 'mobot' in m.lower() and message.author.name!='Mobot':
			try:await client.send_message(message.channel, c(['das meee :3','hai!~']))
			except:pass

		mc = message.channel

		if n == 'owo':
			await client.send_message(mc, '*What\'s this???*')
		# MAIN
		elif n.startswith(bot_prefix+'help'):
			await client.send_message(mc, help(m[8:]))
		elif n.startswith(bot_prefix+'bf'):
			args = m[6:].split('\n')
			await client.send_message(mc, str(mochabf.run(args[0],args[1:])))
		elif n.startswith(bot_prefix+'gs'):
			await client.send_message(mc, str(mochagolfscript.run(m[6:])))
		elif n.startswith(bot_prefix+'ast'):
			await client.send_message(mc, str(moastro(m[7:])))
		elif n.startswith(bot_prefix+'bug'):
			await client.send_message(mc, str(bug(m[7:])))
		elif n.startswith(bot_prefix+'mat'):
			await client.send_message(mc, str(momath(m[7:])))
		elif n.startswith(bot_prefix+'rpn'):
			await client.send_message(mc, str(mocharpn.rpn(m[7:])))
		elif n.startswith(bot_prefix+'ttt'):
			await client.send_message(mc, str(mochattt.ai(m[7:])))
		elif n.startswith(bot_prefix+'dice'):
			await client.send_message(mc, str(dicemat(m[8:])))
		elif n.startswith(bot_prefix+'ling'):
			await client.send_message(mc, str(moling(m[8:])))
		elif n.startswith(bot_prefix+'mbti'):
			await client.send_message(mc, str(mbti(m[8:])))
		elif n.startswith(bot_prefix+'time'):
			args = m[8:].split(' ')
			if args[0] == 'taken':
				await client.send_message(mc, 'm! time diff')
				lastmessage = message
			elif n == 'm! time diff' and message.author.name == 'Mobot':
				await client.edit_message(message,'Calculating...')
				sleep(1)
				old = lastmessage.timestamp.replace(tzinfo=timezone.utc).timestamp()
				new = message.timestamp.replace(tzinfo=timezone.utc).timestamp()
				await client.edit_message(message,str(int((new-old)*1000))+' ms')
			else:
				await client.send_message(mc, str(message.timestamp)[:19]+' UTC')
		elif n.startswith(bot_prefix+'quote'):
			await client.send_message(mc, str(sto(m[9:])))
		elif n.startswith(bot_prefix+'zodiac'):
			await client.send_message(mc, str(zodiac(m[10:])))
		elif n.startswith(bot_prefix+'coffee'):
			await client.send_message(mc, str(coffee(m[10:])))
		elif n.startswith(bot_prefix+'convert'):
			await client.send_message(mc, str(convert(m[11:])))
		elif n.startswith(bot_prefix+'religion'):
			await client.send_message(mc, str(religion(m[12:])))
		# QUOTES
		elif qf[0]=='m!' and qf[1] in quotefiles:
			await client.send_message(mc, quotefile(m[4+len(qf[1]):],qf[1]))
		# GAMES
		elif n.startswith(bot_prefix+'game'):
			args = n.split(' ')[2:]
			if args[0] == '24':
				await twentyfour(mc)
			elif args[0] == 'gtn':
				await gtn(args,mc)
			elif args[0] == 'g2/3':
				await g23(mc)
			elif args[0] == 'hangman':
				await hangman(args,mc)
			elif args[0] == 'llama':
				await llama(message)
			elif args[0] == 'numbers':
				await numbers(mc)
			elif args[0] == 'verbrace':
				await verbrace(args,mc)
			elif args[0] == 'word':
				await word(args,message)

		# ELSE
		elif n.startswith(bot_prefix):
			try:await client.send_message(message.channel, special[m[3:].lower()]) # specials
			except KeyError:await client.send_message(message.channel,'me confufu uwu')
	except discord.errors.Forbidden:pass

print('Loaded')
client.run(token)
