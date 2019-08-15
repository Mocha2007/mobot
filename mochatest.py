from random import choice, randint
from typing import Tuple
from mochaxyz import grammarq


def wilson(u: float, d: float) -> float:
	z = 1.95 # 95% confidence
	n = u+d
	a = (u+z**2/2)/(n+z**2)
	b = z/(n+z**2)*(u*d/n+z**2/4)**.5
	return a-b


def rpair() -> Tuple[int, int]:
	return randint(0, 12), randint(0, 12)


def rgrammar() -> Tuple[str, str]:
	return choice(grammarq)
