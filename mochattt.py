def won(p):
	m = (p[6],p[7],p[8]),(p[3],p[4],p[5]),(p[0],p[1],p[2])
	# check for verticals
	for i in range(3):
		if m[0][i]+m[1][i]+m[2][i] == 'xxx':return 'x'
		if m[0][i]+m[1][i]+m[2][i] == 'ooo':return 'o'
	# check for horizontals
	for i in range(3):
		if m[i] == ('x','x','x'):return 'x'
		if m[i] == ('o','o','o'):return 'o'
	#check \
	if m[0][0]+m[1][1]+m[2][2] == 'xxx':return 'x'
	if m[0][0]+m[1][1]+m[2][2] == 'ooo':return 'o'
	#check /
	if m[0][2]+m[1][1]+m[2][0] == 'xxx':return 'x'
	if m[0][2]+m[1][1]+m[2][0] == 'ooo':return 'o'
	return False

def togo(p):
	s = 0
	for n in '123456789':
		if n in p:s+=1
	return 'x' if s%2==1 else 'o'

def moves(p):
	return p.replace('x','').replace('o','')

def opp(p):
	return 'o' if togo(p)=='x' else 'x'

def ai(position):
	p = position.replace(' ','').lower()
	if p in ('123456789','1234x6789'):return 7
	#checking
	if won(p):return 'Invalid Position'
	#for all possible moves
	tg = togo(p)
	opponent = opp(p)
	m = moves(p)
	#can the ai immediately win?
	for move in m:
		if won(p.replace(move,tg)):return move
	#can the opponent win just after?
	for move in m:
		if won(p.replace(move,opponent)):return move
	#can the ai win in two?
	for move in m:
		p2 = p.replace(move,tg)
		for move2 in moves(p2):
			if won(p2.replace(move2,tg)):return move
	# failsafe
	# center
	if '5' in p:return 5
	# corners
	if '7' in p:return 7
	if '9' in p:return 9
	if '1' in p:return 1
	if '3' in p:return 3
	# edges
	if '8' in p:return 8
	if '4' in p:return 4
	if '2' in p:return 2
	if '6' in p:return 6