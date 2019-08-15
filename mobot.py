from discord.ext.commands import Bot
import discord

from datetime import timezone
from random import choice as c, randint, seed, shuffle
from math import ceil, gcd, hypot, pi
from time import time, sleep
from re import compile, findall, search, sub
from statistics import median, mode, StatisticsError, stdev
from winsound import PlaySound, SND_FILENAME
# noinspection PyUnresolvedReferences
import mochaastro, mochabf, mochagolfscript, mochalang, mochallama, mochamath, mocharpn, mochastargen, mochattt, mochamw
import mochaweb, mochaweather, moclimate, mochatest, hello
from mochaxyz import *


# CODE SHIT
def help_function(command: str) -> str:
	"""Help"""
	if command == '':
		return open("help2.txt", "r").read()
	doc = open("help.txt", "r").read() # reload docs
	doclines = doc.split('\n')
	clen = len(command)
	relevant = '```\n'
	# try to find command
	depth = 0 # to prevent UnboundLocalError on a wrong command
	i, lastmajor = 0, ''
	for i in range(len(doclines)):
		line = doclines[i]
		if line[0] != '\t':
			lastmajor = line
		if line[:clen] == command: # MAJOR command, not minor
			depth = 1
			break
		elif line[:clen+1] == '\t'+command: # MINOR command, not major
			depth = 2
			break
	if depth > 1:
		relevant += lastmajor+'\n' # print overcommand
	while 1:
		relevant += doclines[i]+'\n'
		i += 1
		try:
			if doclines[i][:depth] != '\t'*depth:
				break # must be another command or end
		except IndexError:
			break
	return relevant+'```'


def play(x: str):
	PlaySound(x, SND_FILENAME)


def product(numlist) -> int:
	if len(numlist) == 0:
		return 0
	if len(numlist) == 1:
		return numlist[0]
	return numlist[0] * product(numlist[1:])


def momath(string: str):
	arg = string.lower().split(' ')

	# simple

	if arg[0] in ('circumference', 'perimeter'):
		if arg[1] == 'circle':
			return float(arg[2])*pi
	elif arg[0] == 'ecc':
		a = float(arg[1])
		b = float(arg[2])
		return (1-b**2/a**2)**.5
	elif arg[0] == 'hypot':
		return hypot(float(arg[1]), float(arg[2]))

	# complex

	elif arg[0][:3] == 'ack':
		return mochamath.ack(int(arg[1]), int(arg[2]))
	elif arg[0][-4:] == 'area':
		if arg[1] in ('annulus', 'ring'):
			r1 = float(arg[2])
			r2 = float(arg[3])
			return mochamath.areacircle(r1)-mochamath.areacircle(r2)
		elif arg[1] == 'arbelos':
			r1 = float(arg[2])
			r2 = float(arg[3])
			r3 = float(arg[4])
			return (mochamath.areacircle(r1)-mochamath.areacircle(r2)-mochamath.areacircle(r3))/2
		elif arg[1] == 'circle':
			r = float(arg[2])
			return mochamath.areacircle(r)
		elif arg[1] == 'cone':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.areacone(r, h)
		elif arg[1] == 'cube':
			return 6*float(arg[2])**2
		elif arg[1] == 'cylinder':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.areacone(r, h)
		elif arg[1] == 'hexagon':
			return 3/2*3**.5*float(arg[2])**2
		elif arg[1] == 'octagon':
			return (2+2*2**.5)*float(arg[2])**2
		elif arg[1] == 'pentagon':
			return ((25+10*5**.5)**.5)/4*float(arg[2])**2
		elif arg[1] == 'rectangle':
			return float(arg[2])*float(arg[3])
		elif arg[1] == 'salinon':
			r = float(arg[2])+float(arg[3])
			return mochamath.areacircle(r)/4
		elif arg[1] == 'sector':
			r = float(arg[2])
			theta = float(arg[3])
			return mochamath.areacircle(r)*theta/2/pi
		elif arg[1] == 'sphere':
			r = float(arg[2])
			return mochamath.areasphere(r)
		elif arg[1] == 'square':
			return float(arg[2])**2
		elif arg[1] in ('trapezoid', 'trapezium'):
			return float(arg[4])*(float(arg[2])+float(arg[3]))/2
		elif arg[1] == 'triangle':
			a = float(arg[2])
			b = float(arg[3])
			cc = float(arg[4])
			s = (a+b+cc)/2
			return (s*(s-a)*(s-b)*(s-cc))**.5
		elif arg[1] == 'trigon':
			return 3**.5/4*float(arg[2])**2
	elif arg[0] == 'd':
		dd = int(arg[1])
		poly = list(map(float, arg[2:]))
		return mochamath.dpoly(poly, dd)
	elif arg[0] == 'i':
		i = int(arg[1])
		poly = list(map(float, arg[2:]))
		return mochamath.ipoly(poly, i)
	elif arg[0] == 'frac':
		neg = False
		floating = float(arg[1])
		if floating < 0:
			floating = -floating
			neg = True
		dd = 0
		while floating != int(floating):
			floating = floating*10
			dd += 1
		floating = int(floating)
		dd = 10**dd
		g = gcd(floating, dd)
		floating = int(floating/g)
		dd = int(dd/g)
		return int(('-' if neg else '')+str(floating)), dd
	elif arg[0] == 'gcd':
		return gcd(int(arg[1]), int(arg[2]))
	elif arg[0] == 'lcm':
		a = int(arg[1])
		b = int(arg[2])
		return int(abs(a*b)/gcd(a, b))
	elif arg[0] == 'max':
		return max(map(float, arg[1:]))
	elif arg[0] == 'mean':
		a = list(map(float, arg[1:]))
		return sum(a)/len(a)
	elif arg[0] == 'min':
		return min(map(float, arg[1:]))
	elif arg[0] == 'nroot':
		return float(arg[1])**(1/float(arg[2]))
	elif arg[0] == 'linear':
		m = float(arg[1])
		b = float(arg[2])
		return -b/m
	elif arg[0] == 'product':
		return product(list(map(float, arg[1:])))
	elif arg[0] == 'root':
		a = float(arg[1])
		b = float(arg[2])
		cc = float(arg[3])
		dd = (b**2-4*a*cc)**.5
		return (-b+dd)/2, (-b-dd)/2
	elif arg[0] == 'random':
		if arg[1] == 'card':
			return mochamath.card()
		elif arg[1] == 'mnm' or arg[1] == 'm&m':
			return mochamath.mnm()
	elif arg[0] == 'sqrt':
		return float(arg[1])**.5
	elif arg[0] == 'sum':
		return sum(map(float, arg[1:]))
	elif arg[0][:3] == 'vol':
		if arg[1] == 'cone':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.volumecone(r, h)
		elif arg[1] == 'cube':
			return float(arg[2])**3
		elif arg[1] == 'cylinder':
			r = float(arg[2])
			h = float(arg[3])
			return mochamath.volumecylinder(r, h)
		elif arg[1] == 'frustrum':
			r1 = float(arg[2])
			r2 = float(arg[3])
			h = float(arg[4])
			return pi*h/3*(r1**2+r1*r2+r2**2)
		elif arg[1] == 'sphere':
			r = float(arg[2])
			return mochamath.volumesphere(r)
		elif arg[1] == 'wedge':
			a = float(arg[2])
			b = float(arg[3])
			cc = float(arg[4])
			h = float(arg[5])
			return b*h*(a/3+cc/6)

	return ':/'


def moastro(string: str):
	arg = string.lower().split(' ')

	if arg[0] == 'delay':
		cc = 299792458
		if 1 < len(arg) and arg[1] in object and 'a' in object[arg[1]]:
			a1 = object[arg[1]]['a']
		else:
			a1 = 0
		if 2 < len(arg) and arg[2] in object and 'a' in object[arg[2]]:
			a2 = object[arg[2]]['a']
		else:
			a2 = 0
		bigd = (a1+a2)/cc
		littled = abs(a1-a2)/cc
		seconds = 'Between '+str(int(littled))+' and '+str(ceil(bigd))+' seconds'
		if bigd < 60:
			return seconds
		bigdm = ceil(bigd/60)
		littledm = int(littled/60)
		minutes = ';\nBetween '+str(int(littledm))+' and '+str(ceil(bigdm))+' minutes'
		if bigdm < 60:
			return seconds+minutes
		bigdh = ceil(bigdm/60)
		littledh = int(littledm/60)
		hours = ';\nBetween '+str(littledh)+' and '+str(bigdh)+' hours'
		return seconds+minutes+hours
	elif arg[0] == 'density' or arg[0] == 'rho':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.density(mass, radius)
	elif arg[0] == 'escapevelocity' or arg[0] == 've':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.vescape(mass, radius)
	elif arg[0] == 'g' or arg[0] == 'grav' or arg[0] == 'gravity':
		mass = float(arg[1])
		radius = float(arg[2])
		return mochaastro.surfacegravity(mass, radius)
	elif arg[0] == 'goldilocks' or arg[0] == 'habitablezone':
		m = float(arg[1])
		return mochaastro.habitablezone(m)
	elif arg[0] == 'hohmann':
		i = float(arg[1])
		o = float(arg[2])
		m = float(arg[3])
		return mochaastro.hohmann(i, o, m)
	elif arg[0] == 'horizons':
		try:
			return '```\n'+mochaweb.horizons(arg[1])[:1992]+'\n```'
		except EOFError:
			return 'unable to connect'
	elif arg[0] == 'p' or arg[0] == 'period':
		mass = float(arg[1])
		sma = float(arg[2])
		return mochaastro.p(mass, sma)
	elif arg[0] == 'roche':
		m = float(arg[1])
		dd = float(arg[2])
		return mochaastro.roche(m, dd)
	elif arg[0] == 'soi':
		m = float(arg[1])
		mm = float(arg[2])
		a = float(arg[3])
		return mochaastro.soi(m, mm, a)
	elif arg[0] == 'star':
		m = float(arg[1])
		s = mochaastro.star(m)
		return '```\nMass: '+str(m) + \
				' kg\nRadius: '+str(s[0]) + \
				' m\nLuminosity: '+str(s[1]) + \
				' W\nTemperature: '+str(s[2]) + \
				' K\nLifespan: '+str(s[3])+' s```'
	elif arg[0] == 'stargen':
		try:
			m = float(arg[1])
			return mochastargen.stargen(m)
		except (IndexError, ValueError):
			return mochastargen.stargen('r')
	elif arg[0] == 'synodic':
		a = float(arg[1])
		b = float(arg[2])
		return mochaastro.synodic(a, b)
	try:
		return object[arg[0]][arg[1]]
	except (IndexError, KeyError):
		return ':/'


def lf(x: str) -> str:
	letters = mochalang.sortdict(mochalang.letterfreq(x))
	s = '```\n'
	for i in letters:
		s += i[0]+' '+str(i[1])+'\n'
	return s+'```'


def moling(string: str):
	arg = string.split(' ')

	if arg[0] == 'freq':
		sss = ' '.join(arg[1:]).lower()
		ppp = compile('[^a-z]')
		return lf(sub(ppp, '', sss))
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
		elif arg[1] == 'pl':
			return mochalang.polishipa(arg[2])
	elif arg[0] == 'morse':
		try:
			return mochalang.morse(' '.join(arg[1:]))
		except (IndexError, KeyError):
			return 'https://en.wikipedia.org/wiki/Morse_code'
	elif arg[0] == 'pie':
		if 1 < len(arg):
			return pie(arg[1])
		else:
			return 'https://en.wikipedia.org/wiki/Proto-Indo-European_phonology'
	elif arg[0] == 'scrabble':
		try:
			m = int(arg[2])
		except (IndexError, ValueError):
			m = 1
		return mochalang.scrabble(arg[1])*m
	elif arg[0] == 'shuffle':
		x = arg[1:]
		shuffle(x)
		return ' '.join(x)
	elif arg[0] == 'soundex':
		return mochalang.soundex(arg[1])
	elif arg[0] == 'square':
		if 2 < len(arg) and arg[2] in ('scrabble', 'freq'):
			second = arg[2]
		else:
			second = '0'
		try:
			return mochalang.lettersquare(int(arg[1]), second)
		except ValueError:
			return '>:U'
	elif arg[0] == 'romanize':
		return mochalang.romanize(' '.join(arg[1:]))
	elif arg[0] == 'unmojibake':
		try:
			return mochalang.unmojibake(' '.join(arg[1:]), 'windows-1252', 'utf-8')
		except UnicodeDecodeError:
			return 'Invalid... probably missing some characters?'
		except:
			return 'Invalid... just really, really invalid.'
	elif arg[0] == 'x-sampa' or arg[0] == 'xsampa':
		if 1 < len(arg):
			return xsampa(arg[1])
		else:
			return 'https://en.wikipedia.org/wiki/X-SAMPA'
	return ':/'


def trivia(string: str) -> str:
	arg = string.split(' ')
	try:
		int(arg[0])
		number = True
	except (IndexError, ValueError):
		number = False

	if number:
		return mochaweb.numbersapi(arg[0])
	elif arg[0] == 'number':
		try:
			return mochaweb.numbersapi(arg[1])
		except:
			return 'unable to connect to numbersapi'
	return ':/'


def sto(string: str) -> str:
	arg = string.split(' ')
	try:
		if arg[0] == 'search':
			try:
				return qfsearch(arg[1], 'temp')
			except:
				return 'Bad RegEx'
	except IndexError:
		pass
	if arg[0] == 'sto':
		inputendo = ' '.join(arg[1:])
		if '<@!' in inputendo:
			return 'Not happening.'
		if 'm!' == inputendo[:2]:
			return 'Not happening.'
		if len(inputendo) == 0:
			return 'Not happening.'
		for line in open("temp.txt", "r").read():
			if inputendo == line:
				return 'Quote Already Stored.'
		open("temp.txt", "a").write('\n'+inputendo)
		return 'Success!'
	try:
		return quotefile(arg[0], 'temp')
	except:
		return quotefile('', 'temp')


def bug(string: str) -> str:
	try:
		open("bug.txt", "a").write('\n'+string)
	except:
		return ':/'
	try:
		play('../bug.wav')
	except:
		print('\a')
	return 'Success!\nhttps://youtu.be/bLHL75H_VEM'


def quotefile(line: str, file: str) -> str:
	words = line.split(' ')
	if words[0].lower() == 'search':
		return qfsearch(' '.join(words[1:]), file)
	if line == '':
		q = c(open(file+".txt", "r").read().split('\n'))
		return q
	try:
		q = open(file+".txt", "r").read().split('\n')[int(line)]
	except IndexError:
		return 'That line is not present in the document.'
	return quotefile('', file) if q == '' else q


def qfsearch(pattern: str, file: str) -> str:
	p = compile(pattern)
	q = open(file+".txt", "r").read().split('\n')
	ll = []
	r = ''
	for i in range(len(q)):
		line = q[i]
		if search(p, line) is not None:
			ll.append((i, line))
	for m in ll:
		mmatch = m[1]
		for mmmatch in findall(p, mmatch):
			mmatch = mmatch.replace(mmmatch, '**'+mmmatch+'**')
		r += str(m[0])+' '+mmatch+'\n'
	return 'No Match' if r == '' else r


def zodiac(arg: str) -> str:
	signs = 'aries taurus gemini cancer leo virgo libra scorpio sagittarius capricorn aquarius pisces coffee'.split()
	signelements = ['Fire (Enthusiasm; drive to express self; faith)', 'Earth (Practicality; caution; material world)',
				'Air (Communication; socialization; conceptualization)', 'Water (Emotion; empathy; sensitivity)']
	signqualities = ['Cardinal (active; self-motivated; insightful; ambitious)',
					'Fixed (stabilization; determination; depth; persistence)',
					'Mutable (adaptability; flexibility; sympathy)']
	signrulers = 'Mars Venus Mercury Moon Sun Mercury Venus Mars Jupiter Saturn Saturn Jupiter Starbucks'.split()
	vernal = 6884100 # Venal equinox 1970

	if len(arg):
		n = signs.index(arg.lower())
	else:
		n = int(((time()-vernal) % 31556952)/2629746) # sign number 0-11

	return '**'+signs[n].title()+'**\nElement: '+signelements[n % 4]+'\nQuality: '+signqualities[n % 3]+'\nRuler: ' + \
			signrulers[n]


def mbti(arg) -> str:
	arg = arg[:4].lower()
	ids = (('e', 'i'), ('s', 'n'), ('t', 'f'), ('j', 'p'))
	idz = (('extroverted', 'introverted'), ('sensing', 'intuition'), ('thinking', 'feeling'), ('judging', 'perceiving'))

	string = ''
	for i in range(4):
		try:
			string += idz[i][ids[i].index(arg[i])]+'\n'
		except (IndexError, ValueError):
			pass
	try:
		string += '\nDom: '+functions[arg][0]+'\nAux: '+functions[arg][1]+'\n'
	except (IndexError, KeyError, ValueError):
		pass
	return '**'+arg.upper()+'**\n```\n'+string+'```\nhttps://www.personalityclub.com/wp-content/uploads/2015/05/'+arg + \
			'-profile.png'


def coffee(arg: str) -> str:
	if arg in coffees:
		return '```\n'+coffees[arg]+'```'
	else:
		return ':/'


def convert(uwaa: str) -> str:
	arg = uwaa.split(' ')
	# desc
	if arg[0][:4] in ('desc', 'help'):
		return '```\n'+units[arg[1]][1]+'\n```'

	if arg[1] in religions or arg[2] in religions:
		return 'No, I meant the **other** kind of convert!'
	
	try:
		return str(float(arg[0]) * units[arg[1]][0] / units[arg[2]][0])
	except KeyError:
		return 'invalid unit... did you try using its abbreviation?'


def convertcurrency(uwaa: str):
	arg = uwaa.split(' ')
	try:
		return round(float(arg[0])*mochaweb.currency(arg[1].upper(), arg[2].upper()), 2)
	except KeyError:
		return 'invalid currency... did you try using its abbreviation?'


def religion(uwaa: str) -> str:
	if uwaa in religions:
		return '**'+uwaa.title()+'**```\nPart of: '+religions[uwaa]['partof']+'\nMembers: ' + \
				str(religions[uwaa]['members'])+'```'+religions[uwaa]['url']
	else:
		return ':/'


def xsampa(string: str) -> str:
	for replacement in xskey:
		string = string.replace(replacement[0], replacement[1])
	return string


def pie(string: str) -> str:
	for replacement in piekey:
		string = string.replace(replacement[0], replacement[1])
	return string


def rword(lang: str, minimum: int) -> str:
	replace = '\n.?,!0123456789[]()":;'
	if lang == 'la':
		corpus = open("cdbg.txt", "r").read()
	elif lang == 'fr':
		corpus = open("lg.txt", "r").read()
	elif lang[:7] == 'en-lang':
		corpus = open("en-languages.txt", "r").read()
	else:
		corpus = open("bee.txt", "r").read()
	for char in replace:
		corpus = corpus.replace(char, ' ')
	corpus = corpus.split(' ')
	while 1:
		attempt = c(corpus).lower()
		if len(attempt) >= minimum: # obeys min
			if not compile("[^a-z-']").search(attempt): # must only contain a-z, hyphens, or apostrophes
				return attempt


def d(m: int, n: int) -> int:
	if m*n == 0:
		return 0
	if m < 0:
		return -d(-m, n)
	if n < 0:
		return -d(m, -n)
	s = 0
	for i in range(m):
		s += c(range(n))+1
	return s


def dice(m: int, n: int) -> str:
	maxrolls = 10000
	rolls = []
	for i in range(maxrolls):
		rolls += [d(m, n)]
	mean = sum(rolls)/maxrolls
	try:
		mmmm = str(mode(rolls))
	except StatisticsError:
		mmmm = 'No Unique Mode'
	ssss = stdev(rolls)
	return '```\nMin: '+str(m)+'\nMax: '+str(m*n)+'\nMean: '+str(mean)+'\nMedian: '+str(median(rolls))+'\nMode: '+mmmm + \
			'\nσ: '+str(ssss)+'\n\tm-2σ: '+str(mean-2*ssss)+'\n\tm+2σ: '+str(mean+2*ssss)+'\n\nSample: '+str(d(m, n))+'```'


def dicemat(x: str) -> str:
	x = x.lower().replace('d', ' ')
	x = x.split(' ')
	try:
		m = int(x[0])
		n = int(x[1])
		if abs(m) < 99 > abs(n):
			return dice(m, n)
		return 'Too High'
	except (IndexError, ValueError):
		return 'Space-separated!'


def gp(x: str) -> str:
	args = x.split(' ')
	try:
		gold = float(args[0])
		ways = float(args[1])
	except (IndexError, ValueError):
		return 'if you need help: `m! help gp`'
	if ways == 0:
		return 'Zero ways, eh?'
	quotient = str(round(gold/ways, 2)).split('.')
	g = quotient[0]
	try:
		s = quotient[1][0]
	except IndexError:
		s = '0'
	try:
		copper = quotient[1][1]
	except IndexError:
		copper = '0'
	return g+'g '+s+'s '+copper+'c'


def asmr(s: str) -> str:
	if len(s):
		seed(s)
	# .		S1					S2					S3
	# (ADJ/NOUN/VERBing) [NOUN(s)/VERBing] <ASMR (front/back;optional)>
	name = []
	asmrstyle = randint(0, 2) # 0bXY X-beginning Y-end
	# S1 style
	s1style = c(['adj', 'ing', 'n', False])
	if s1style:
		name += [c(asmrwords[s1style])]
	# S2 style
	s2style = c(['ing', 'n', 'pl'])
	name += [c(asmrwords[s2style])]
	# ooo
	name = ' '.join(name).title()
	# S3 style
	if bin(asmrstyle)[-2] == '1':
		name = 'ASMR '+name
	elif bin(asmrstyle)[-1] == '1':
		name += ' ASMR'
	return name


# GAMES
async def g23(mc: discord.TextChannel) -> bool:
	timer = 30
	await mc.send('Start guessing! You have **'+str(timer)+'** seconds! Clock starts *now*!~')
	start = time()
	guesses = []
	while time() < start+timer: # 30s should be enough
		def check(m: discord.Message) -> bool:
			return m.channel == mc
		msg = await bot.wait_for('message', timeout=1, check=check) # type: discord.Message
		try:
			ma = msg.author.name # type: str
			guesses.append((float(msg.content), ma))
			await msg.delete()
		except:
			pass
	a1 = list(map(lambda x: x[0], guesses))
	try:
		avg23 = sum(a1)*2/3/len(a1)
		a2 = list(map(lambda x: abs(x-avg23), a1))
		winner = a2.index(min(a2))
		await mc.send(guesses[winner][1]+', you won with your guess of '+str(guesses[winner][0]) +
						' (2/3 of the mean was actually '+str(avg23)+')! ^o^')
		return False
	except ZeroDivisionError:
		await mc.send('N-nobody??? ;-;')
		return True


async def gtn(args, msg: discord.Message) -> bool:
	mc = msg.channel
	try:
		minn = int(args[1])
		maxn = int(args[2])
	except (IndexError, ValueError):
		minn = 0
		maxn = 99
	answer = randint(minn, maxn)
	while msg.content.lower() not in quit:
		if msg:
			try:
				if int(msg.content) < answer:
					await mc.send('>')
				else:
					await mc.send('<')
			except ValueError:
				pass
		else:
			await mc.send('Guess a number between '+str(minn)+' and '+str(maxn)+'!')

		def check(m: discord.Message) -> bool:
			return m.channel == mc
		msg = await bot.wait_for('message', check=check)
		if msg.content == str(answer):
			await mc.send(msg.author.name+', you win! ^o^')
			return False
	await mc.send('o oki ;-;')
	return True


async def word(args, message: discord.Message) -> bool:
	mc = message.channel
	try:
		w = args[1].lower()
		await message.delete()
		if w == 'latin':
			w = rword('la', 1)
	except:
		w = rword('en', 4)
	await mc.send('A new game of **Word** has begun:\n**'+'X'*len(w)+'**')
	while 1:
		def check(m: discord.Message) -> bool:
			return m.channel == mc
		msg = await bot.wait_for('message', check=check)
		if msg.content.lower() in quit:
			await mc.send('c r i e ;-;\nthe word was **'+w+'**.')
			return True
		pips = ''
		if msg.author.name != 'Mobot':
			try:
				guess = msg.content.lower()
				if len(guess) == len(w): # NO CHEATING
					if guess == w:
						await mc.send(msg.author.name+', you won with your guess of '+guess+'! ^o^')
						mochagive(5, msg.author.name.lower())
						return False
					mr = range(min(len(w), len(guess)))
					# look for EXACT matches
					for i in mr:
						if guess[i] == w[i]:
							pips += 'x'
					for i in mr:
						if guess[i] in w and guess[i] != w[i]:
							pips += '*'
					await mc.send(msg.author.name+', your guess of '+guess+' resulted in:\n'+pips)
			except:
				pass


async def hangman(args, msg: discord.Message) -> bool:
	mc = msg.channel
	if 1 < len(args):
		lang = args[1]
	else:
		lang = 'en'
	w = rword(lang, 4)
	# print('\t\t'+lang,word)
	known = 'X'*len(w)
	await mc.send('A new game of **Hangman** has begun:\n**'+known+'**')
	fails = 0
	faill = ''
	won = False
	while fails < 10:
		def check(m: discord.Message) -> bool:
			return m.channel == mc
		msg = await bot.wait_for('message', check=check)
		if msg.content.lower() in quit:
			await mc.send('c r i e ;-;\nthe word was **'+w+'**.')
			return True
		if msg.author.name != 'Mobot':
			try:
				guess = msg.content.lower()
				if len(guess) == 1:
					if guess in w:
						# replace letters in known
						for i in range(len(w)):
							if guess == w[i]:
								known = list(known)
								known[i] = guess
								known = ''.join(known)
						# won?
						if 'X' not in known:
							won = True
							break
					else:
						fails += 1
						faill += guess+' '
						await mc.send('**'+guess+'** is not in the word.')
				elif guess == w:
					won = True
					break
				# display word
				await mc.send('**'+known+'**\n'+faill)
			except:
				pass
	if won:
		await mc.send('**'+msg.author.name+'**, you won! The word was **'+w+'**! ^o^')
		if 'en-lang' in lang: # To Appease Yata
			await mc.send('https://en.wikipedia.org/wiki/'+w.title()+'_language')
		mochagive(1, msg.author.name.lower())
	else:
		await mc.send('You lost. The word was **'+w+'**. uwu')
	return False


def vrleaderboard(lang: str, verb: str, n: int) -> str:
	# [(lang,verb,##,user),...]
	wholelist = list(map(lambda x: (x[0], x[1], int(x[2]), x[3]), map(lambda x: x.split('\t'),
											open("vrleaderboard.txt", "r").read().split('\n'))))
	# the above is CONFIRMED to work correctly. the problem is below this point
	# find relevant entries
	o = []
	for entry in wholelist:
		if entry[0] == lang and entry[1] == verb:
			o.append((entry[2], entry[3]))
	# sort by time
	o = sorted(o, key=lambda x: x[0])
	# now turn to text
	oo = ''
	for i in range(min(len(o), n+1)):
		entry = o[i]
		oo += str(entry[0])+'\t'+entry[1]+'\n'
	return '```\ns \tusername\n'+oo+'```'


async def associate(message: discord.Message) -> bool:
	idk = {'dunno', 'idk', 'pass', 'skip', 'unno'}
	ma = message.author
	mc = message.channel
	await mc.send('A new game of **Associate** has begun!')
	used = []
	while 1:
		# regenerate list
		associatefile = open('associate.txt', 'r').read()
		wordlist = list(map(lambda x: x[0:2]+[int(x[2])], map(lambda x: x.split('\t'), associatefile.split('\n'))))
		# choose word
		i = 0
		while 1:
			word = c(wordlist)[c([0, 1])]
			if word not in used:
				break
			if i > 999:
				used = []
				break
			i += 1
		# generate word stats
		wordstats1 = []
		wordstats2 = []
		for match in wordlist:
			if match[0] == word:
				wordstats1.append(match[1])
				wordstats2.append(match[2])
		s = sum(wordstats2)
		wordstats2 = list(map(lambda x: x/s, wordstats2))
		# text
		await mc.send('Your word is **'+word+'**! Type a word associated with it!')
		while 1:
			def check(m: discord.Message) -> bool:
				return m.channel == mc and m.author == ma
			msg = await bot.wait_for('message', check=check)
			mcl = msg.content.lower()
			if mcl in idk or mcl in quit or mcl == 'stats':
				break
			if not search('[^a-z]', mcl):
				if mcl in word or word in mcl:
					await mc.send('Your word must not contain the word, and the word must not contain yours.')
				else:
					break
			else:
				await mc.send('Your word must contain only the letters a-z.')
		# quit
		if mcl in quit:
			break
		# stats
		if mcl == 'stats':
			try:
				o = '```'
				for i in range(len(wordstats1)):
					o += '\n'+wordstats1[i]+'\t'+str(round(wordstats2[2], 4))
				o += '```'
				await mc.send(o)
			except:
				await mc.send('No stats for this word!')
		elif mcl in idk:
			pass
		# was message in list?
		elif mcl in wordstats1:
			i = wordstats1.index(mcl)
			await mc.send(str(round(wordstats2[i]*100, 2))+'% agree!')
			# add
			target = word+'\t'+mcl
			for line in associatefile.split('\n'):
				if line[:len(target)] == target:
					n = int(line[len(target)+1:])
					oldline = target+'\t'+str(n)
					newline = target+'\t'+str(n+1)
					associatefile = associatefile.replace(oldline, newline)
					open("associate.txt", "w").write(associatefile)
					break
		else:
			# I feel clever for the following couple lines... :^)
			x = 'No' if len(wordstats1) else 'Every'
			await mc.send(x+'body agrees!')
			# add
			open("associate.txt", "a").write('\n'+word+'\t'+mcl+'\t1')
		used.append(word)
	await mc.send('Bye-bye!~ ^_^')
	return False


async def tests(message: discord.Message) -> bool:
	length = 20
	ma = message.author
	mc = message.channel
	name = message.content[8:].lower()
	score = 0

	def check(m: discord.Message) -> bool:
		return m.channel == mc and m.author == ma
	if name[:3] == 'add':
		for i in range(length):
			n = mochatest.rpair()
			await mc.send(str(n[0])+' + '+str(n[1]))
			msg = await bot.wait_for('message', check=check)
			try:
				if int(msg.content) == sum(n):
					score += 1
			except:
				pass
	elif name[:3] == 'mul':
		for i in range(length):
			n = mochatest.rpair()
			await mc.send(str(n[0])+' * '+str(n[1]))
			msg = await bot.wait_for('message', check=check)
			try:
				if int(msg.content) == n[0]*n[1]:
					score += 1
			except:
				pass
	elif name == 'literacy':
		length = 10
		for i in range(length):
			n = mochatest.rgrammar()
			await mc.send(n[0])
			msg = await bot.wait_for('message', check=check)
			try:
				mcl = msg.content.lower()
				if mcl == n[1]:
					score += 1
			except:
				pass
	else:
		return True
	antiscore = length-score
	w = mochatest.wilson(score, antiscore)
	await mc.send('**'+ma.name.title()+'** correctly performs at least **'+str(round(w*100)) +
					'%** of the time, with 95% confidence.\n'+str(score)+'/'+str(length))
	return True


async def verbrace(args, mc: discord.TextChannel) -> bool:
	def check(m: discord.Message) -> bool:
		return m.channel == mc
	forms = pronouns[args[1]]
	word = c(verbs[args[1]])
	limit = 30
	await mc.send('A new game of **Verb Race** has begun! You have **'+str(limit)+'** seconds to type `join`!')
	form = 0
	start = time()
	players = []
	finalform = len(forms)
	while time() < start+limit:
		msg = await bot.wait_for('message', check=check, timeout=1)
		try:
			if msg.content.lower() == 'join' and msg.author.name != 'Mobot':
				players.append(msg.author)
				await msg.delete()
				await mc.send('**'+msg.author.name+'** has joined!')
		except:
			pass
	if len(players) < finalform: # for small games
		players = players*ceil(finalform/len(players))
	shuffle(players)
	pbu = players[:] # player backup
	choice = False
	start = time()
	await mc.send('A new game of **Verb Race** has begun!\nYour verb is: **'+word[finalform]+'**!')
	allcorrect = True
	while form < finalform:
		if choice:
			msg = await bot.wait_for('message', check=check)
			if msg.content.lower() in quit and msg.author in players:
				await mc.send('c r i e ;-;')
				break # return True
			elif msg.author == choice:
				await msg.delete()
				if msg.content == word[form]:
					await mc.send('Correct!')
				else:
					await mc.send('Incorrect! The correct form was **'+word[form]+'**')
					allcorrect = False
				form += 1
				choice = False
		else:
			choice = players.pop()
			await mc.send('**'+choice.name+'**, conjugate **'+word[finalform]+'** for **'+forms[form]+'**!')
	await mc.send('The game of **Verb Race** has ended! You took '+str(int(time()-start))+' seconds!')
	# check to see if eligible for leaderboard
	if allcorrect and len(set(pbu[:finalform])) == 1:
		mochagive(1, pbu[0].name.lower())
		open("vrleaderboard.txt", "a").write('\n'+'\t'.join([args[1], word[finalform], str(int(time()-start)), pbu[0].name]))
	# print leaders
	await mc.send('Leaderboard for **'+word[finalform]+'**:\n'+vrleaderboard(args[1], word[finalform], 5))
	return False


async def numbers(mc: discord.TextChannel) -> bool:
	def check(m: discord.Message) -> bool:
		return m.channel == mc
	limit = 45
	ops = '+-*/'
	minn = 2
	maxn = 20
	nn = 6
	ns = []
	for i in range(nn):
		ns.append(randint(minn, maxn))
	target = 0.5
	whatsthis = ' '.join(map(str, ns))
	owo = whatsthis
	while target != int(target) or not (10 <= target <= 1000):
		owo = whatsthis
		for i in range(len(ns)-1):
			owo += c(ops)
		target = mocharpn.rpn(owo)[0]
	# now a valid target is established
	target = int(target)
	# shuffle again to prevent exploit
	shuffle(ns)
	# Begin!
	await mc.send('A new game of **Numbers** has begun!\nYour target is **'+str(target) +
					'**, and your numbers are **'+' '.join(map(str, ns))+'**!')
	await mc.send('You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time() < start+limit:
		msg = await bot.wait_for('message', check=check, timeout=1)
		try:
			if msg.content.lower() in quit:
				await mc.send('c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name != 'Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await msg.delete()
					await mc.send('**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await mc.send('u already gone shoo shoo')
		except AttributeError:
			pass
		if time()+5 > start+limit and not warned:
			await mc.send('You have **5** seconds left to solve!')
			warned = True
	await mc.send('The game of **Numbers** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await mc.send(guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await mc.send('The Math Corner notes that **'+str(target)+'** was achievable using the following solution:\n`'+owo+'`')
	return False


async def twentyfour(mc: discord.TextChannel) -> bool:
	def check(m: discord.Message) -> bool:
		return m.channel == mc
	limit = 30
	ops = '+-*/'
	# generate numbers until it works dammit
	target = 0
	owo, whatsthis = '', ''
	while target != 24:
		start = time()
		ns = []
		for i in range(4):
			ns.append(randint(1, 10))
		whatsthis = ' '.join(map(str, ns))
		while target != 24:
			owo = whatsthis
			for i in range(len(ns)-1):
				owo += c(ops)
			target = mocharpn.rpn(owo)[0]
			if time()-start > 1:
				break
	# now a valid sample is established
	# Begin!
	await mc.send('A new game of **24** has begun!\nYour numbers are **'+whatsthis+'**!')
	await mc.send('You have **'+str(limit)+'** seconds to solve!')
	start = time()
	guesses1 = []
	guesses2 = []
	warned = False
	while time() < start+limit:
		msg = await bot.wait_for('message', check=check, timeout=1)
		try:
			if msg.content.lower() in quit:
				await mc.send('c r i e ;-;')
				return True
			elif msg.author.name not in guesses2:
				if msg.author.name != 'Mobot':
					guesses1.append(msg.content)
					guesses2.append(msg.author.name)
					await msg.delete()
					await mc.send('**'+msg.author.name+'**, your answer has been submitted!')
			else:
				await mc.send('u already gone shoo shoo')
		except AttributeError:
			pass
		if time()+5 > start+limit and not warned:
			await mc.send('You have **5** seconds left to solve!')
			warned = True
	await mc.send('The game of **24** has ended! Check your answers!')
	for i in range(len(guesses1)):
		result = mocharpn.rpn(guesses1[i])[0]
		await mc.send(guesses2[i]+' `'+guesses1[i]+'` = `'+str(result)+'` (`'+str(abs(result-target))+'` off)')
	await mc.send('The Math Corner notes that **24** was achievable using the following solution:\n`'+owo+'`')
	return False


async def llama(message: discord.Message) -> bool:
	ma, mc = message.author, message.channel

	def check(m: discord.Message) -> bool:
		return m.channel == mc and m.author == ma
	room = -1
	state = 0
	inv = False
	await mc.send('A new emulation of **Llama Adventure** has been initiated! Type anything to begin, and have fun!~ ^_^')
	while 1:
		msg = await bot.wait_for('message', check=check)
		if room == -1 == state:
			return True # exit
		ml = mochallama.llama(room, state, inv, msg)
		await mc.send(ml[3])
		room = ml[0]
		state = ml[1]


async def hello_game(message: discord.Message) -> bool:
	ma = message.author
	mc = message.channel

	def check(m: discord.Message) -> bool:
		return m.channel == mc and m.author == ma
	await mc.send('A new HELLO has begun!')
	hello.questions = eval(open('../hello_q.txt', 'r').read()) # I'm so sorry
	hello.users = eval(open('../hello_u.txt', 'r').read()) # I'm so sorry
	if ma.id not in hello.users:
		hello.users[ma.id] = [[1000, 1], []]
	while 1:
		# await mc.send(str(ma.name) + str(ma.id))
		p_elo = hello.elo(hello.users[ma.id][0])
		qid = 0
		for i in range(10):
			qid = randint(0, len(hello.questions)-1)
			if qid not in hello.users[ma.id][1]:
				break
			elif i == 9:
				await mc.send('You appear to have answered all available questions.\nFinal Elo: '+str(p_elo))
				return False
		q_elo = round(hello.elo(hello.questions[qid][0]))
		await mc.send(hello.ask_question(qid)+'\nQuestion Elo: '+str(q_elo)+'\n Your Elo: '+str(p_elo))
		msg = await bot.wait_for('message', check=check)
		if msg.content.lower() in quit:
			await mc.send('c r i e ;-;')
			return True
		else:
			result = hello.check_answer(qid, msg.content)
			hello.addgame(qid, p_elo, result)
			if result:
				await mc.send(':)')
				mochagive(1, ma.id)
			else:
				await mc.send(':(')
			hello.users[ma.id][0][0] += q_elo + 400 * (1 if result else -1)
			hello.users[ma.id][0][1] += 1
			hello.users[ma.id][1].append(qid)
			# update p + q files
			open('../hello_q.txt', 'w').write(str(hello.questions))
			open('../hello_u.txt', 'w').write(str(hello.users))


async def jeopardy(message: discord.Message):
	mc = message.channel

	def check(m: discord.Message) -> bool:
		return m.channel == mc
	question, answer = mochaweb.jeopardy()
	await mc.send(embed=question)
	while 1:
		attempt = await bot.wait_for('message', check=check)
		if attempt.content.lower() == answer.lower():
			await mc.send('**'+answer+'** is correct!\n+1 moki to **'+attempt.author.name+'**')
			mochagive(1, attempt.author.id)
			break
		elif attempt.content.lower() in quit:
			await mc.send(':(\nThe answer was **'+answer+'**.')
			break


def moore(array: list, coords: (int, int)) -> list:
	x, y = coords
	neighbors = []
	if 0 < y:
		if 0 < x:
			# UL
			neighbors.append(array[y-1][x-1])
		if x+1 < len(array):
			# UR
			neighbors.append(array[y-1][x+1])
		# U
		neighbors.append(array[y-1][x])
	if y+1 < len(array):
		if 0 < x:
			# DL
			neighbors.append(array[y+1][x-1])
		if x+1 < len(array):
			# DR
			neighbors.append(array[y+1][x+1])
		# D
		neighbors.append(array[y+1][x])
	if 0 < x:
		# L
		neighbors.append(array[y][x-1])
	if x+1 < len(array[0]):
		# R
		neighbors.append(array[y][x+1])
	return neighbors


def minesweeper(length: int = 10, bombs: int = 20) -> str:
	title = 'Minesweeper ({0}x{0}, {1} mines)'.format(length, bombs)
	number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
	mine = 'boom'
	tiles = [False] * (length**2 - bombs) + [True] * bombs
	shuffle(tiles)
	grid = [[tiles.pop() for _ in range(length)] for _ in range(length)]
	text_grid = ''
	for y, row in enumerate(grid):
		text_grid += '\n'
		for x, tile in enumerate(row):
			neighbor_count = moore(grid, (x, y)).count(True)
			text_grid += '||:'
			text_grid += mine if tile else number_names[neighbor_count]
			text_grid += ':||'
	return title + '\n' + text_grid


filters = {}


def reloadfilter():
	global filters
	filters = {}
	for line in open('filter.txt', 'r').read().split('\n'):
		lineargs = line.split('\t')
		filters[lineargs[0]] = lineargs[1:]


async def mfilter(message: discord.Message) -> bool:
	ma, mc = message.author, message.channel

	def check(m: discord.Message) -> bool:
		return m.channel == mc and m.author == ma
	if not message.author.server_permissions.administrator:
		await mc.send('Not happening.')
		return True

	mc = message.channel
	# filter messages containing OR filter messages NOT containing?
	await mc.send('Filter messages WITH regex or WITHOUT regex?')
	msg = False
	while msg not in ('with', 'without'):
		msg = await bot.wait_for('message', check=check)
		msg = msg.content.lower()
	await mc.send('Enter regex filter:')
	refilter = await bot.wait_for('message', check=check)
	refilter = refilter.content
	await mc.send('Successfully set up **'+msg+'** filter **/'+refilter+'/** for **'+message.channel.name+'**.')
	
	open('filter.txt', 'a').write('\n'+message.channel.id+'\t'+msg+'\t'+refilter)
	# reload filters
	reloadfilter()
	return False


mochaid = open('../mocha.txt', 'r').read()
mobotid = open('../mobot.txt', 'r').read()


def bankwrite(bank: dict):
	s = ''
	for account in bank:
		s += '\n'+account+'\t'+str(bank[account])
	open("bank.txt", "w").write(s[1:])


def mochagive(amt: int, acct: str):
	# acct = user.id
	file = open("bank.txt", "r").read().split('\n')
	bank = {}
	for line in file:
		words = line.split('\t')
		try:
			bank[words[0]] = int(words[1])
		except ValueError: # inf from mocha
			pass
	try:
		bank[acct] += amt
	except KeyError:
		bank[acct] = amt
	bankwrite(bank)


def mochapoint(message: discord.Message) -> str:
	donating = ['del', 'don']
	giving = ['giv']
	id = message.author.id
	string = ' '.join(message.content.lower().split(' ')[2:])
	# ["user\t$",...]
	file = open("bank.txt", "r").read().split('\n')
	bank = {}
	for line in file:
		ll = line.split('\t')
		try:
			bank[ll[0]] = int(ll[1])
		except ValueError:
			pass
	bank[mochaid] = float('inf')
	# string edit
	subcommand = string.split(' ')
	if subcommand[0][:3] == 'bal':
		if id == mochaid:
			return 'https://youtu.be/7sWpSvQ_hwo'
		try:
			return message.author.name+': **'+str(bank[id])+'**'
		except KeyError: # not in there
			open("bank.txt", "a").write('\n'+id+'\t0')
			return message.author.name+': **0**'
	elif subcommand[0][:3] == 'eco':
		people = len(bank)
		wealth = []
		for acct in bank:
			if acct != mochaid:
				wealth.append(bank[acct])
		summation = sum(wealth)
		# x% of people hold 95% of the wealth
		wealth = sorted(wealth)
		while sum(wealth) > summation*.05:
			wealth.pop()
		rich = str(round((1 - len(wealth) / people)*100, 2))
		# continue
		if id == mochaid:
			percent = 'errythin'
		else:
			try:
				percent = str(round(int(bank[id])/summation*100, 2))
			except KeyError:
				percent = '0'
		return '**'+str(summation)+'** mokis in circulation\nYou own **'+percent+'%**.\n**'+rich + \
				'%** of people own **95%** of the wealth!'
	elif subcommand[0][:3] in donating+giving:
		if subcommand[0][:3] in donating:
			subcommand.append(subcommand[1])
			subcommand[1] = c(list(message.guild.members)).id
			tgt = subcommand[1]
		else:
			tgt = subcommand[1][3:-1]
		try:
			int(tgt)
		except:
			return 'Invalid user'
		if id == tgt:
			return '...no.'
		try:
			# easter egg
			if 'respect' in subcommand[2]:
				return '**respecc**\nhttps://www.youtube.com/watch?v=6FOUqQt3Kg0'
			# main
			amt = int(subcommand[2])
			if amt < 1:
				raise ValueError('SKREE')
			try:
				if bank[id] < amt:
					raise ValueError('SKREE')
				bank[id] -= amt
				if tgt in bank:
					bank[tgt] += amt
				else:
					bank[tgt] = amt
				bankwrite(bank)
				user = 'user' if subcommand[0][:3] in giving else '<@!'+tgt+'>'
				return 'Successfully transfered **'+str(amt)+'** moki'+('s' if amt > 1 else '')+' to '+user+'!'
			except:
				return 'Insufficient Funds'
		except:
			return 'Invalid Amount; require a natural number.'
	else: # if subcommand[0] == 'help':
		mokicommands = (
			'game hangman',
			'game hello',
			'game verbrace',
			'game word',
			'jeopardy'
		)
		commandslist = '`, `m! '.join(mokicommands)
		return '*Mokis* are used to purchase **bragging rights**... or someshit.\nRewards are given by `m! '+commandslist+'`.'


def new_status():
	lines = open('status.txt', 'r').read().split('\n')
	lines = list(filter(lambda x: x[0] != '/', lines))
	return c(lines)


# ACTUAL BOT SHIT
bot_prefix = "m!"
token = open("../token.txt", "r").read()

bot = Bot(command_prefix=bot_prefix)


@bot.event
async def on_ready():
	print(bot.user.name+' loaded.')
	reloadfilter()


@bot.event
async def on_message(message: discord.Message):
	await bot.process_commands(message)
	global anchor
	global lastmessage
	global timecheck
	m = message.content
	mc = message.channel
	n = m.lower()
	ma = m.split(' ')
	na = n.split(' ')
	# quotefile
	try:
		qfcondition = na[0] == 'm!' and na[1] in quotefiles+wholequotefiles
	except:
		qfcondition = False
	# GOAT
	try:
		gchelp = 'which' if 'which' in n else ('what' if 'what' in n else ('who' if 'who' in n else 0)), \
				'best' if 'best' in n else ('greatest' if 'greatest' in n else 0)
		# goatcondition = gchelp[0] and 'bot' in n and 'is' in n and gchelp[1]
		if 'mobot' in n:
			goatcondition = n.index(gchelp[0]) < n.index('is') < n.index(gchelp[1])
		else:
			goatcondition = n.index(gchelp[0]) < n.index('bot') < n.index('is') < n.index(gchelp[1])
			goatcondition = goatcondition or (n.index(gchelp[0]) < n.index('is') < n.index(gchelp[1]) < n.index('bot'))
	except:
		goatcondition = False

	try:
		notmobot = message.author.name!='Mobot'
		if notmobot:
			if goatcondition: # needed due to complicated conditions
				try:
					await mc.send('MOBOT IS GOAT\nhttps://www.youtube.com/watch?v=wsj0XFdmxZ0')
				except:
					pass
			else: # special triggers
				done = False
				for i in rspecial:
					if i in n:
						try:
							await mc.send(c(rspecial[i]))
						except:
							pass
						done = True
						break
				if not done:
					for i in specialer:
						ret = compile('^'+i+'$|^'+i+'\\W|\\W'+i+'$|\\W'+i+'\\W')
						if search(ret, n):
							try:
								await mc.send(specialer[i])
							except:
								pass
							break
		# real commands
		if na[0] == bot_prefix and 1 < len(na):
			# logging
			loglook = str(message.created_at)[:19]+' - @'+str(message.author)+' (#'+str(mc)+' in '+str(message.guild)+')\n\t'+m
			loglook = sub(compile(r'[^!-~\s]'), '?', loglook)
			print(loglook)
			open("log.txt", "a").write(loglook+'\n')
			# find command
			try:
				if na[1] in open('../disable.txt', 'r').read().split('\n'):
					await mc.send("Command temporarily disabled for repairs")
					return True
			except FileNotFoundError:
				pass
			if na[1] == 'help':
				await mc.send(help_function(m[8:]))
			elif na[1] == 'bf':
				args = m[6:].split('\n')
				await mc.send(str(mochabf.run(args[0], args[1:])))
			elif na[1] == 'gi':
				await mc.send(embed=mochaweb.gi(m[6:]))
			elif na[1] == 'gs':
				await mc.send(str(mochagolfscript.run(m[6:])))
			elif na[1] == 'gp':
				await mc.send(gp(m[6:]))
			elif na[1] == 'dfprop':
				entry = m[10:].replace(' ', '%20')
				try:
					await mc.send(mochaweb.dfprop(entry))
				except:
					await mc.send('Can\'t seem to fetch properties for '+m[10:])
			elif na[1] == 'df':
				entry = m[6:].replace(' ', '%20')
				try:
					await mc.send(mochamw.main2('dwarffortresswiki.org', 'DF2014:'+entry))
				except:
					await mc.send('Can\'t seem to fetch article for '+m[6:])
			elif na[1] == 'mc':
				entry = m[6:].replace(' ', '%20')
				try:
					await mc.send(mochamw.main('minecraft.gamepedia.com', entry))
				except:
					await mc.send('Can\'t seem to fetch article for '+m[6:])
			elif na[1] == 'sc2':
				entry = m[7:].replace(' ', '%20')
				try:
					await mc.send(mochamw.main('liquipedia.net/starcraft2', entry))
				except:
					await mc.send('Can\'t seem to fetch article for '+m[7:])
			elif na[1] == 'ud':
				try:
					await mc.send(mochaweb.ud(m[6:]))
				except:
					await mc.send('Can\'t seem to fetch entry for '+m[6:])
			elif na[1] == 'wc':
				entry = m[6:].replace(' ', '%20')
				try:
					await mc.send(mochaweb.wtcleanup(mochamw.main('en.wikibooks.org/w', 'Cookbook:'+entry)))
				except:
					await mc.send('Can\'t seem to fetch recipe for '+m[6:])
			elif na[1] == 'wt':
				entry = m[6:].replace(' ', '%20')
				try:
					await mc.send(mochaweb.wtcleanup(mochamw.main('en.wiktionary.org/w', entry)))
				except:
					await mc.send('Can\'t seem to fetch entry for '+m[6:])
			elif na[1] == 'ast':
				await mc.send(str(moastro(m[7:])))
			elif na[1] == 'bug':
				await mc.send(str(bug(m[7:])))
			elif na[1] == 'mat':
				await mc.send(str(momath(m[7:])))
			elif na[1] == 'rpn':
				await mc.send(str(mocharpn.rpn(m[7:])))
			elif na[1] == 'ttt':
				await mc.send(str(mochattt.ai(m[7:])))
			elif na[1] == 'dice':
				await mc.send(str(dicemat(m[8:])))
			elif na[1] == 'ling':
				await mc.send(str(moling(m[8:])))
			elif na[1] == 'mbti':
				await mc.send(str(mbti(m[8:])))
			elif na[1] == 'test':
				await tests(message)
			elif na[1] == 'time':
				if na[2] == 'taken':
					await mc.send('m! time diff')
					lastmessage = message
				elif n == 'm! time diff' and message.author.id == mobotid:
					await message.edit(content='Calculating...')
					sleep(1)
					old = lastmessage.created_at.replace(tzinfo=timezone.utc).created_at()
					new = message.created_at.replace(tzinfo=timezone.utc).created_at()
					await message.edit(content=str(int((new-old)*1000))+' ms')
				else:
					await mc.send(str(message.created_at)[:19]+' UTC')
			elif na[1] == 'xkcd':
				try:
					await mc.send(mochaweb.xkcd(m[8:]))
				except:
					await mc.send('Can\'t seem to fetch comic #'+m[8:])
			elif na[1] == 'wiki':
				entry = m[8:].replace(' ', '%20')
				try:
					await mc.send(mochaweb.wikicleanup(mochamw.main('en.wikipedia.org/w', entry)))
				except:
					await mc.send('Can\'t seem to fetch article for '+m[8:])
			elif na[1] == 'jisho':
				await mc.send(embed=mochaweb.jisho(m[9:]))
			elif na[1] == 'metar':
				try:
					await mc.send(mochaweb.metar(m[9:]))
				except:
					await mc.send('Can\'t seem to fetch metar data for '+m[9:] +
								'\nhttps://aviationweather.gov/dataserver/example?datatype=metar')
			elif na[1] == 'quote':
				try:
					await mc.send(str(sto(m[9:])))
				except:
					await mc.send('Message too Long')
			elif na[1] == 'phoon':
				try:
					await mc.send(mochaweather.phoon())
				except:
					await mc.send('Can\'t seem to fetch current lunar phase')
			elif na[1] == 'quake':
				try:
					await mc.send(mochaweather.quake())
				except:
					await mc.send('Can\'t seem to fetch earthquake information')
			elif na[1] == 'solve':
				await mc.send(mocharpn.infix(m[9:]))
			elif na[1] == 'tarot':
				await mc.send(embed=mochaweb.tarot())
			elif na[1] == 'filter':
				await mfilter(message)
			elif na[1] == 'zodiac':
				await mc.send(zodiac(n[10:]))
			elif na[1] == 'coffee':
				await mc.send(str(coffee(m[10:])))
			elif na[1] == 'trivia':
				await mc.send(str(trivia(m[10:])))
			elif na[1][:6] == 'secret':
				await mc.send('**'+str(len(quotefiles)+len(special)+len(specialer)+len(rspecial)) +
							'** secret commands, of which:\n\n**'+str(len(specialer)+len(rspecial)) +
							'** are triggered by a string,\n**'+str(len(special))+'** are triggered by `m!`, and\n**' +
							str(len(quotefiles))+'** are triggered by `m!` and an optional argument.')
			elif na[1] == 'convert':
				await mc.send(str(convert(n[11:])))
			elif na[1] == 'currency':
				await mc.send(str(convertcurrency(n[12:])))
			elif na[1] == 'weather':
				try:
					await mc.send(mochaweather.main(m[11:]))
				except:
					await mc.send('Can\'t seem to fetch weather for '+m[11:])
			elif na[1] == 'welcome':
				try:
					code = na[2]
					try:
						bonus = ' '.join(na[3:])
						if bonus == '':
							raise ValueError('no blenk plox')
						await mc.send(welcome[code].title()+', '+bonus+'!')
					except:
						await mc.send(welcome[code].title()+'!')
				except:
					await mc.send('Welcome!')
			elif na[1] == 'hurricane':
				try:
					await mc.send(mochaweather.hurricane(m[13:]))
				except:
					await mc.send('Can\'t seem to fetch hurricane advisories')
			elif na[1] == 'asmrname':
				await mc.send(asmr(m[12:]))
			elif na[1] == 'califire':
				try:
					await mc.send(mochaweb.califire())
				except:
					await mc.send('Can\'t seem to fetch california fire data')
			elif na[1] == 'jeopardy':
				await jeopardy(message)
			elif na[1] == 'religion':
				await mc.send(str(religion(m[12:])))
			elif na[1] == 'worldgen':
				moclimate.wg(m[12:])
				await mc.send(file='img/temp.png')
			elif na[1] == 'minesweeper':
				await mc.send(minesweeper(*list(map(int, na[2:]))))
			elif na[1][:4] == 'moki':
				await mc.send(mochapoint(message))
			# SECRET DEBUG
			elif na[1] == 'anchor' and message.author.id == mochaid:
				anchor = mc
				await message.delete()
			elif na[1] == 'torpedo' and message.author.id == mochaid:
				await anchor.send(m[11:])
				await message.delete()
			# QUOTES
			elif qfcondition:
				if n[3:] in wholequotefiles:
					o = open(n[3:]+'.txt', 'r').read()
				else:
					o = quotefile(' '.join(ma[2:]), ma[1].lower())
				try:
					await mc.send(o)
				except discord.errors.HTTPException:
					await mc.send('Too many matches ('+str(o.count('\n'))+')')
			# GAMES
			elif na[1] == 'game':
				args = n.split(' ')[2:]
				if na[2] == '24':
					await twentyfour(mc)
				elif na[2] == 'associate':
					await associate(message)
				elif na[2] == 'gtn':
					await gtn(args, message)
				elif na[2] == 'g2/3':
					await g23(mc)
				elif na[2] == 'hangman':
					await hangman(args, message)
				elif na[2] == 'hello':
					await hello_game(message)
				elif na[2] == 'llama':
					await llama(message)
				elif na[2] == 'numbers':
					await numbers(mc)
				elif na[2] == 'verbrace':
					await verbrace(args, mc)
				elif na[2] == 'word':
					await word(args, message)
			# ELSE
			elif n.startswith(bot_prefix):
				try:
					await mc.send(special[m[3:].lower()]) # specials
				except KeyError:
					await mc.send('me confufu uwu')
		# Check filters
		if mc.id in filters:
			filter_type = filters[mc.id][0]
			lookfor = filters[mc.id][1]
			if filter_type == 'with' and search(compile(lookfor), m):
				await message.delete()
			elif filter_type == 'without' and not search(compile(lookfor), m):
				await message.delete()
	except discord.errors.Forbidden:
		pass
	# status
	timecheck[1] = time()
	if timecheck[1] > timecheck[0] + 60 or ('1453' in message.content and message.author.id == mochaid):
		await bot.change_presence(activity=discord.Game(name=new_status()))
		timecheck[0] = time()

print('Connecting...')
timecheck = [time()]*2
bot.run(token)
