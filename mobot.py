# TODO
# random fact
from discord.ext.commands import Bot
import discord

from random import choice as c
from math import gcd,hypot,pi
from time import time
import mochaastro,mochabf,mochagolfscript,mochalang,mochamath,mocharpn,mochastargen
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
'spidey'
]

def product(numlist):
	if len(numlist) == 0:return 0
	if len(numlist) == 1:return numlist[0]
	return numlist[0] * product(numlist[1:])

def momath(string):
	arg = string.lower().split(' ')

	# simple

	if arg[0] == 'circumference':
		return float(arg[2])*pi
	elif arg[0] == 'ecc':
		a = float(arg[1])
		b = float(arg[2])
		return (1-b**2/a**2)**.5
	elif arg[0] == 'hypot':
		return hypot(float(arg[1]),float(arg[2]))

	# complex

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
			return float(arg[2])+float(arg[3])/2
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

	if arg[0] == 'sto':
		inputendo = ' '.join(arg[1:])
		if '<@!' in inputendo:return 'Not happening.'
		open("temp.txt", "a").write(inputendo+'\n')
		return 'Success!'

	try:q = open("temp.txt", "r").read().split('\n')[int(arg[0])]
	except:q = c(open("temp.txt", "r").read().split('\n'))
	if q not in '\n ':return q
	return sto('get')

def bug(string):
	open("bug.txt", "a").write(string+'\n')
	return 'Success!'

def quotefile(line,file):
	if line == '':
		q = c(open(file+".txt", "r").read().split('\n'))
		return q
	q = open(file+".txt", "r").read().split('\n')[int(line)]
	return q

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

# ACUTAL BOT SHIT

bot_prefix = "m! "
token = open("../token.txt", "r").read()

client = Bot(command_prefix = bot_prefix)

@client.event
async def on_message(message):
	m = message.content
	n = m.lower()
	try:qf = n.split(' ')[1]
	except: qf = False

	if message.content.startswith(bot_prefix):
		loglook = str(message.timestamp)[:19]+' - @'+str(message.author)+' (#'+str(message.channel)+' in '+str(message.server)+')\n\t'+message.content
		try:print(loglook)
		except UnicodeEncodeError:
			try:print(str(message.timestamp)[:19]+'\n\t'+message.content)
			except UnicodeEncodeError:print(str(message.timestamp)[:19]+' [Unable to read message]')
		try:open("log.txt", "a").write(loglook+'\n')
		except UnicodeEncodeError as e:open("log.txt", "a").write(str(e)+'\n')

	if 'mobot' in m.lower():
		try:await client.send_message(message.channel, c(['das meee :3','hai!~']))
		except:pass

	if n == 'owo':
		await client.send_message(message.channel, '*What\'s this???*')
	# MAIN
	elif n.startswith(bot_prefix+'help'):
		await client.send_message(message.channel, help(m[8:]))
	elif n.startswith(bot_prefix+'bf'):
		await client.send_message(message.channel, str(mochabf.run(m[6:])))
	elif n.startswith(bot_prefix+'gs'):
		await client.send_message(message.channel, str(mochagolfscript.run(m[6:])))
	elif n.startswith(bot_prefix+'ast'):
		await client.send_message(message.channel, str(moastro(m[7:])))
	elif n.startswith(bot_prefix+'bug'):
		await client.send_message(message.channel, str(bug(m[7:])))
	elif n.startswith(bot_prefix+'mat'):
		await client.send_message(message.channel, str(momath(m[7:])))
	elif n.startswith(bot_prefix+'rpn'):
		await client.send_message(message.channel, str(mocharpn.rpn(m[7:])))
	elif n.startswith(bot_prefix+'ling'):
		await client.send_message(message.channel, str(moling(m[8:])))
	elif n.startswith(bot_prefix+'mbti'):
		await client.send_message(message.channel, str(mbti(m[8:])))
	elif n.startswith(bot_prefix+'quote'):
		await client.send_message(message.channel, str(sto(m[9:])))
	elif n.startswith(bot_prefix+'zodiac'):
		await client.send_message(message.channel, str(zodiac(m[10:])))
	elif n.startswith(bot_prefix+'coffee'):
		await client.send_message(message.channel, str(coffee(m[10:])))
	elif n.startswith(bot_prefix+'convert'):
		await client.send_message(message.channel, str(convert(m[11:])))
	elif n.startswith(bot_prefix+'religion'):
		await client.send_message(message.channel, str(religion(m[12:])))
	# QUOTES
	elif qf in quotefiles:
		await client.send_message(message.channel, quotefile(m[4+len(qf):],qf))
	# ELSE
	elif n.startswith(bot_prefix):
		try:await client.send_message(message.channel, special[m[3:].lower()]) # specials
		except KeyError:await client.send_message(message.channel,'me confufu uwu')

print('Loaded')
client.run(token)