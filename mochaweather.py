from json import load
from io import StringIO
import urllib.request
from re import compile,sub,findall,search

key = open("../openweathermap.txt", "r").read()

linkpattern = r'\[\[[^\]]+?\]\]'
limit = 499

user_agent = 'MochaMW/1.0 (https://github.com/Mocha2007/mochalib)'
headers={'User-Agent':user_agent}

def k2c(t):
	return t-273.16

def k2f(t):
	return 1.8*t-459.4

def l(loc): #load
	url='http://api.openweathermap.org/data/2.5/weather?q='+loc+'&appid='+key
	request=urllib.request.Request(url,None,headers)
	webpage=urllib.request.urlopen(request).read().decode("utf-8")
	return load(StringIO(webpage))

def cleanup(j):
	state = j['weather'][0]['main']
	temp = round(k2c(j['main']['temp']),2)
	tempf = round(k2f(j['main']['temp']),2)
	return str(temp)+'\xb0C ('+str(tempf)+'\xb0F) '+state

def main(loc):
	# eg main('London')
	return cleanup(l(loc))