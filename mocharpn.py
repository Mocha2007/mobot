from math import acos, asin, atan, ceil, cos, e, floor, log, pi, sin, tan
from re import sub

digits = '01234567890'


def rpn(prog: str):
	decimal = False
	stack = []
	cnum = ''
	for command in prog:
		err = 'ERR @ '+command
		if command in digits:
			cnum += command
		elif command == '.':
			decimal = True
			try:
				stack.append(int(cnum))
			except ValueError:
				pass
			cnum = ''
		else:
			if decimal:
				try:
					temp = stack.pop()
					temp += float('.'+cnum)
					stack.append(temp)
				except ValueError:
					pass
				decimal = False
			else:
				try:
					stack.append(int(cnum))
				except ValueError:
					pass
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
						if temp == 0:
							return err
						stack.append(temp2/temp)
					elif command == '%':
						if temp == 0:
							return err
						stack.append(temp2 % temp)
					elif command == '^':
						if temp == temp2 == 0:
							return err
						stack.append(temp2**temp)
					elif command == 'L':
						stack.append(log(temp)/log(temp2))
					# stack manip
					elif command == '\\':
						stack.append(temp)
						stack.append(temp2)
					else:
						return err
				else:
					return err
			else:
				return err
	return stack


def infix(x: str) -> str:
	# case insensitive
	x = x.lower()
	# 2e -> 2*e
	x = sub(r'(?<=\d)e', '*e', x)
	x = sub(r'(?<=\d)pi', '*pi', x)
	# sub e and pi appropriately, also xX->*
	x = x.replace('e', str(e))
	x = x.replace('pi', str(pi))
	x = x.replace('x', '*')
	x = x.replace('arc', 'a')
	x = x.replace('sin', 's')
	x = x.replace('cos', 'c')
	x = x.replace('tan', 't')
	x = x.replace('ln', 'l')
	x = x.replace('log', 'l')
	# strip non-digits, non- ()+-*/^.
	x = sub('[^%(-9^aclst]|,', '', x)
	# readd sin cos tan log
	x = x.replace('s', 'sin')
	x = x.replace('c', 'cos')
	x = x.replace('t', 'tan')
	x = x.replace('l', 'log')
	# ^ -> **
	x = sub(r'\^', '**', x)
	# eg. 3(5) -> 3*(5)
	for n in digits+')':
		x = x.replace(n+'(', n+'*(')
	# eg. (5)3 -> (5)*3
	for n in digits:
		x = x.replace(')'+n, ')*'+n)
	# eval. used to have actual code here, but then i realized eval would be guaranteed safe and easy
	try:
		x = eval(x) # ^(a|sin|cos|tan|log)+$ matches all functions usable by eval
	except:
		return 'ERROR'
	try:
		if x % 1 == 0:
			x = int(x)
	except TypeError:
		pass # in case of complex number
	return str(x) # always a string
