import sys
from typing import Callable

def int_input(
		text: str = "Entrez un nombre : ",
		min_number: int = -sys.maxsize,
		max_number: Callable[[int], int] = lambda i: sys.maxsize,
		can_stop: bool = False
) -> int:
	"""
	Fonction permettant de demander à l'utilisateur d'entrer un entier dans un intervalle

	:param text: Texte affiché à l'utilisateur.
	:type text: str
	:param min_number: Entier minimum autorisé.
	:type min_number: int
	:param max_number: Entier maximum autorisé.
	:type max_number: Callable[[int], int]
	:param can_stop: Booléen indiquant si l'utilisateur peut arrêter l'exécution de l'input.
	:type can_stop: bool
	:returns Entier saisi par l'utilisateur.
	:type: int
	"""
	while True:
		try:
			inp: str = input(text)
			if can_stop and inp.lower() == "stop":
				raise KeyboardInterrupt
			i: int = int(inp)
			max_result = max_number(i)
		except ValueError:
			print("Veuillez saisir un entier valide.")
			continue
		if i < min_number or i > max_result:
			print(f"Veuillez saisir un entier dans l'intervalle [{min_number}, {max_result}].")
			continue
		return i

def float_input(
		text: str = "Veuillez saisir un nombre :"
) -> float:
	"""
	Fonction permettant de demander à l'utilisateur d'entrer un nombre à virgule flottante

	:param text: Texte affiché à l'utilisateur.
	:type text: str
	:returns Nombre à virgule flottante saisi par l'utilisateur.
	:type: float
	"""
	while True:
		try:
			f: float = float(input(text))
			if f > sys.maxsize:
				print(f"Veuillez saisir un nombre inférieur à {sys.maxsize}.")
				continue
			if f < -sys.maxsize:
				print(f"Veuillez saisir un nombre supérieur à {-sys.maxsize}.")
				continue
		except ValueError:
			print("Veuillez saisir un nombre à virgule flottante valide.")
			continue
		return f
