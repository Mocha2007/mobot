from random import choice as c
from random import randint as r
from mochaxyz import grammarq

def wilson(u,d):
	z = 1.95 # 95% confidence
	n = u+d
	a = (u+z**2/2)/(n+z**2)
	b = z/(n+z**2)*(u*d/n+z**2/4)**.5
	return a-b

def rpair():
	return r(0,12),r(0,12)

def rgrammar():
	return c(grammarq)