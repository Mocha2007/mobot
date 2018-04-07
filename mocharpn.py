from math import acos,asin,atan,ceil,cos,floor,log,sin,tan

def rpn(prog):
	decimal = False
	stack = []
	cnum = ''
	for command in prog:
		if command in '01234567890':
			cnum += command
		elif command == '.':
			decimal = True
			try:stack.append(int(cnum))
			except ValueError:pass
			cnum = ''
		elif command in ', ':
			if not decimal:
				try:stack.append(int(cnum))
				except ValueError:pass
			else:
				try:
					temp = stack.pop()
					temp += float('.'+cnum)
					stack.append(temp)
				except ValueError:pass
				decimal = False
			cnum = ''
		elif len(stack): # for commands requiring at least ONE number
			if command == '~':
				temp = stack.pop()
				stack.append(-temp)
			elif command == 'c':
				temp = stack.pop()
				stack.append(cos(temp))
			elif command == 'C':
				temp = stack.pop()
				stack.append(acos(temp))
			elif command == 'l':
				temp = stack.pop()
				stack.append(log(temp))
			elif command == 's':
				temp = stack.pop()
				stack.append(sin(temp))
			elif command == 'S':
				temp = stack.pop()
				stack.append(asin(temp))
			elif command == 't':
				temp = stack.pop()
				stack.append(tan(temp))
			elif command == 'T':
				temp = stack.pop()
				stack.append(atan(temp))
			elif command == '[':
				temp = stack.pop()
				stack.append(floor(temp))
			elif command == ']':
				temp = stack.pop()
				stack.append(ceil(temp))
			elif command == '|':
				temp = stack.pop()
				stack.append(abs(temp))
			# stack manip
			elif command == ';':
				stack.pop()
			elif command == '@':
				temp = stack.pop()
				stack = [temp] + stack
			elif len(stack)>=2: # for commands requiring at least ONE number
				if command == '+':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2+temp)
				elif command == '-':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2-temp)
				elif command == '*':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp2*temp)
				elif command == '/':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == 0:return 'Nice try, sweetheart.'
					stack.append(temp2/temp)
				elif command == '%':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == 0:return 'Nice try, sweetheart.'
					stack.append(temp2%temp)
				elif command == '^':
					temp = stack.pop()
					temp2 = stack.pop()
					if temp == temp2 == 0:return 'Nice try, sweetheart.'
					stack.append(temp2**temp)
				elif command == 'L':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(log(temp)/log(temp2))
				# stack manip
				elif command == '\\':
					temp = stack.pop()
					temp2 = stack.pop()
					stack.append(temp)
					stack.append(temp2)
				else:
					stack = 'ERR @ '+command
					break
			else:
				stack = 'ERR @ '+command
				break
		else:
			stack = 'ERR @ '+command
			break
	return stack