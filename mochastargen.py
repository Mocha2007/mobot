import random,math
def stargen(x):
	outputstring = '```'
	outputstring2 = []
	outputstring3 = ''
	#BEGIN STAR GEN
	if x=='r':
		if random.random()<.7645:
			#M
			starmass=random.random()*.37+.08 #b/w .08 and .45
		elif random.random()<.5138:
			#K
			starmass=random.random()*.35+.45 #b/w .45 and .8
		elif random.random()<.6638:
			#G
			starmass=random.random()*.24+.8 #b/w .8 and 1.04
		elif random.random()<.7792:
			#F
			starmass=random.random()*.36+1.04 #b/w 1.04 and 1.4
		elif random.random()<.7059:
			#A
			starmass=random.random()*.7+1.4 #b/w 1.4 and 2.1
		elif random.random()<.52:
			#B
			starmass=random.random()*13.9+2.1 #b/w 2.1 and 16
		else:
			#O
			starmass=random.random()*58+16 #b/w 16 and 100 (Above 42 generates no habitables)
	else:starmass = float(x)
	starluminosity=starmass**3.5#Artifexian says 4 but Stefan-Boltzmann Law dictates 3.5 based on the other shit he's said.
	starradius=starmass**.74
	startemperature=5772*starmass**.505
	starlife=12000000000*starmass**-2.5#Artifexian says 10 billion, newest sources say 12 billion
	innerhabitable=.95*starluminosity**.5
	outerhabitable=1.37*starluminosity**.5
	frost=4.85*starluminosity**.5
	innerlimit=.1*starmass
	outerlimit=40*starmass
	outputstring+="\nSTAR:\n MASS "+str(starmass)+" suns\n RADIUS "+str(starradius)+" suns\n TEMPERATURE "+("{:,}".format(round(startemperature)))+" K\n LUMINOSITY "+str(starluminosity)+" suns\n LIFESPAN "+("{:,}".format(round(starlife)))+" years\nPLANETARY SEMIMAJOR AXES, ORBITAL PERIODS, MEAN ORBITAL VELOCITIES, AND MEAN SURFACE TEMPERATURES:"
	#Min habitable zone=.95*luminosity**.5,Max habitable zone=1.37*luminosity**.5, Frost Point
	#print(innerhabitable,outerhabitable,frost)#au
	#Inner and outer limits of the system
	#print(innerlimit,outerlimit)#au
	#PLANETS~~~~~~~~~~~~~~~~~~~~~~~~~
	#FIRST GAS GIANT GEN
	gg1sma=frost+random.random()*.2+1
	if gg1sma<outerlimit:#can't be outside the system - can happen if starmass>~16.5
		outputstring3+="\n Gas Giant 1 : "+str(gg1sma)+" au, "+str((gg1sma**3/starmass)**.5)+" years,\n              "+str(498659569/52594920*math.pi*(starmass/gg1sma)**.5)+" km/s, "+str(round(startemperature*(1-.5)**.25*(2319000/498659569*starradius/2/gg1sma)**.5))+" K"#gas giants have an average albedo closer to .5
	#More gas giants
	ggosma=gg1sma
	ggn=1
	while ggosma*2<outerlimit:
		ggn+=1
		ggosma=ggosma*(random.random()*.6+1.4)
		outputstring3+="\n Gas Giant "+str(ggn)+" : "+str(ggosma)+" au, "+str((ggosma**3/starmass)**.5)+" years,\n              "+str(498659569/52594920*math.pi*(starmass/ggosma)**.5)+" km/s, "+str(round(startemperature*(1-.5)**.25*(2319000/498659569*starradius/2/ggosma)**.5))+" K"
	#Inner worlds!
	rocky=gg1sma
	lastrocky=gg1sma+1
	while rocky/2>innerlimit:
		rocky=rocky/(random.random()*.6+1.4)
		if 273<startemperature*(1-.3)**.25*(2319000/498659569*starradius/2/rocky)**.5<373 and lastrocky-rocky>.15 and rocky<outerlimit:#can't be outside the system, habitable calc used to be innerhabitable<rocky<outerhabitable
			if (rocky**3/starmass)**.5>1: #use years as unit
				outputstring2+=["\n Habitable: "+str(rocky)+" au, "+str((rocky**3/starmass)**.5)+" years,\n           "+str(498659569/52594920*math.pi*(starmass/rocky)**.5)+" km/s, "+str(round(startemperature*(1-.35)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]#assuming albedo of .3 since like earth yo. i need the weird frac cuz i need to convert solar radii to au
			else: #days
				outputstring2+=["\n Habitable: "+str(rocky)+" au, "+str(365.2425*(rocky**3/starmass)**.5)+" days,\n           "+str(498659569/52594920*math.pi*(starmass/rocky)**.5)+" km/s, "+str(round(startemperature*(1-.35)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]
		elif lastrocky-rocky>.15 and rocky<outerlimit:#can't be within .15 au or outside the system
			if (rocky**3/starmass)**.5>1: #use years as unit
				outputstring2+=["\n Rocky: "+str(rocky)+" au, "+str((rocky**3/starmass)**.5)+" years,\n       "+str(498659569/52594920*math.pi*(starmass/rocky)**.5)+" km/s, "+str(round(startemperature*(1-.2)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]#assuming albedo of .2
			else:
				outputstring2+=["\n Rocky: "+str(rocky)+" au, "+str(365.2425*(rocky**3/starmass)**.5)+" days,\n       "+str(498659569/52594920*math.pi*(starmass/rocky)**.5)+" km/s, "+str(round(startemperature*(1-.2)**.25*(2319000/498659569*starradius/2/rocky)**.5))+" K"]
		lastrocky=rocky
	return outputstring+''.join(outputstring2[::-1])+outputstring3+'\n```'
	#rocky moon mass total = planet mass/random.randint(80,200)
	#gas moon mass total = planet mass/random.randint(4000,10000)
	#first moon = random.random()*that value
	#second moon = random.random()*remainder, etc
