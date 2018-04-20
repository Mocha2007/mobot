import urllib.request
from re import compile,sub,findall,search

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