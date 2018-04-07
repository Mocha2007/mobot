def typeof(x):
	return type(x).__name__

def pre(prog):
	return prog

def main(prog):
	var = {'n':'\n'}
	comment = False
	string = False
	stack = []
	cnum = ''
	for i in range(len(prog)):
		command = prog[i]
		errorcode = 'error @ char '+str(i)+': '+command+'\n\tstack ('+str(len(stack))+'): '+str(stack)+'\n\tcode '
		#TODO ' " : and or xor print p puts rand do while until if abs zip base
		try:isdefined = prog[i-1] == ':'
		except:isdefined = False
		if not comment and not isdefined:
			if string or command in '0123456789':
				cnum += command
			elif command == ' ' and not string or command == '\'' and string: # ADD ESCAPE SEQUENCES PLEASE
				if string:
					stack.append(cnum)
				else:
					try:stack.append(int(cnum))
					except:return errorcode+'a'
				cnum = ''
			elif command == '#':
				comment = True
			elif command == '\'':
				string = True
			else:
				if cnum!='':
					try:
						stack.append(int(cnum))
						cnum = ''
					except:return errorcode+'b'
				if command in var:
					stack.append(var[command])
				elif len(stack): # for commands requiring at least ONE var
					temp = stack.pop()
					if command == '~':
						if typeof(temp) == 'int':stack.append(~temp)
						elif typeof(temp) == 'str':stack.append(run(temp))
						elif typeof(temp) == 'list':
							for j in temp:
								stack.append(j)
						else:return errorcode+'c'
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
					elif command == ':':
						stack.append(temp)
						var[prog[i+1]] = temp
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
						except:return errorcode+'d'
					elif command == ')':
						try:
							if typeof(temp) == 'int':
								stack.append(temp-1)
							else:
								stack.append(temp[:-1])
								stack.append(temp[-1])
						except:return errorcode+'e'
					elif len(stack): # for commands requiring at least TWO vars
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
							else:return errorcode+'f'
						elif command == '-':
							try:stack.append(temp2-temp)
							except:return errorcode+'g'
						# TODO *
						# TODO /
						# TODO %
						elif command == '|':
							try:stack.append(temp2|temp)
							except:return errorcode+'h'
						elif command == '&':
							try:stack.append(temp2&temp)
							except:return errorcode+'i'
						elif command == '^':
							try:stack.append(temp2^temp)
							except:return errorcode+'j'
						elif command == '\\':
							stack.append(temp)
							stack.append(temp2)
						elif command == '<':
							try:stack.append(temp2<temp)
							except:return errorcode+'k'
						elif command == '>':
							try:stack.append(temp2>temp)
							except:return errorcode+'l'
						elif command == '=':
							try:stack.append(temp2==temp)
							except:return errorcode+'m'
						elif command == '?':
							if typeof(temp) == 'int' == typeof(temp2):
								stack.append(temp2**temp)
							else:
								try:stack.append(temp.index(temp2))
								except:stack.append(-1)
						elif len(stack): # for commands requiring at least THREE vars
							temp3 = stack.pop()
							if command == '@':
								stack.append(temp2)
								stack.append(temp)
								stack.append(temp3)
							else:return errorcode+'n'
						else:return errorcode+'o'
					else:return errorcode+'p'
				else:return errorcode+'q'
		elif command == '\n':
			comment = False
	if cnum!='':
		try:stack.append(int(cnum))
		except:pass
	return stack

def run(prog):
	return main(pre(prog))