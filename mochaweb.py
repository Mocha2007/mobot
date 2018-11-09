import urllib.request,mochamw,telnetlib
from re import compile,sub,findall,search,M
from random import choice, randint
from json import load
from io import StringIO
from discord import Embed

linkpattern = r'\[\[[^\]]+?\]\]'
limit = 499

user_agent = 'MochaWeb/1.0 (https://github.com/Mocha2007/mochalib)'
headers={'User-Agent':user_agent,}

def l(url): #load
	request=urllib.request.Request(url,None,headers)
	webpage=urllib.request.urlopen(request).read().decode("utf-8", errors='ignore')
	return webpage

try:
	swears = l('http://www.bannedwordlist.com/lists/swearWords.txt').split('\r\n')
	swears += l('https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en').split('\n')[:-1]
except:
	swears = []

def udcleanup(string):
	string = search(compile(r'(?<=class="meaning">)[^\0]+?(?=<\/div>)'),string).group(0) # get first def
	string = string.replace('<br/>','\n') # newline
	string = string.replace('&quot;','"') # quote
	string = sub(compile(r'<.+?>'),'',string)#.group(0) # remove links
	return string

def wtcleanup(string):
	string = sub(r'----[\w\W]+','',string) # crap in end
	string = sub('^[^#].+$','',string,flags=M) # delete ANY line not beginning with a hash
	string = string.replace('#','\n#') # ol
	string = sub('^[^#]+','',string) # crap in beginning
	string = sub('#[:*].+','',string) # crap in middle
	string = sub(r'\n{2,}','\n',string) # multiple returns
	string = sub(r'Category:[\w:]+','',string) # category removal
	string = sub(r'^[#*][^\w\n]+\n','',string) # empty defs
	n = 0
	for c in string:# start numbering the definitions
		if c=='#':
			n+=1
			string = string.replace(c,'**'+str(n)+'.**',1)
	return string[:2000]

def htmlescape(string):
	string = sub(r'&nbsp;',' ',string) # nbsp
	return string

def wikicleanup(string):
	string = sub(r'\s?\(.*?\)','',string) # text in parens
	string = sub(r'<ref.+?ref>','',string) # references
	string = htmlescape(string) # escape chars
	return ''.join(findall('[^.]+.',string)[:3]) # first three sentences

def ud(word):
	# eg ud('test')
	return udcleanup(l('https://www.urbandictionary.com/define.php?term='+word))

def dfprop(word):
	art = mochamw.read2('dwarffortresswiki.org','DF2014:'+word)
	temps = findall(compile(r'{{ct\|\d+}}'),art)
	for m in temps: # template ct
		art = art.replace(m,sub(r'\D','',m)+'\xb0U')
	props = search(compile(r'(?<=properties=\n)[\w\W]+?(?=}}{{av}})'),art).group(0)
	return mochamw.cleanup(props)

def xkcdcleanup(string):
	string = string.replace('&#39;','\'').replace('&quot;','"')
	title = search(r'(?<=ctitle">)[^<]+?(?=<)',string).group(0)
	img = 'https:'+search(r'(?<=src=")[^"]+?(?=" t)',string).group(0)
	alt = search(r'(?<=title=")[^"]+?(?=" a)',string).group(0)
	return '**'+title+'**\n*'+alt+'*\n'+img

def xkcd(arg):
	try:arg = 'https://xkcd.com/'+str(int(arg))
	except:arg = 'https://c.xkcd.com/random/comic/'
	return xkcdcleanup(l(arg))

def numbersapi(n):
	x = l('http://numbersapi.com/'+n)
	if 'numbersapi' in x:return n+' is a gay-ass number.'
	return x

htn = telnetlib.Telnet(host='horizons.jpl.nasa.gov',port=6775)
def horizons(name):
	htn.read_until(b'Horizons> ',timeout=1)
	htn.write(name.encode('ascii')+b'\n')
	x = htn.read_until(b'Horizons> ',timeout=1)
	if b'<cr>=yes' in x:
		htn.write(b'\n')
		x = htn.read_until(b'Select ...',timeout=1)
	return sub(r'^[^*]*\*+|\*+[^*]*$','',x.decode('ascii'))

fixerioapikey = open('../fixer.io.txt','r').read()
j = False
def currency(a,b):
	global j
	if not j:j = load(StringIO(l('http://data.fixer.io/api/latest?access_key='+fixerioapikey)))

	if a != 'EUR':a = j['rates'][a]
	else:a = 1

	if b != 'EUR':b = j['rates'][b]
	else:b = 1
	
	return b/a

def califire():
	page = l('http://iscaliforniaonfire.com/').split('\n')[5:7] # just the two relevant lines
	page = '\n'.join(page) # reconnect
	page = page.replace('<h1>', '**').replace('</h1>', '**')
	return page

def metar(string):
	page = l('https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=csv&stationString='+string+'&hoursBeforeNow=1')
	page = page.split('\n')[5:] # split & get only relevant lines
	# halve
	page1 = page[0].split(',')
	page2 = page[1].split(',')
	s = 'METAR data for '+string
	for title, entry in zip(page1, page2):
		s += '\n'+title+'\t'+entry
	return '```\n' + s + '```'

def gi(searchstring: str):
	for swear in swears:
		if swear in searchstring:
			return gi('nope')
	url = 'https://www.google.com/search?tbm=isch&q='+searchstring.replace(' ', '%20')
	o = Embed(title=searchstring, type="rich", url=url, color=0x00ff00)
	# now time to find an image!
	page = l(url)
	# delete first 562 lines; it's just bloated js
	line = page.split('\n')[-1]
	images = findall('<img.+?>', line)
	images = list(map(lambda x: search(r'(?<=src=").+?(?=")', x), images))
	# set image and return
	image = images[0].group(0)
	o.set_image(url=image) # 'https://i.ytimg.com/vi/_9v1Q5MurnM/maxresdefault.jpg'
	return o

def jisho(searchstring: str):
	url = 'https://jisho.org/api/v1/search/words?keyword='+searchstring
	embed = Embed(title=searchstring, type="rich", url=url, color=0x56D926)
	true, false = True, False
	try:
		json = eval(l(url))
	except UnicodeEncodeError:
		return embed
	jp_word = json['data'][0]['japanese'][0] # {} with word and reading
	embed.add_field(name='Word', value=jp_word['word'], inline=False)
	embed.add_field(name='Reading', value=jp_word['reading'], inline=False)
	# o = jp_word['word']+'\n'+jp_word['reading']
	o = ''
	en_senses = []
	for sense in json['data'][0]['senses']:
		o += '\n'+', '.join(sense['parts_of_speech'])
		o += '\n\t* '.join(['']+sense['english_definitions'])
	embed.add_field(name='Entry', value=o, inline=False)
	return embed

def tarot():
	json = eval(l('https://raw.githubusercontent.com/dariusk/corpora/master/data/divination/tarot_interpretations.json'))
	cards = json["tarot_interpretations"]
	card = choice(cards)
	#
	embed = Embed(title=card['name'].title(), type="rich", color=0x8000FF)
	embed.add_field(name='Fortune Telling', value='\n'.join(card['fortune_telling']), inline=False)
	embed.add_field(name='Keywords', value='\n'.join(card['keywords']).title(), inline=False)
	embed.add_field(name='Meanings (Light)', value='\n'.join(card['meanings']['light']), inline=False)
	embed.add_field(name='Meanings (Shadow)', value='\n'.join(card['meanings']['shadow']), inline=False)
	embed.add_field(name='Rank', value=str(card['rank']), inline=False)
	embed.add_field(name='Suit', value=card['suit'].title(), inline=False)
	return embed

def jeopardy():
	null = None
	json = eval(l('https://raw.githubusercontent.com/dariusk/corpora/master/data/games/jeopardy_questions.json'))
	card = choice(json["questions"])
	#
	embed = Embed(title='Category: '+card['category'], type="rich", color=0x000080)
	embed.add_field(name='Question', value=card['question'], inline=False)
	return embed, card['answer']
