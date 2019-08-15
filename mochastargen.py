from math import pi
from random import random, uniform


def stargen(x: str) -> str:
	outputstring = '```'
	outputstring2 = []
	outputstring3 = ''
	# BEGIN STAR GEN
	if x == 'r':
		if random() < .7645: # M
			starmass = uniform(.08, .45) # b/w .08 and .45
		elif random() < .5138: # K
			starmass = uniform(.45, .8) # b/w .45 and .8
		elif random() < .6638: # G
			starmass = uniform(.8, 1.04) # b/w .8 and 1.04
		elif random() < .7792: # F
			starmass = uniform(1.04, 1.4) # b/w 1.04 and 1.4
		elif random() < .7059: # A
			starmass = uniform(1.4, 2.1) # b/w 1.4 and 2.1
		elif random() < .52: # B
			starmass = uniform(2.1, 16) # b/w 2.1 and 16
		else: # O
			starmass = uniform(16, 100) # b/w 16 and 100 (Above 42 generates no habitables)
	else:
		starmass = float(x)
	starluminosity = starmass**3.5
	# Artifexian says 4 but Stefan-Boltzmann Law dictates 3.5 based on the other shit he's said.
	starradius = starmass**.74
	startemperature = 5772*starmass**.505
	starlife = 12000000000*starmass**-2.5 # Artifexian says 10 billion, newest sources say 12 billion
	# innerhabitable = .95*starluminosity**.5
	# outerhabitable = 1.37*starluminosity**.5
	frost = 4.85*starluminosity**.5
	innerlimit = .1*starmass
	outerlimit = 40*starmass
	outputstring += "\nSTAR:\n MASS "+str(starmass)+" suns\n RADIUS "+str(starradius)+" suns\n TEMPERATURE " + \
		("{:,}".format(round(startemperature)))+" K\n LUMINOSITY "+str(starluminosity)+" suns\n LIFESPAN " + \
		("{:,}".format(round(starlife))) + \
		" years\nPLANETARY SEMIMAJOR AXES, ORBITAL PERIODS, MEAN ORBITAL VELOCITIES, AND MEAN SURFACE TEMPERATURES:"
	# Min habitable zone=.95*luminosity**.5,Max habitable zone=1.37*luminosity**.5, Frost Point
	# print(innerhabitable,outerhabitable,frost)#au
	# Inner and outer limits of the system
	# print(innerlimit,outerlimit)#au
	# PLANETS~~~~~~~~~~~~~~~~~~~~~~~~~
	# FIRST GAS GIANT GEN
	gg1sma = frost+random()*.2+1
	if gg1sma < outerlimit: # can't be outside the system - can happen if starmass>~16.5
		# gas giants have an average albedo closer to .5
		outputstring3 += "\n Gas Giant 1\n\t"+str(gg1sma)+" au\n\t"+str((gg1sma**3/starmass)**.5)+" years\n\t" + \
						str(498659569/52594920*pi*(starmass/gg1sma)**.5)+" km/s\n\t" + \
						str(round(startemperature*(1-.5)**.25*(2319000/498659569*starradius/2/gg1sma)**.5))+" K"
	# More gas giants
	ggosma = gg1sma
	ggn = 1
	while ggosma*2 < outerlimit:
		ggn += 1
		ggosma = ggosma*(random()*.6+1.4)
		outputstring3 += "\n Gas Giant "+str(ggn)+"\n\t"+str(ggosma)+" au\n\t"+str((ggosma**3/starmass)**.5) + \
						" years\n\t"+str(498659569/52594920*pi*(starmass/ggosma)**.5)+" km/s\n\t" + \
						str(round(startemperature*(1-.5)**.25*(2319000/498659569*starradius/2/ggosma)**.5))+" K"
	# Inner worlds!
	rocky = gg1sma
	lastrocky = gg1sma+1
	while innerlimit < rocky/2:
		rocky = rocky/(random()*.6+1.4)
		if 273 < startemperature*(1-.3)**.25*(2319000/498659569*starradius/2/rocky)**.5 < 373 and lastrocky-rocky > .15 and \
			rocky < outerlimit: # can't be outside the system, habitable calc used to be innerhabitable<rocky<outerhabitable
			if 1 < (rocky**3/starmass)**.5: # use years as unit
				outputstring2 += ["\n Habitable\n\t"+str(rocky)+" au\n\t"+str((rocky**3/starmass)**.5)+" years\n\t" +
								str(498659569/52594920*pi*(starmass/rocky)**.5)+" km/s\n\t" +
								str(round(startemperature*(1-.35)**.25*(2319000/498659569*starradius/2/rocky)**.5)) +
								" K"] # assuming albedo of .3 since like earth yo. i need the weird frac cuz i need to convert solar radii to au
			else: # days
				outputstring2 += ["\n Habitable\n\t"+str(rocky)+" au\n\t"+str(365.2425*(rocky**3/starmass)**.5) +
								" days\n\t"+str(498659569/52594920*pi*(starmass/rocky)**.5)+" km/s\n\t" +
								str(round(startemperature*(1-.35)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]
		elif .15 < lastrocky-rocky and rocky < outerlimit: # can't be within .15 au or outside the system
			if 1 < (rocky**3/starmass)**.5: # use years as unit
				outputstring2 += ["\n Rocky\n\t"+str(rocky)+" au\n\t"+str((rocky**3/starmass)**.5)+" years\n\t" +
							str(498659569/52594920*pi*(starmass/rocky)**.5)+" km/s\n\t" +
							str(round(startemperature*(1-.2)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"] # assuming albedo of .2
			else:
				outputstring2 += ["\n Rocky\n\t"+str(rocky)+" au\n\t"+str(365.2425*(rocky**3/starmass)**.5) +
								" days\n\t"+str(498659569/52594920*pi*(starmass/rocky)**.5)+" km/s\n\t" +
								str(round(startemperature*(1-.2)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]
		lastrocky = rocky
	return outputstring+''.join(outputstring2[::-1])+outputstring3+'\n```'
