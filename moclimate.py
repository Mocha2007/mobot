import pygame,random,time

spritesize = 4
rows = 48
columns = 96
size = columns*spritesize,rows*spritesize

plains = pygame.image.load("img/grass.png")
mountains = pygame.image.load("img/stone.png")
sea = pygame.image.load("img/sea.png")

#generator variables
seedchance = 1/512#generate continent seeds
conversion = .2#if an adjacent tile is a plain, then 20% chance of conversion per adjacent plains
landfrac = .3#check if 30% full off land
mountainschance = .1#change plains to mountains 10% of the time if all 4 adjacent are not sea
	
def random_world(sc,conv,lf,mc):
	s = time.time()
	w=[]

	plainscount=0
	for i in range(rows):
		row=[]
		for j in range(columns):
			t = sea
			if random.random()<sc:
				t = plains
				plainscount+=1
			row+=[t]
		w+=[row]

	while plainscount < lf*rows*columns:
		for i in range(rows):
			for j in range(columns):
				try:
					if w[i][j] != plains:
						neighbors = [w[i][(j+1)%columns],w[i][(j-1)%columns],w[i+1][j],w[i-1][j]].count(plains)
						if random.random()<conv*neighbors:
							w[i][j]=plains
							plainscount+=1
				except IndexError:pass
		if time.time() > s + 5:return w # too long

	for i in range(rows):
		for j in range(columns):
			try:
				if w[i][j]==plains and [w[i][(j+1)%columns],w[i][(j-1)%columns],w[i+1][j],w[i-1][j]].count(sea)==0 and random.random()<mc:
					w[i][j]=mountains
			except IndexError:pass

	return w

def wg(string):
	arg = string.split(' ')
	try:
		v1 = float(arg[0])
		if not (0<v1<=1):raise ValueError('v1 must be in the interval (0,1]')
		v2 = float(arg[1])
		if not (0<v2<=1):raise ValueError('v2 must be in the interval (0,1]')
		v3 = float(arg[2])
		if not (0<=v3<=1):raise ValueError('v3 must be in the interval [0,1]')
		v4 = float(arg[3])
		if not (0<=v4<=1):raise ValueError('v4 must be in the interval [0,1]')
	except:
		v1 = seedchance
		v2 = conversion
		v3 = landfrac
		v4 = mountainschance
			
	pygame.init()
	screen = pygame.display.set_mode(size)

	terrain=random_world(v1,v2,v3,v4)
	#Drawing the bg
	for i in range(rows):
		for j in range(columns):
			screen.blit(terrain[i][j],(j*spritesize,i*spritesize))
	#snip
	pygame.display.flip()
	pygame.image.save(screen,'img/temp.png')
	pygame.quit()