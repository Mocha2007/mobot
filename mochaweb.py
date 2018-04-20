import urllib.request,mochamw
from re import compile,sub,findall,search
from random import randint

linkpattern = r'\[\[[^\]]+?\]\]'
limit = 499

user_agent = 'MochaMW/1.0 (https://github.com/Mocha2007/mochalib)'
headers={'User-Agent':user_agent,}

def l(url): #load
	request=urllib.request.Request(url,None,headers)
	webpage=urllib.request.urlopen(request).read().decode("utf-8")
	return webpage

def udcleanup(string):
	string = search(compile(r'(?<=class="meaning">)[^\0]+?(?=<\/div>)'),string).group(0) # get first def
	string = string.replace('<br/>','\n') # newline
	string = string.replace('&quot;','"') # quote
	string = sub(compile(r'<.+?>'),'',string)#.group(0) # remove links
	return string

def wtcleanup(string):
	string = sub(compile(r'====[^=]+?===='),'',string) # remove 4th header
	string = sub(compile(r'===[^=]+?==='),'',string) # remove 3rd header
	string = sub(compile(r'==[^=]+?=='),'',string) # remove 2nd header
	string = string.replace('#','\n#') # ol
	return string

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
	string = string.replace('&#39;','\'')
	title = search(r'(?<=ctitle">)[^<]+?(?=<)',string).group(0)
	img = 'https:'+search(r'(?<=src=")[^"]+?(?=" t)',string).group(0)
	alt = search(r'(?<=title=")[^"]+?(?=" a)',string).group(0)
	return '**'+title+'**\n*'+alt+'*\n'+img

def xkcd(arg):
	try:arg = 'https://xkcd.com/'+str(int(arg))
	except:arg = 'https://c.xkcd.com/random/comic/'
	return xkcdcleanup(l(arg))