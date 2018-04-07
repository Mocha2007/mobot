from time import time as t

def tonum(x):
	try:return int(x)
	except:	
		try:return chr(x)
		except:return len(x)

mem = [0]*256

def run(prog,inp):
	inp = list(map(tonum,inp))
	o = []
	inpn = 0
	start = t()
	pointer = 0
	i = 0
	while 1:
		try:command = prog[i]
		except:break
		
		if command == '>':pointer+=1
		elif command == '<':pointer-=1
		elif command == '+':mem[pointer]+=1
		elif command == '-':mem[pointer]-=1
		elif command == ',':
			try:mem[pointer]=inp[inpn]
			except:return 'Error: End of input'
			inpn+=1
		elif command == '.':o+=[mem[pointer]]
		elif command == '[':# jump to the next matching ]
			if mem[pointer] == 0:
				balance = 1
				while balance:
					i+=1
					try:
						if prog[i] == '[':balance+=1
						elif prog[i] == ']':balance-=1
					except:return 'Error: End of input'
				i-=1
		elif command == ']':# jump to the next matching [
			if mem[pointer]:
				balance = -1
				while balance:
					i-=1
					if prog[i] == '[':balance+=1
					elif prog[i] == ']':balance-=1
					
		pointer = pointer%256
		mem[pointer] = mem[pointer]%256
		i+=1
		if t()-start>5:return 'Took too long (5s) Stopped at char '+str(i)
	return str(o)+'\n'+''.join(map(chr,o))
