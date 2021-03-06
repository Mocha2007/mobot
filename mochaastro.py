from math import cos, inf, log, pi, sin

g = 6.67408e-11 # standard gravitational constant
c = 299792458 # m/s

pc = 3.0857e16
ly = 9.4607e15
au = 149597870700
a_moon = 3.84399e8
a_planck = 2.176470e-8

m_sun = 1.98855e30
m_j = 1.8986e27
m_e = 5.97237e24
m_moon = 7.342e22
m_person = 69

r_sun = 6.957e8
r_j = 6.9911e7
r_e = 6.371e6
r_moon = 1737100
r_person = .2544 # assuming a perfect sphere
r_planck = 1.616229e-35

t_e = 86164.100352
t_planck = 5.39116e-44

l_sun = 3.828e26 # Watts
l_planck = 3.62831e52 # Watts

lb = 0.45359237
mi = 1609.344
minute = 60
hour = 3600
day = 86400
year = 31556952
jyear = 31536000

mercury = {'a': 0.387098*au, 'e': 0.205630, 'r': 2439700, 'm': 3.3011e23}
venus = {'a': 0.723332*au, 'e': 0.006772, 'r': 6051800, 'm': 4.8675e24}
earth = {'a': au, 'e': 0.0167086, 'r': r_e, 'm': m_e}
mars = {'a': 1.523679*au, 'e': 0.0934, 'r': 3389500, 'm': 6.4171e23}
jupiter = {'a': 5.2026*au, 'e': 0.048498, 'r': r_j, 'm': m_j}
saturn = {'a': 9.5549*au, 'e': 0.05555, 'r': 58232000, 'm': 5.6836e26}
uranus = {'a': 19.2184*au, 'e': 0.046381, 'r': 25362000, 'm': 8.681e25}
neptune = {'a': 30.110387*au, 'e': 0.009456, 'r': 24622000, 'm': 1.0243e26}
planetnine = {'a': 700*au, 'e': 0.6, 'r': 20000000, 'm': 6e25}
# hohmann(362600000,405400000,5.97237e24)


def hohmann(inner: float, outer: float, m: float) -> float:
	mu = m*g
	dv1 = (mu/inner)**.5*((2*outer/(inner+outer))**.5-1)
	dv2 = (mu/inner)**.5*(1-(2*inner/(inner+outer))**.5)
	return dv1+dv2


# bielliptic(362600000,405400000,4054000000,5.97237e24)
def bielliptic(inner: float, outer: float, mid: float, m: float) -> float:
	mu = m*g
	a1 = (inner+mid)/2
	a2 = (outer+mid)/2
	dv1 = (2*mu/inner-mu/a1)**.5-(mu/inner)**.5
	dv2 = (2*mu/mid-mu/a2)**.5-(2*mu/mid-mu/a1)**.5
	dv3 = (2*mu/outer-mu/a2)**.5-(mu/outer)**.5
	return dv1+dv2+dv3


# biellipticinf(362600000,405400000,5.97237e24)
def biellipticinf(inner: float, outer: float, m: float) -> float:
	mu = m*g
	return (mu/inner)**.5*(2**.5-1)*(1+(inner/outer)**.5)


# bielliptictime(362600000,405400000,4054000000,5.97237e24)
def bielliptictime(inner: float, outer: float, mid: float, m: float) -> float:
	mu = m*g
	a1 = (inner+mid)/2
	a2 = (outer+mid)/2
	t1 = pi*(a1**3/mu)**.5
	t2 = pi*(a2**3/mu)**.5
	return t1+t2


def optimal(inner: float, outer: float, m: float) -> str:
	if biellipticinf(inner, outer, m) > hohmann(inner, outer, m):
		return "Bi-Elliptic"
	return "Hohmann"


def inclinationburn(deltai: float, ecc: float, aop: float, trueanomaly: float, meanmotion: float, sma: float) -> float:
	return 2*sin(deltai/2)*(1-ecc**2)**.5*cos(aop+trueanomaly)*meanmotion*sma/(1+ecc*cos(trueanomaly))


def p(m: float, sma: float) -> float: # period
	mu = g*m
	return 2*pi*(sma**3/mu)**.5


# mov(1.98855e30,149598023000)
def mov(m: float, sma: float) -> float: # mean orbital velocity
	mu = g*m
	return (sma/mu)**-.5


def apsides(a: float, e: float) -> (float, float):
	return (1-e)*a, (1+e)*a


def vextrema(a: float, e: float, m: float) -> (float, float):
	if e == 0:
		return mov(m, a)
	mu = g*m
	v_peri = ((1+e)*mu/(1-e)/a)**.5
	v_apo = ((1-e)*mu/(1+e)/a)**.5
	return v_peri, v_apo


def apsides2ecc(apo: float, peri: float) -> (float, float):
	return (apo+peri)/2, (apo-peri)/(apo+peri)


def density(m: float, r: float) -> float:
	return m/(4/3*pi*r**3)


def synchronous(t: float, m: float) -> float:
	mu = g*m
	return (mu*t**2/4/pi**2)**(1/3)


def soi(m: float, M: float, a: float) -> float:
	return a*(m/M)**.4


def speed(a: float, r: float, m: float) -> float:
	mu = g*m
	return (mu*(2/r-1/a))**.5


# based on dv/dr(speed)
def acc(a: float, r: float, m: float) -> float:
	mu = g*m
	return mu/(a**2*(mu*(2/r-1/a))**.5)


def surfacegravity(m: float, r: float) -> float:
	return g*m/r**2


def vescape(m: float, r: float) -> float:
	return (2*g*m/r)**.5


def vtan(t: float, r: float): # Equatorial rotation velocity
	return 2*pi*r/t


def synodic(p1: float, p2: float) -> float: # synodic period
	if p2-p1:
		return p1*p2/(p2-p1)
	return inf


def star(star_mass: float) -> (float, float, float, float):
	"""Mass (kg)\n-> Radius (m), Luminosity (W), Temp (K), Lifespan (s)"""
	m = star_mass/m_sun
	# default exponents: .74,3,.505,-2.5
	# I find 0.96 a better approximation than 0.74, at least for smaller stars.
	# I find 0.54 a very slightly better approximation than 0.505, at least for smaller stars.
	# Luminosity and time values from https://www.academia.edu/4301816/On_Stellar_Lifetime_Based_on_Stellar_Mass
	# L
	if m > .45:
		lum = 1.148*m**3.4751
	else:
		lum = .2264*m**2.52
	return r_sun*m**0.96, l_sun*lum, 5772*m**.54, 3.97310184e17*m**-2.5162


def habitablezone(m: float) -> (float, float):
	return au*.95*(star(m)[1]/l_sun)**.5, au*1.37*(star(m)[1]/l_sun)**.5


def temp(T: float, R: float, sma: float, a: float) -> float:
	"""Temperature of the star (K),
	Radius of the star (m),
	Semi-major axis (m),
	Albedo\n->
	Temperature of the body (K)\n
	Formula from https://en.wikipedia.org/wiki/Planetary_equilibrium_temperature#Theoretical_model"""
	return T*(1-a)**.25*(R/2/sma)**.5


def absmag(appmag: float, distance: float) -> float:
	return appmag-5*(log(distance/pc)-1)


def peakwavelength(T: float) -> float:
	return 2.8977729e-3/T


def roche(m: float, rho: float) -> float:
	"""m = primary mass, rho = secondary density"""
	return (9*m/4/pi/rho)**(1/3)


def hill(m: float, M: float, a: float, e: float) -> float:
	return a*(1-e)*(m/3/M)**(1/3)


# NEW!
def gravbinding(m: float, r: float) -> float:
	"""gravitational binding energy (in joules)"""
	return 3*g*m**2/5/r


def gravbinding2(r: float, rho: float) -> float:
	"""gravitational binding energy (in joules), using density for mass"""
	return g*pi**2*16*rho**2*r**5/15


def schwarzschild(m: float) -> float:
	"""Schwarzschild radius"""
	return 2*g*m/c**2


def energy(m: float) -> float:
	"""rest energy"""
	return m*c**2


def mass(e: float) -> float:
	"""relativistic mass"""
	return e/c**2


def orbitenergy(m: float, a: float):
	"""Specific orbital energy"""
	return -m*g/2/a


# source for the formula: http://phl.upr.edu/projects/earth-similarity-index-esi
# esi(mars['r'],mars['m'],210)
def esi(r: float, m: float, T: float) -> float: # Radius,Density,Escape Velocity,Temperature
	esi1 = 1-abs((r-r_e)/(r+r_e))
	esi2 = 1-abs((density(m, r)-density(m_e, r_e))/(density(m, r)+density(m_e, r_e)))
	esi3 = 1-abs((vescape(m, r)-vescape(m_e, r_e))/(vescape(m, r)+vescape(m_e, r_e)))
	esi4 = 1-abs((T-255)/(T+255))
	return esi1**(.57/4)*esi2**(1.07/4)*esi3**(.7/4)*esi4**(5.58/4)


def drake(R: float, fp: float, ne: float, fl: float, fi: float, fc: float, L: float) -> float:
	"""Use -1 for defaults"""
	if R == -1:
		R = 2.25
	if fp == -1:
		fp = 1
	if ne == -1:
		ne = .4
	if fl == -1:
		fl = .5
	if fi == -1:
		fi = 1
	if fc == -1:
		fc = 1
	if L == -1:
		L = 200
	return R*fp*ne*fl*fi*fc*L


def itemp(T: float, R: float, a: float, Tp: float) -> float:
	"""Temperature of the star (K),
	Radius of the star (m),
	Albedo,
	Temperature of the body (K)\n->
	Semi-major axis (m)\n
	Formula inverted from https://en.wikipedia.org/wiki/Planetary_equilibrium_temperature#Theoretical_model"""
	return R*T**2*(1-a)**.5/2/Tp**2


# ADD DOCS FOR THESE TWO
def lz(eee: float, i_1: float, i_2: float) -> float: # https://en.wikipedia.org/wiki/Kozai_mechanism
	iii = i_1-i_2
	return (1-eee**2)**.5*cos(iii)


def tkozai(m_1: float, m_2: float, p_1: float, p_2: float, e_2: float) -> float:
	"""kg,kg,s,s,[dimensionless]->s\n
	Variables with subscript "2" refer to the outer (perturber) orbit and variables with subscript
	"1" refer to the inner (satellite) orbit."""
	return m_1/m_2*p_2**2/p_1*(1-e_2**2)**1.5
