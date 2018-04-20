import urllib.request,mochamw
from re import compile,sub,findall,search,M
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
	string = sub('^[^#].+$','',string,flags=M) # delete ANY line not beginning with a hash
	string = string.replace('#','\n#') # ol
	string = sub('^[^#]+','',string) # crap in beginning
	string = sub('#[:*].+','',string) # crap in middle
	string = sub(r'----[\w\W]+','',string) # crap in end
	string = sub(r'\n{2,}','\n',string) # multiple returns
	string = sub(r'Category:[\w:]+','',string) # category removal
	string = sub(r'^[#*][^\w\n]+\n','',string) # empty defs
	return string

def wikicleanup(string):
	string = sub(r'\s?\(.*?\)','',string) # text in parens
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