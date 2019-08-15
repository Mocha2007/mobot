import pygame, time
from random import random
from typing import List

spritesize = 4
rows = 48
columns = 96
size = columns*spritesize, rows*spritesize
# default generator variables
seedchance = 1/512 # generate continent seeds
conversion = .1 # if an adjacent tile is a plain, then 20% chance of conversion per adjacent plains
landfrac = .3 # check if 30% full off land
mountainschance = .1 # change plains to mountains 10% of the time if all 4 adjacent are not sea

plains = pygame.image.load("img/grass.png")
mountains = pygame.image.load("img/stone.png")
sea = pygame.image.load("img/sea.png")


def random_world(sc: float, conv: float, lf: float, mc: float) -> List[list]: # List[List[pygame.image]]
	s = time.time()
	w = []

	plainscount = 0
	for i in range(rows):
		row = []
		for j in range(columns):
			t = sea
			if random() < sc:
				t = plains
				plainscount += 1
			row.append(t)
		w.append(row)

	while plainscount < lf*rows*columns:
		ow = [x[:] for x in w]
		for i in range(rows):
			for j in range(columns):
				if w[i][j] != plains:
					try:
						neighbors = [ow[i][(j+1) % columns], ow[i][(j-1) % columns], ow[i+1][j], ow[i-1][j]].count(plains)
					except IndexError:
						neighbors = [ow[i][(j+1) % columns], ow[i][(j-1) % columns], ow[i-1][j]].count(plains)
					if random() < conv*neighbors:
						w[i][j] = plains
						plainscount += 1
		if time.time() > s + 5:
			return w # too long

	for i in range(rows):
		for j in range(columns):
			try:
				neighbors = [w[i][(j+1) % columns], w[i][(j-1) % columns], w[i+1][j], w[i-1][j]].count(sea)
			except IndexError:
				neighbors = [w[i][(j+1) % columns], w[i][(j-1) % columns], w[i-1][j]].count(sea)
			if w[i][j] == plains and neighbors == 0 and random() < mc:
				w[i][j] = mountains

	return w


def wg(string: str) -> None:
	arg = string.split(' ')
	read_errors = IndexError, ValueError
	try:
		v1 = float(arg[0])
		if not (0 < v1 <= 1):
			raise ValueError('v1 must be in the interval (0,1]')
	except read_errors:
		v1 = seedchance
	try:
		v2 = float(arg[1])
		if not (0 < v2 <= 1):
			raise ValueError('v2 must be in the interval (0,1]')
	except read_errors:
		v2 = conversion
	try:
		v3 = float(arg[2])
		if not (0 <= v3 <= 1):
			raise ValueError('v3 must be in the interval [0,1]')
	except read_errors:
		v3 = conversion
	try:
		v4 = float(arg[3])
		if not (0 <= v4 <= 1):
			raise ValueError('v4 must be in the interval [0,1]')
	except read_errors:
		v4 = mountainschance

	pygame.init()
	pygame.display.iconify()
	screen = pygame.display.set_mode(size)

	terrain = random_world(v1, v2, v3, v4)
	# Drawing the bg
	for i in range(rows):
		for j in range(columns):
			screen.blit(terrain[i][j], (j*spritesize, i*spritesize))
	# snip
	pygame.display.flip()
	pygame.image.save(screen, 'img/temp.png')
	pygame.quit()
