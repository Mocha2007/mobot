# TODO
# random fact
from discord.ext.commands import Bot
import discord

from random import choice as c
from math import acos,asin,atan,ceil,cos,floor,gcd,hypot,log,pi,sin,tan
from time import time
import mochaastro,mochalang,mochamath

# CODE SHIT
def help():
	return open("help.txt", "r").read()

def mobotlink():
	return open("link.txt", "r").read()

moquote = open("moquote.txt", "r").read().split('\n')

religions = {
'catholicism':{'members':1.285e9,'partof':'Christianity','url':'https://en.wikipedia.org/wiki/Catholic_Church'},
'christianity':{'members':2.4e9,'partof':'Abrahamic Religions','url':'https://en.wikipedia.org/wiki/Christianity'},
'islam':{'members':1.8e9,'partof':'Abrahamic Religions','url':'https://en.wikipedia.org/wiki/Islam'},
'moonism':{'members':1,'partof':'Crazy Shit','url':'HAIL MOON'},
'shia':{'members':200e6,'partof':'Islam','url':'https://en.wikipedia.org/wiki/Shia_Islam'},
'sunni':{'members':1.6e9,'partof':'Islam','url':'https://en.wikipedia.org/wiki/Sunni_Islam'},
'talos':{'members':'1 (Heimskr)','partof':'Nine Divines','url':'http://en.uesp.net/wiki/Lore:Tiber_Septim'},
'wicca':{'members':750000,'partof':'n/a','url':'https://en.wikipedia.org/wiki/Wicca'},
}

special = {
'alexa':'do i look like a slave to you?',
'ban':'u can\'t make me!!!',
'hey google':'hey yourself faggot',
'up':'five more minutes sky daddy',
}

xskey = [
('b_<','ɓ'),
('d`','ɖ'),
('d_<','ɗ'),
('g_<','ɠ'),
('h\\','ɦ'),
('j\\','ʝ'),
('l`','ɭ'),
('l\\','ɺ'),
('n`','ɳ'),
('p\\','ɸ'),
('r`','ɽ'),
('r\\','ɹ'),
('r\\`','ɻ'),
('s`','ʂ'),
('s\\','ɕ'),
('t`','ʈ'),
('v\\','ʋ'),
('x\\','ɧ'),
('z`','ʐ'),
('z\\','ʑ'),
('A','ɑ'),
('B','β'),
('B\\','ʙ'),
('C','ç'),
('D','ð'),
('E','ɛ'),
('F','ɱ'),
('G','ɣ'),
('G\\','ɢ'),
('G\\_<','ʛ'),
('H','ɥ'),
('H\\','ʜ'),
('I','ɪ'),
('I\\','ɪ̈'),
('J','ɲ'),
('J\\','ɟ'),
('J\\_<','ʄ'),
('K','ɬ'),
('K\\','ɮ'),
('L','ʎ'),
('L\\','ʟ'),
('M','ɯ'),
('M\\','ɰ'),
('N','ŋ'),
('N\\','ɴ'),
('O','ɔ'),
('O\\','ʘ'),
('P','ʋ'),
('Q','ɒ'),
('R','ʁ'),
('R\\','ʀ'),
('S','ʃ'),
('T','θ'),
('U','ʊ'),
('U\\','ʊ̈'),
('V','ʌ'),
('W','ʍ'),
('X','χ'),
('X\\','ħ'),
('Y','ʏ'),
('Z','ʒ'),
('.','.'),
('"','ˈ'),
('%','ˌ'),
('\'','ʲ'),
(':','ː'),
(':\\','ˑ'),
('@','ə'),
('@\\','ɘ'),
('{','æ'),
('}','ʉ'),
('1','ɨ'),
('2','ø'),
('3','ɜ'),
('3\\','ɞ'),
('4','ɾ'),
('5','ɫ'),
('6','ɐ'),
('7','ɤ'),
('8','ɵ'),
('9','œ'),
('&','ɶ'),
('?','ʔ'),
('?\\','ʕ'),
('<\\','ʢ'),
('>\\','ʡ'),
('^','ꜛ'),
('!','ꜜ'),
('!\\','ǃ'),
('|\\|\\','ǁ'),
('|\\','ǀ'),
('||','‖'),
('|','|'),
('=\\','ǂ'),
('-\\','‿'), # TODO: diacritics
('_>','ʼ'),
('_?\\','ˤ'),
('<F>','↘'),
('_G','ˠ'),
('_h','ʰ'),
('_j','ʲ'),
('_n','ⁿ'),
('<R>','↗'),
('_w','ʷ')
]

sun={'r':6.957e8,'m':1.98855e30}
moon={'a':384399000,'e':0.0549,'r':1737100,'m':7.342e22}
object = {
'sun':sun,
'moon':moon,
'mercury':mochaastro.mercury,
'venus':mochaastro.venus,
'earth':mochaastro.earth,
'mars':mochaastro.mars,
'jupiter':mochaastro.jupiter,
'saturn':mochaastro.saturn,
'uranus':mochaastro.uranus,
'neptune':mochaastro.neptune,
'planetnine':mochaastro.planetnine
}

def rpn(prog):
	stack = []
	cnum = ''
	for command in prog:
		if command in '01234567890':
			cnum += command
		elif command in ', ':
			try:stack += [int(cnum)]
			except ValueError:pass
			cnum = ''
		# stack manip
		elif len(stack): # for commands requiring at least ONE number
			if command == '~':
				temp = stack.pop()
				stack.append(-temp)
			elif command == 'c':
				temp = stack.pop()
				stack.append(cos(temp))
			elif command == 'C':
				temp = stack.pop()
				stack.append(acos(temp))
			elif command == 'l':
				temp = stack.pop()
				stack.append(log(temp))
			elif command == 's':
				temp = stack.pop()
				stack.append(sin(temp))
			elif command == 'S':
				temp = stack.pop()
				stack.append(asin(temp))
			elif command == 't':
				temp = stack.pop()
				stack.append(tan(temp))
			elif command == 'T':
				temp = stack.pop()
				stack.append(atan(temp))
			elif command == '[':
				temp = stack.pop()
				stack.append(floor(temp))
			elif command == ']':
				temp = stack.pop()
				stack.append(ceil(temp))
			elif command == '|':
				temp = stack.pop()
				stack.append(abs(temp))
			# stack manip
			elif command == ';':
				stack.pop()
			elif command == '.':
				temp = stack.pop()
				stack.append(temp)
				stack.append(temp)
			elif command == '@':
				temp = stack.pop()
				stack = [temp] + stack
			elif len(stack)>=2: # for commands requiring at least ONE number
				if command == '+':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2+temp)
				elif command == '-':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2-temp)
				elif command == '*':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2*temp)
				elif command == '/':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == 0:return 'Nice try, sweetheart.'
					stack.append(temp2/temp)
				elif command == '%':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == 0:return 'Nice try, sweetheart.'
					stack.append(temp2%temp)
				elif command == '^':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == temp2 == 0:return 'Nice try, sweetheart.'
					stack.append(temp2**temp)
				elif command == 'L':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(log(temp)/log(temp2))
				# stack manip
				elif command == '\\':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp)
					stack.append(temp2)
				else:
					stack = 'ERR @ '+command
					break
			else:
				stack = 'ERR @ '+command
				break
		else:
			stack = 'ERR @ '+command
			break
	return stack

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
	elif arg[0] == 'map':
		a = list(map(float,arg[2:]))
		f = arg[1]
		return eval('list(map('+f+',a))')
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
	elif arg[0] == 'synodic':
		a = float(arg[1])
		b = float(arg[2])
		return mochaastro.synodic(a,b)

	try:return object[arg[0]][arg[1]]
	except:return ':/'

def moling(string):
	arg = string.split(' ')

	if arg[0] == 'soundex':
		return mochalang.soundex(arg[1])
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
	elif arg[0] == 'x-sampa':
		return xsampa(arg[1])

	return ':/'

def sto(string):
	arg = string.split(' ')

	if arg[0] == 'sto':
		open("temp.txt", "a").write(' '.join(arg[1:])+'\n')
		return 'Success!'
	elif arg[0] == 'get':
		q = c(open("temp.txt", "r").read().split('\n'))
		if q!='\n':return q

	return sto('get')

def bee(line):
	if line == '':
		q = c(open("bee.txt", "r").read().split('\n'))
		return q
	q = open("bee.txt", "r").read().split('\n')[int(line)]
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

def coffee(arg):
	coffees = {
	'':'coffee',
	'americano':'espresso\nhot water',
	'grande':'16 oz cup',
	'latte':'espresso\nhot milk',
	'macchiato':'espresso\nhot milk',
	'mocha':'chocolate\nespresso\nhot milk\n\n(also my senpai uwu)',
	'tall':'8 oz cup',
	'venti':'20 oz cup',
	}
	try:return '```\n'+coffees[arg]+'```'
	except KeyError:return ':/'

def convert(uwaa):
	units = {
	'au':149597870700,
	'banana':.3048*8/12,
	'cm':.01,
	'd':86400,
	'fir':40.8233133,
	'ft':.3048,
	'ftn':1209600,
	'fur':201.168,
	'g':.001,
	'gal':.00454609,
	'h':3600,
	'in':.3048/12,
	'jyr':31536000, # julian year
	'kg':1,
	'km':1000,
	'l':.001,
	'lb':.45359237,
	'league':5556,
	'ly':9.4607e15,
	'm':1,
	'mi':1609.344,
	'min':60,
	'mm':.001,
	'nmi':1852,
	'oz':.0283,
	'pc':3.0857e18,
	'penis':.129,
	's':1,
	'si':1, # for general si conversion
	'yd':.9144,
	'yr':31556952,
	}
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

	if message.content.startswith(bot_prefix):
		print(message.content)
		open("log.txt", "a").write(message.content+'\n')

	if 'mobot' in m.lower():
		try:await client.send_message(message.channel, c(['das meee :3','hai!~']))
		except:pass

	if m.lower() == 'owo':
		await client.send_message(message.channel, '*What\'s this???*')
	elif m.startswith(bot_prefix+'help'):
		await client.send_message(message.channel, help())
	elif m.startswith(bot_prefix+'link'):
		await client.send_message(message.channel, mobotlink())
	elif m.startswith(bot_prefix+'hi'):
		await client.send_message(message.channel, c(['fuck off','go fuck yourself','die in a fire','go to hell','go drink some bleach','ur mom gay']))
	elif m.startswith(bot_prefix+'moquote'):
		await client.send_message(message.channel, c(moquote))
	elif m.startswith(bot_prefix+'rpn'):
		await client.send_message(message.channel, str(rpn(m[7:])))
	elif m.startswith(bot_prefix+'mat'):
		await client.send_message(message.channel, str(momath(m[7:])))
	elif m.startswith(bot_prefix+'ast'):
		await client.send_message(message.channel, str(moastro(m[7:])))
	elif m.startswith(bot_prefix+'ling'):
		await client.send_message(message.channel, str(moling(m[8:])))
	elif m.startswith(bot_prefix+'quote'):
		await client.send_message(message.channel, str(sto(m[9:])))
	elif m.startswith(bot_prefix+'zodiac'):
		await client.send_message(message.channel, str(zodiac(m[10:])))
	elif m.startswith(bot_prefix+'coffee'):
		await client.send_message(message.channel, str(coffee(m[10:])))
	elif m.startswith(bot_prefix+'convert'):
		await client.send_message(message.channel, str(convert(m[11:])))
	elif m.startswith(bot_prefix+'religion'):
		await client.send_message(message.channel, str(religion(m[12:])))
	elif m.startswith(bot_prefix+'bee'):
		await client.send_message(message.channel, str(bee(m[7:])))
	elif m.startswith(bot_prefix):
		try:await client.send_message(message.channel, special[m[3:]])
		except KeyError:await client.send_message(message.channel,'me confufu uwu')

print('Loaded')
#gayme = discord.Game('you like a fiddle')
#client.change_status(game=gayme, idle=False)
client.run(token)
