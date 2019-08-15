def won(p):
	m = (p[6], p[7], p[8]), (p[3], p[4], p[5]), (p[0], p[1], p[2])
	# check for verticals
	for i in range(3):
		if m[0][i]+m[1][i]+m[2][i] == 'xxx':
			return 'x'
		if m[0][i]+m[1][i]+m[2][i] == 'ooo':
			return 'o'
	# check for horizontals
	for i in range(3):
		if m[i] == ('x',)*3:
			return 'x'
		if m[i] == ('o',)*3:
			return 'o'
	# check \
	if m[0][0]+m[1][1]+m[2][2] == 'xxx':
		return 'x'
	if m[0][0]+m[1][1]+m[2][2] == 'ooo':
		return 'o'
	# check /
	if m[0][2]+m[1][1]+m[2][0] == 'xxx':
		return 'x'
	if m[0][2]+m[1][1]+m[2][0] == 'ooo':
		return 'o'
	return ''


def togo(p: str) -> str:
	s = 0
	for n in p:
		if n == 'x':
			s += 1
		elif n == 'o':
			s -= 1
	if s == 0:
		return 'x'
	if s == 1:
		return 'o'
	return 'Illegal Position'


def moves(p: str) -> str:
	return p.replace('x', '').replace('o', '')


def opp(p: str) -> str:
	return 'o' if togo(p) == 'x' else 'x'


def ai(position: str):
	p = position.replace(' ', '').lower()
	if len(p) != 9:
		return 'Invalid Position'
	if p in ('123456789', '1234x6789'):
		return 7
	# checking
	if won(p):
		return 'Game Already Won'
	# for all possible moves
	tg = togo(p)
	if tg[0] == 'I':
		return tg
	opponent = opp(p)
	m = moves(p)
	# can the ai immediately win?
	for move in m:
		if won(p.replace(move, tg)):
			return move
	# can the opponent win just after?
	for move in m:
		if won(p.replace(move, opponent)):
			return move
	# can the ai win in two?
	for move in m:
		p2 = p.replace(move, tg)
		for move2 in moves(p2):
			if won(p2.replace(move2, tg)):
				return move
	# failsafe
	for i in '579138426':
		if i in p:
			return i
	return 'Game Already Drawn'
