def plural(n: int, s: str) -> str:
	"""
	Renvoie le pluriel d'une chaîne suivant si le nombre est supérieur à 1 ou non.
	:param n: Nombre à tester.
	:type n: int
	:param s: Chaîne.
	:type s: str
	:return: Chaîne au pluriel ou normale.
	:rtype: str
	"""
	return s if n == 1 else s + 's'