def typeof(x):
	return type(x).__name__

def pre(prog):
	return prog # unimplemented so far

def main(prog):
	comment = False
	stack = []
	cnum = ''
	for i in range(len(prog)):
		command = prog[i]
		errorcode = 'error @ char'+str(i)+': '+command
		#TODO ' " : and or xor print p n puts rand do while until if abs zip base
		if not comment:
			if command in '0123456789':
				cnum += command
			elif command == ' ':
				try:stack.append(int(cnum))
				except:return errorcode
				cnum = ''
			elif command == '#':
				comment = True
			elif cnum!='':
				try:stack.append(int(cnum))
				except:return errorcode
				cnum = ''
				if False:
					pass
				elif len(stack): # for commands requiring at least ONE var
					temp = stack.pop()
					if command == '~':
						if typeof(temp) == 'int':stack.append(~temp)
						elif typeof(temp) == 'str':stack.append(run(temp))
						elif typeof(temp) == 'list':
							for j in temp:
								stack.append(j)
						else:return errorcode
					elif command == '`':
						stack.append(str(temp))
					elif command == '!':
						if temp in ([],0,''):stack.append(1)
						else:stack.append(0)
					elif command == '$':
						if typeof(temp) == 'int':
							stack.append(stack[len(stack)-1-temp])
						else:
							stack.append(sorted(temp))
					elif command == ';':
						pass
					elif command == ',':
						if typeof(temp) == 'int':
							stack.append(list(range(temp)))
						else:
							stack.append(len(temp))
					elif command == '.':
						stack.append(temp)
						stack.append(temp)
					elif command == '(':
						try:
							if typeof(temp) == 'int':
								stack.append(temp-1)
							else:
								stack.append(temp[0])
								stack.append(temp[1:])
						except:return errorcode
					elif command == ')':
						try:
							if typeof(temp) == 'int':
								stack.append(temp-1)
							else:
								stack.append(temp[:-1])
								stack.append(temp[-1])
						except:return errorcode
					elif len(stack)>=2: # for commands requiring at least TWO vars
						temp2 = stack.pop()
						if command == '+':
							if typeof(temp) == 'int' == typeof(temp2) or typeof(temp) == 'list' == typeof(temp2): # int int or arr arr
								stack.append(temp+temp2)
							elif typeof(temp) == 'str' or 'str' == typeof(temp2): # either string
								stack.append(str(temp2)+str(temp))
							elif typeof(temp) == 'int': # int arr
								stack.append([temp2]+temp)
							elif typeof(temp2) == 'int': # arr int
								stack.append(temp2+[temp])
							else:return errorcode
						elif command == '-':
							try:stack.append(temp2-temp)
							except:return errorcode
						# TODO *
						# TODO /
						# TODO %
						elif command == '|':
							try:stack.append(temp2|temp)
							except:return errorcode
						elif command == '&':
							try:stack.append(temp2&temp)
							except:return errorcode
						elif command == '^':
							try:stack.append(temp2^temp)
							except:return errorcode
						elif command == '\\':
							stack.append(temp)
							stack.append(temp2)
						elif command == '<':
							try:stack.append(temp2<temp)
							except:return errorcode
						elif command == '>':
							try:stack.append(temp2>temp)
							except:return errorcode
						elif command == '=':
							try:stack.append(temp2==temp)
							except:return errorcode
						elif command == '?':
							if typeof(temp) == 'int' == typeof(temp2):
								stack.append(temp2**temp)
							else:
								try:stack.append(temp.index(temp2))
								except:stack.append(-1)
						elif len(stack)>=3: # for commands requiring at least THREE vars
							temp3 = stack.pop()
							if command == '@':
								stack.append(temp2)
								stack.append(temp)
								stack.append(temp3)
							else:return errorcode
						else:return errorcode
					else:return errorcode
				else:return errorcode
			else:return errorcode
		elif command == '\n':comment = False
	if cnum!='':
		try:stack.append(int(cnum))
		except:pass
	return stack

def run(prog):
	return main(pre(prog))