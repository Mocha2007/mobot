from time import time as t

mem = [0]*256

def run(prog):
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
		elif command == '[':# jump to the next matching ]
			if mem[pointer] == 0:
				balance = 1
				while balance:
					i+=1
					if prog[i] == '[':balance+=1
					elif prog[i] == ']':balance-=1
				i-=1
		elif command == ']':# jump to the next matching [
			if mem[pointer]:
				balance = -1
				while balance:
					i-=1
					if prog[i] == '[':balance+=1
					elif prog[i] == ']':balance-=1
					
		pointer = pointer%256
		i+=1
		if t()-start>5:return 'Took too long (5s)'
	return str(mem)+'\n'+''.join(map(chr,mem))