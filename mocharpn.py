from math import acos,asin,atan,ceil,cos,floor,log,sin,tan

def rpn(prog):
	decimal = False
	stack = []
	cnum = ''
	for command in prog:
		err = 'ERR @ '+command
		if command in '01234567890':
			cnum += command
		elif command == '.':
			decimal = True
			try:stack.append(int(cnum))
			except ValueError:pass
			cnum = ''
		else:
			if decimal:
				try:
					temp = stack.pop()
					temp += float('.'+cnum)
					stack.append(temp)
				except ValueError:pass
				decimal = False
			else:
				try:stack.append(int(cnum))
				except ValueError:pass
			cnum = ''

			if len(stack): # for commands requiring at least ONE number
				temp = stack.pop()
				if command in ' \t\n':
					stack.append(temp)
				elif command == '~':
					stack.append(-temp)
				elif command == 'c':
					stack.append(cos(temp))
				elif command == 'C':
					stack.append(acos(temp))
				elif command == 'l':
					stack.append(log(temp))
				elif command == 's':
					stack.append(sin(temp))
				elif command == 'S':
					stack.append(asin(temp))
				elif command == 't':
					stack.append(tan(temp))
				elif command == 'T':
					stack.append(atan(temp))
				elif command == '[':
					stack.append(floor(temp))
				elif command == ']':
					stack.append(ceil(temp))
				elif command == '|':
					stack.append(abs(temp))
				# stack manip
				elif command == ';':
					pass
				elif command == ',':
					stack += list(range(temp))
				elif command == '@':
					stack = [temp] + stack
				elif len(stack): # for commands requiring at least TWO numbers
					temp2 = stack.pop()
					if command == '+':
						stack.append(temp2+temp)
					elif command == '-':
						stack.append(temp2-temp)
					elif command == '*':
						stack.append(temp2*temp)
					elif command == '/':
						if temp == 0:return err
						stack.append(temp2/temp)
					elif command == '%':
						if temp == 0:return err
						stack.append(temp2%temp)
					elif command == '^':
						if temp == temp2 == 0:return err
						stack.append(temp2**temp)
					elif command == 'L':
						stack.append(log(temp)/log(temp2))
					# stack manip
					elif command == '\\':
						stack.append(temp)
						stack.append(temp2)
					else:return err
				else:return err
			else:return err
	return stack