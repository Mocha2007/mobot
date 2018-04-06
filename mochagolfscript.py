def typeof(x)
	return type(x).__name__

def pre(prog):
	return prog # unimplemented so far

def main(prog):
	stack = []
	cnum = ''
	for i in prog:
		command = prog[i]
		errorcode = 'error @ char'+str(i)+': '+command
		if command in '0123456789':
			cnum += command
		elif command == ' ':
			try:stack.append(int(cnum))
			except:return errorcode
			cnum = ''
		elif len(stack): # for commands requiring at least ONE number
			if command == '~':
				temp = stack.pop()
				if typeof(temp) == 'int':stack.append(~temp)
				elif typeof(temp) == 'str':stack.append(run(temp))
				elif typeof(temp) == 'list':
					for j in temp:
						stack.append(j)
				else:return errorcode
			elif len(stack)>=2: # for commands requiring at least ONE number
				if command == '++':
					pass
				else:return errorcode
			else:return errorcode
		else:return errorcode
	return stack

def run(prog):
	return main(pre(prog))