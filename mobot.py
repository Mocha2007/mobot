from discord.ext.commands import Bot
from discord.ext import commands
import discord

from datetime import timezone
from random import choice as c
from random import randint,shuffle
from math import ceil,gcd,hypot,pi
from time import time,sleep
from re import compile,findall,search,sub
from statistics import median,mode,stdev
from winsound import PlaySound,SND_FILENAME
import mochaastro,mochabf,mochagolfscript,mochalang,mochallama,mochamath,mocharpn,mochastargen,mochattt,mochamw,mochaweb,mochaweather,moclimate
from mochaxyz import *

# CODE SHIT
def help(command):
	'''help'''
	if command == '':return open("help2.txt", "r").read()
	doc = open("help.txt", "r").read() #reload docs
	doclines = doc.split('\n')
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

	if arg[0] == 'delay':
		c = 299792458
		try:a1 = object[arg[1]]['a']
		except:a1 = 0
		try:a2 = object[arg[2]]['a']
		except:a2 = 0
		bigd = (a1+a2)/c
		littled = abs(a1-a2)/c
		seconds = 'Between '+str(int(littled))+' and '+str(ceil(bigd))+' seconds'
		if bigd<60:return seconds
		bigdm = ceil(bigd/60)
		littledm = int(littled/60)
		minutes = ';\nBetween '+str(int(littledm))+' and '+str(ceil(bigdm))+' minutes'
		if bigdm<60:return seconds+minutes
		bigdh = ceil(bigdm/60)
		littledh = int(littledm/60)
		hours = ';\nBetween '+str(littledh)+' and '+str(bigdh)+' hours'
		return seconds+minutes+hours
	elif arg[0] == 'density' or arg[0] == 'rho':
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
	elif arg[0] == 'horizons':
		try:return ('```\n'+mochaweb.horizons(arg[1])[:1992]+'\n```')
		except EOFError:return 'unable to connect'
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
		return mochaastro.soi(m,M,a)
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

def lf(x):
	l = mochalang.sortdict(mochalang.letterfreq(x))
	s = '```\n'
	for i in l:
		s+=i[0]+' '+str(i[1])+'\n'
	return s+'```'

def moling(string):
	arg = string.split(' ')

	if arg[0] == 'freq':
		sss = ' '.join(arg[1:]).lower()
		ppp = compile('[^a-z]')
		return lf(sub(ppp,'',sss))
	elif arg[0] == 'freq2':
		return lf(' '.join(arg[1:]))
	elif arg[0] == 'ipa':
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
	elif arg[0] == 'morse':
		try:return mochalang.morse(arg[1])
		except:return 'https://en.wikipedia.org/wiki/Morse_code'
	elif arg[0] == 'pie':
		try:return pie(arg[1])
		except:return 'https://en.wikipedia.org/wiki/Proto-Indo-European_phonology'
	elif arg[0] == 'scrabble':
		try:m = int(arg[2])
		except:m = 1
		return mochalang.scrabble(arg[1])*m
	elif arg[0] == 'soundex':
		return mochalang.soundex(arg[1])
	elif arg[0] == 'romanize':
		return mochalang.romanize(' '.join(arg[1:]))
	elif arg[0] == 'unmojibake':
		try:return mochalang.unmojibake(' '.join(arg[1:]),'windows-1252','utf-8')
		except UnicodeDecodeError:return 'Invalid... probably missing some characters?'
		except:return 'Invalid... just really, really invalid.'
	elif arg[0] == 'x-sampa' or arg[0] == 'xsampa':
		try:return xsampa(arg[1])
		except:return 'https://en.wikipedia.org/wiki/X-SAMPA'

	return ':/'

def trivia(string):
	arg = string.split(' ')
	try:
		x = int(arg[0])
		number = True
	except:number = False

	if number:
		return mochaweb.numbersapi(arg[0])
	elif arg[0] == 'number':
		try:
			x = int(arg[1])
			try:return mochaweb.numbersapi(arg[1])
			except:pass
		except:pass

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
		if len(inputendo) == 0:return 'Not happening.'
		for line in open("temp.txt", "r").read():
			if inputendo == line:return 'Quote Already Stored.'
		open("temp.txt", "a").write('\n'+inputendo)
		return 'Success!'

	try:return quotefile(arg[0],'temp')
	except:return quotefile('','temp')

def bug(string):
	try:
		open("bug.txt", "a").write('\n'+string)
		try:play('../bug.wav')
		except:print('\a')
		return 'Success!\nhttps://youtu.be/bLHL75H_VEM'
	except:
		return ':/'

def quotefile(line,file):
	l = line.split(' ')
	if l[0].lower() == 'search':return qfsearch(' '.join(l[1:]),file)
	if line == '':
		q = c(open(file+".txt", "r").read().split('\n'))
		return q
	try:q = open(file+".txt", "r").read().split('\n')[int(line)]
	except IndexError:return 'That line is not present in the document.'
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
		mmatch = m[1]
		for mmmatch in findall(p,mmatch):
			mmatch = mmatch.replace(mmmatch,'**'+mmmatch+'**')
		r+=str(m[0])+' '+mmatch+'\n'
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
	maxrolls = 10000
	rolls = []
	for i in range(maxrolls):
		rolls += [d(m,n)]
	mean = sum(rolls)/maxrolls
	try:mmmm = str(mode(rolls))
	except:mmmm = 'No Unique Mode'
	ssss = stdev(rolls)
	return '```\nMin: '+str(m)+'\nMax: '+str(m*n)+'\nMean: '+str(mean)+'\nMedian: '+str(median(rolls))+'\nMode: '+mmmm+'\nσ: '+str(ssss)+'\n\tm-2σ: '+str(mean-2*ssss)+'\n\tm+2σ: '+str(mean+2*ssss)+'\n\nSample: '+str(d(m,n))+'```'

def dicemat(x):
	x = x.split(' ')
	try:
		m = int(x[0])
		n = int(x[1])
		if abs(m)<99>abs(n):return dice(m,n)
		return 'Too High'
	except:return 'Space-separated!'

def gp(x):
	args = x.split(' ')
	try:
		gold = float(args[0])
		ways = float(args[1])
	except:return 'if you need help: `m! help gp`'
	if ways == 0:return 'Zero ways, eh?'
	quotient = str(round(gold/ways,2)).split('.')
	g = quotient[0]
	try:s = quotient[1][0]
	except:s = '0'
	try:c = quotient[1][1]
	except:c = '0'
	return g+'g '+s+'s '+c+'c'

# GAMES
	
async def g23(mc):
	timer = 30
	await bot.send_message(mc, 'Start guessing! You have **'+str(timer)+'** seconds! Clock starts *now*!~')
	start = time()
	guesses = []
	while time()<start+timer:#30s should be enough
		msg = await bot.wait_for_message(timeout=1,channel=mc)
		try:
			guesses.append((float(msg.content),msg.author.name))
			await bot.delete_message(msg)
		except:pass
	a1 = list(map(lambda x:x[0],guesses))
	try:
		avg23 = sum(a1)*2/3/len(a1)
		a2 = list(map(lambda x:abs(x-avg23),a1))
		winner = a2.index(min(a2))
		await bot.send_message(mc, guesses[winner][1]+', you won with your guess of '+str(guesses[winner][0])+' (2/3 of the mean was actually '+str(avg23)+')! ^o^')
		return False
	except ZeroDivisionError:
		await bot.send_message(mc, 'N-nobody??? ;-;')
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
					await bot.send_message(mc, '>')
				else:
					await bot.send_message(mc, '<')
			except:pass
		else:
			await bot.send_message(mc, 'Guess a number between '+str(minn)+' and '+str(maxn)+'!')
		msg = await bot.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await bot.send_message(mc, 'o oki ;-;')
			return True
		elif msg.content == str(answer):
			await bot.send_message(mc, msg.author.name+', you win! ^o^')
			return False
	return True

async def word(args,message):
	mc = message.channel
	try:
		word = args[1].lower()
		await bot.delete_message(message)
		if word == 'latin':word = rword('la',1)
	except:word = rword('en',4)
	await bot.send_message(mc, 'A new game of **Word** has begun:\n**'+'X'*len(word)+'**')
	while 1:
		msg = await bot.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await bot.send_message(mc, 'c r i e ;-;\nthe word was **'+word+'**.')
			return True
		pips = ''
		if msg.author.name!='Mobot':
			try:
				guess = msg.content.lower()
				if len(guess) == len(word): # NO CHEATING
					if guess == word:
						await bot.send_message(mc, msg.author.name+', you won with your guess of '+guess+'! ^o^')
						mochagive(5,msg.author.name.lower())
						return False
					mr = range(min(len(word),len(guess)))
					#look for EXACT matches
					for i in mr:
						if guess[i]==word[i]:pips+='x'
					for i in mr:
						if guess[i] in word and guess[i]!=word[i]:pips+='*'
					await bot.send_message(mc, msg.author.name+', your guess of '+guess+' resulted in:\n'+pips)
			except:pass
	return True

async def hangman(args,mc):
	try:lang = args[1]
	except:lang = 'en'
	word = rword(lang,4)
	#print('\t\t'+lang,word)
	known = 'X'*len(word)
	await bot.send_message(mc, 'A new game of **Hangman** has begun:\n**'+known+'**')
	fails = 0
	faill = ''
	while fails<10:
		msg = await bot.wait_for_message(channel=mc)
		if msg.content.lower() in quit:
			await bot.send_message(mc, 'c r i e ;-;\nthe word was **'+word+'**.')
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
							await bot.send_message(mc, '**'+msg.author.name+'**, you won! The word was **'+word+'**! ^o^')
							mochagive(1,msg.author.name.lower())
							return False
					else:
						fails+=1
						faill+=guess+' '
						await bot.send_message(mc, '**'+guess+'** is not in the word.')
				elif guess == word:
					await bot.send_message(mc, '**'+msg.author.name+'**, you won! The word was **'+word+'**! ^o^')
					return False
				#display word
				await bot.send_message(mc, '**'+known+'**\n'+faill)
			except:pass
	await bot.send_message(mc, 'You lost. The word was **'+word+'**. uwu')
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
	await bot.send_message(mc, 'A new game of **Verb Race** has begun! You have **'+str(limit)+'** seconds to type `join`!')
	form = 0
	start = time()
	players = []
	finalform = len(forms)
	while time()<start+limit:
		msg = await bot.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() == 'join' and msg.author.name!='Mobot':
				players.append(msg.author)
				await bot.delete_message(msg)
				await bot.send_message(mc, '**'+msg.author.name+'** has joined!')
		except:pass
	if len(players)<finalform: # for small games
		players = players*ceil(finalform/len(players))
	shuffle(players)
	pbu = players[:] # player backup
	choice = False
	start = time()
	await bot.send_message(mc, 'A new game of **Verb Race** has begun!\nYour verb is: **'+word[finalform]+'**!')
	allcorrect = True
	while form<finalform:
		if choice:
			msg = await bot.wait_for_message(channel=mc)
			if msg.content.lower() in quit and msg.author in players:
				await bot.send_message(mc, 'c r i e ;-;')
				break#return True
			elif msg.author == choice:
				await bot.delete_message(msg)
				if msg.content == word[form]:
					await bot.send_message(mc, 'Correct!')
				else:
					await bot.send_message(mc, 'Incorrect! The correct form was **'+word[form]+'**')
					allcorrect = False
				form+=1
				choice = False
		else:
			choice = players.pop()
			await bot.send_message(mc, '**'+choice.name+'**, conjugate **'+word[finalform]+'** for **'+forms[form]+'**!')
	await bot.send_message(mc, 'The game of **Verb Race** has ended! You took '+str(int(time()-start))+' seconds!')
	#check to see if eligible for leaderboard
	if allcorrect and len(set(pbu[:finalform])) == 1:
		mochagive(1,pbu[0].name.lower())
		open("vrleaderboard.txt", "a").write('\n'+'\t'.join([args[1],word[finalform],str(int(time()-start)),pbu[0].name]))
	#print leaders
	await bot.send_message(mc, 'Leaderboard for **'+word[finalform]+'**:\n'+vrleaderboard(args[1],word[finalform],5))
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
	await bot.send_message(mc, 'A new game of **Numbers** has begun!\nYour target is **'+str(target)+'**, and your numbers are **'+' '.join(map(str,ns))+'**!')
	await bot.send_message(mc, 'You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time()<start+limit:
		msg = await bot.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() in quit:
				await bot.send_message(mc, 'c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name!='Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await bot.delete_message(msg)
					await bot.send_message(mc, '**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await bot.send_message(mc, 'u already gone shoo shoo')
		except AttributeError:pass
		if time()+5>start+limit and not warned:
			await bot.send_message(mc, 'You have **5** seconds left to solve!')
			warned = True
	await bot.send_message(mc, 'The game of **Numbers** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await bot.send_message(mc, guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await bot.send_message(mc, 'The Math Corner notes that **'+str(target)+'** was achievable using the following solution:\n`'+owo+'`')
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
	await bot.send_message(mc, 'A new game of **24** has begun!\nYour numbers are **'+whatsthis+'**!')
	await bot.send_message(mc, 'You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time()<start+limit:
		msg = await bot.wait_for_message(channel=mc,timeout=1)
		try:
			if msg.content.lower() in quit:
				await bot.send_message(mc, 'c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name!='Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await bot.delete_message(msg)
					await bot.send_message(mc, '**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await bot.send_message(mc, 'u already gone shoo shoo')
		except AttributeError:pass
		if time()+5>start+limit and not warned:
			await bot.send_message(mc, 'You have **5** seconds left to solve!')
			warned = True
	await bot.send_message(mc, 'The game of **24** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await bot.send_message(mc, guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await bot.send_message(mc, 'The Math Corner notes that **24** was achievable using the following solution:\n`'+owo+'`')
	return False

async def llama(message):
	mc = message.channel
	room = -1
	state = 0
	inv = False
	await bot.send_message(message.channel, 'A new emulation of **Llama Adventure** has been initiated! Type anything to begin, and have fun!~ ^_^')
	while 1:
		msg = await bot.wait_for_message(channel=mc,author=message.author)
		if room == -1 == state:return True # exit
		ml = mochallama.llama(room,state,inv,msg)
		await bot.send_message(mc, ml[3])
		room = ml[0]
		state = ml[1]
	return False

mochaid = open('../mocha.txt','r').read()
def bankwrite(bank):
	bank[mochaid] = 0
	s = ''
	for account in bank:
		s+='\n'+account+'\t'+str(bank[account])
	open("bank.txt", "w").write(s[1:])

def mochagive(amt,acct):
	file = open("bank.txt", "r").read().split('\n')
	bank = {}
	for line in file:
		l = line.split('\t')
		bank[l[0]]=int(l[1])
	try:bank[acct] += amt
	except:bank[acct] = amt
	bankwrite(bank)

def mochapoint(message):
	id = message.author.id
	string = ' '.join(message.content.lower().split(' ')[2:])
	#["user\t$",...]
	file = open("bank.txt", "r").read().split('\n')
	bank = {}
	for line in file:
		l = line.split('\t')
		bank[l[0]]=int(l[1])
	bank[mochaid] = float('inf')
	#string edit
	subcommand = string.split(' ')
	if subcommand[0][:3] == 'bal':
		if id == mochaid:return 'https://youtu.be/7sWpSvQ_hwo'
		try:return message.author.name+': **'+str(bank[id])+'**'
		except:# not in there
			open("bank.txt", "a").write('\n'+id+'\t0')
			return message.author.name+': **0**'
	elif subcommand[0][:3] == 'eco': # ADD DOX
		summation = 0
		for acct in bank:
			if acct!=mochaid:summation += bank[acct]
		try:percent = str(round(int(bank[id])/summation*100,2))
		except:percent = '0'
		return '**'+str(summation)+'** mokis in circulation\nYou own **'+percent+'**%'
	elif subcommand[0][:3] == 'giv':
		try:
			tgt = subcommand[1][3:-1]
			int(tgt)
		except:return 'Invalid user'
		if id == tgt:return '...no.'
		try:
			amt = int(subcommand[2])
			if amt<1:raise ValueError('SKREE')
			try:
				bank[id] -= amt
				if bank[id]<0:raise ValueError('SKREE')
				try:bank[tgt] += amt
				except:bank[tgt] = amt
				bankwrite(bank)
				return 'Successfully transfered **'+str(amt)+'** mokis to user!'
			except:return 'Insufficient Funds'
		except:return 'Invalid Amount; require a natural number.'
	elif subcommand[0] == 'help': # ADD DOX
		return '*Mokis* are used to purchase **bragging rights**... or someshit.\nRewards are given by `m! word`, `m! hangman`, and `m! verbrace`.'

	return ':/'

# ACTUAL BOT SHIT
bot_prefix = "m!"
token = open("../token.txt", "r").read()

bot = Bot(command_prefix = bot_prefix)

@bot.event
async def on_ready():
	print(bot.user.name+' loaded.')

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	global anchor
	global lastmessage
	m = message.content
	mc = message.channel
	n = m.lower()
	ma = m.split(' ')
	na = n.split(' ')
	#quotefile
	try:qfcondition = na[0]=='m!' and na[1] in quotefiles
	except:qfcondition = False
	#GOAT
	try:
		gchelp = 'which' if 'which' in n else ('what' if 'what' in n else 0),'best' if 'best' in n else ('greatest' if 'greatest' in n else 0)
		goatcondition = gchelp[0] and 'bot' in n and 'is' in n and gchelp[1]
		if 'mobot' in n:
			goatcondition = n.index(gchelp[0]) < n.index('is') < n.index(gchelp[1])
		else:
			goatcondition = n.index(gchelp[0]) < n.index('bot') < n.index('is') < n.index(gchelp[1])
			goatcondition = goatcondition or (n.index(gchelp[0]) < n.index('is') < n.index(gchelp[1]) < n.index('bot'))
	except: goatcondition = False

	try:
		notmobot = message.author.name!='Mobot'
		if notmobot:
			if ('right, mobot' in n or 'right mobot' in n): #needed due to multiple responses
				try:await bot.send_message(mc, c(mobotyes))
				except:pass
			elif 'mobot irl' in n: #needed due to multiple responses
				try:await bot.send_message(mc, c(mobotirl))
				except:pass
			elif goatcondition: #needed due to complicated conditions
				try:await bot.send_message(mc, c(['MOBOT IS GOAT\nhttps://www.youtube.com/watch?v=wsj0XFdmxZ0']))
				except:pass
			else: #special triggers
				for i in specialer:
					ret = compile('^'+i+'$|^'+i+'\\W|\\W'+i+'$|\\W'+i+'\\W')
					if search(ret,n):
						try:await bot.send_message(mc, specialer[i])
						except:pass
						break
		#real commands
		if na[0] == bot_prefix and len(na)>1:
			#logging
			loglook = str(message.timestamp)[:19]+' - @'+str(message.author)+' (#'+str(mc)+' in '+str(message.server)+')\n\t'+m
			loglook = sub(compile(r'[^!-~\s]'),'?',loglook)
			print(loglook)
			open("log.txt", "a").write(loglook+'\n')
			#find command
			if na[1] == 'help':
				await bot.send_message(mc, help(m[8:]))
			elif na[1] == 'bf':
				args = m[6:].split('\n')
				await bot.send_message(mc, str(mochabf.run(args[0],args[1:])))
			elif na[1] == 'gs':
				await bot.send_message(mc, str(mochagolfscript.run(m[6:])))
			elif na[1] == 'gp':
				await bot.send_message(mc, gp(m[6:]))
			elif na[1] == 'dfprop':
				entry = m[10:].replace(' ','%20')
				try:await bot.send_message(mc, mochaweb.dfprop(entry))
				except:await bot.send_message(mc, 'Can\'t seem to fetch properties for '+m[10:])
			elif na[1] == 'df':
				entry = m[6:].replace(' ','%20')
				try:await bot.send_message(mc, mochamw.main2('dwarffortresswiki.org','DF2014:'+entry))
				except:await bot.send_message(mc, 'Can\'t seem to fetch article for '+m[6:])
			elif na[1] == 'mc':
				entry = m[6:].replace(' ','%20')
				try:await bot.send_message(mc, mochamw.main('minecraft.gamepedia.com',entry))
				except:await bot.send_message(mc, 'Can\'t seem to fetch article for '+m[6:])
			elif na[1] == 'sc2':
				entry = m[7:].replace(' ','%20')
				try:await bot.send_message(mc, mochamw.main('liquipedia.net/starcraft2',entry))
				except:await bot.send_message(mc, 'Can\'t seem to fetch article for '+m[7:])
			elif na[1] == 'ud':
				try:await bot.send_message(mc, mochaweb.ud(m[6:]))
				except:await bot.send_message(mc, 'Can\'t seem to fetch entry for '+m[6:])
			elif na[1] == 'wc':
				entry = m[6:].replace(' ','%20')
				try:await bot.send_message(mc, mochaweb.wtcleanup(mochamw.main('en.wikibooks.org/w','Cookbook:'+entry)))
				except:await bot.send_message(mc, 'Can\'t seem to fetch recipe for '+m[6:])
			elif na[1] == 'wt':
				entry = m[6:].replace(' ','%20')
				try:await bot.send_message(mc, mochaweb.wtcleanup(mochamw.main('en.wiktionary.org/w',entry)))
				except:await bot.send_message(mc, 'Can\'t seem to fetch entry for '+m[6:])
			elif na[1] == 'ast':
				await bot.send_message(mc, str(moastro(m[7:])))
			elif na[1] == 'bug':
				await bot.send_message(mc, str(bug(m[7:])))
			elif na[1] == 'mat':
				await bot.send_message(mc, str(momath(m[7:])))
			elif na[1] == 'rpn':
				await bot.send_message(mc, str(mocharpn.rpn(m[7:])))
			elif na[1] == 'ttt':
				await bot.send_message(mc, str(mochattt.ai(m[7:])))
			elif na[1] == 'dice':
				await bot.send_message(mc, str(dicemat(m[8:])))
			elif na[1] == 'ling':
				await bot.send_message(mc, str(moling(m[8:])))
			elif na[1] == 'mbti':
				await bot.send_message(mc, str(mbti(m[8:])))
			elif na[1] == 'time':
				if na[2] == 'taken':
					await bot.send_message(mc, 'm! time diff')
					lastmessage = message
				elif n == 'm! time diff' and message.author.name == 'Mobot':
					await bot.edit_message(message,'Calculating...')
					sleep(1)
					old = lastmessage.timestamp.replace(tzinfo=timezone.utc).timestamp()
					new = message.timestamp.replace(tzinfo=timezone.utc).timestamp()
					await bot.edit_message(message,str(int((new-old)*1000))+' ms')
				else:
					await bot.send_message(mc, str(message.timestamp)[:19]+' UTC')
			elif na[1] == 'xkcd':
				try:await bot.send_message(mc, mochaweb.xkcd(m[8:]))
				except:await bot.send_message(mc, 'Can\'t seem to fetch comic #'+m[8:])
			elif na[1] == 'wiki':
				entry = m[8:].replace(' ','%20')
				try:await bot.send_message(mc, mochaweb.wikicleanup(mochamw.main('en.wikipedia.org/w',entry)))
				except:await bot.send_message(mc, 'Can\'t seem to fetch article for '+m[8:])
			elif na[1] == 'quote':
				await bot.send_message(mc, str(sto(m[9:])))
			elif na[1] == 'phoon':
				try:await bot.send_message(mc, mochaweather.phoon())
				except:await bot.send_message(mc, 'Can\'t seem to fetch current lunar phase')
			elif na[1] == 'quake':
				try:await bot.send_message(mc, mochaweather.quake())
				except:await bot.send_message(mc, 'Can\'t seem to fetch earthquake information')
			elif na[1] == 'solve':
				await bot.send_message(mc, mocharpn.infix(m[9:]))
			elif na[1] == 'zodiac':
				await bot.send_message(mc, str(zodiac(m[10:])))
			elif na[1] == 'coffee':
				await bot.send_message(mc, str(coffee(m[10:])))
			elif na[1] == 'trivia':
				await bot.send_message(mc, str(trivia(m[10:])))
			elif na[1] == 'secret':
				await bot.send_message(mc, '**'+str(len(quotefiles)+len(special)+len(specialer))+'** secret commands, of which:\n\n**'+str(len(specialer))+'** are triggered by a string,\n**'+str(len(special))+'** are triggered by `m!`, and\n**'+str(len(quotefiles))+'** are triggered by `m!` and an optional argument.')
			elif na[1] == 'convert':
				await bot.send_message(mc, str(convert(m[11:])))
			elif na[1] == 'weather':
				try:await bot.send_message(mc, mochaweather.main(m[11:]))
				except:await bot.send_message(mc, 'Can\'t seem to fetch weather for '+m[11:])
			elif na[1] == 'hurricane':
				try:await bot.send_message(mc, mochaweather.hurricane(m[13:]))
				except:await bot.send_message(mc, 'Can\'t seem to fetch hurricane advisories')
			elif na[1] == 'religion':
				await bot.send_message(mc, str(religion(m[12:])))
			elif na[1] == 'worldgen':
				moclimate.wg(m[12:])
				await bot.send_file(mc,'img/temp.png')
			elif na[1][:4] == 'moki':
				await bot.send_message(mc, mochapoint(message))
			# SECRET DEBUG
			elif na[1] == 'anchor' and message.author.name=='mocha':
				anchor = mc
				await bot.delete_message(message)
			elif na[1] == 'torpedo' and message.author.name=='mocha':
				await bot.send_message(anchor,m[11:])
				await bot.delete_message(message)
			# QUOTES
			elif qfcondition:
				o = quotefile(' '.join(ma[2:]),ma[1].lower())
				try:await bot.send_message(mc,o)
				except discord.errors.HTTPException:await bot.send_message(mc,'Too many matches ('+str(o.count('\n'))+')')
			# GAMES
			elif na[1] == 'game':
				args = n.split(' ')[2:]
				if na[2] == '24':
					await twentyfour(mc)
				elif na[2] == 'gtn':
					await gtn(args,mc)
				elif na[2] == 'g2/3':
					await g23(mc)
				elif na[2] == 'hangman':
					await hangman(args,mc)
				elif na[2] == 'llama':
					await llama(message)
				elif na[2] == 'numbers':
					await numbers(mc)
				elif na[2] == 'verbrace':
					await verbrace(args,mc)
				elif na[2] == 'word':
					await word(args,message)
			# ELSE
			elif n.startswith(bot_prefix):
				try:await bot.send_message(mc, special[m[3:].lower()]) # specials
				except KeyError:await bot.send_message(mc,'me confufu uwu')
			# $
	except discord.errors.Forbidden:pass

print('Connecting...')
bot.run(token)