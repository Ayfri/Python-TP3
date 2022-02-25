import os
import sys
from typing import Callable

from utils.inputs import int_input
from utils.prints import Color, print_line, print_result

def get_exercices_count() -> int:
	"""
	Retourne le nombre d'exercices.
	:return: Le nombre d'exercices.
	:rtype: int
	"""

	# count the number of files with pattern "ex[number].py" in directory ../src
	return len([name for name in os.listdir('src') if name.startswith('ex') and name.endswith('.py')])

def get_exercice(number: int) -> tuple[str, str, Callable[[], None]]:
	"""
	Retourne le tuple contenant le nom, la consigne et la fonction à exécuter.
	:param number: Le numéro de l'exercice.
	:type number: int
	:return: Le tuple contenant le nom, la consigne et la fonction à exécuter.
	:rtype: tuple[str, str, Callable[[], None]]
	"""
	file: object = __import__(f"src.ex{number}")
	module: object = getattr(file, f"ex{number}")
	function: Callable[[], None] = getattr(module, f"ex{number}")
	return getattr(module, "__title__"), str(function.__doc__), function

def get_instructions_from_docstring(function: tuple[str, str, Callable[[], None]]) -> str:
	"""
	Retourne la consigne de l'exercice.
	:param function: L'exercice.
	:type function: tuple[str, str, Callable[[], None]]
	:return: La consigne de l'exercice depuis le docstring.
	:rtype: str
	"""
	return function[1].split(':return:')[0].strip().replace('\t', '')

def print_menu() -> None:
	"""
	Affiche le menu de sélection des exercices.
	:return: None
	:rtype: None
	"""
	print_line("Menu", color = Color.YELLOW)
	exercices: list[tuple[str, str, Callable[[], None]]] = [get_exercice(i) for i in range(1, get_exercices_count() + 1)]
	list_exercices: str = '\n'.join([f"Exercice {Color.cyan(i + 1)} - {Color.green(exercices[i][0])}" for i in range(len(exercices))])
	list_exercices += Color.red('\n\nSTOP pour arrêter.')
	print(list_exercices)

def menu() -> None:
	"""
	Lance le programme.
	:return: None
	:rtype: None
	"""
	print(Color.red('Bienvenue dans le menu du TP 3'))
	while True:
		print_menu()
		try:
			input1: int = int_input(Color.blue('Veuillez choisir un exercice : '), 1, lambda _: get_exercices_count(), True)
			exercice: tuple[str, str, Callable[[], None]] = get_exercice(input1)
			print(exercice)
			print_line(f"Exercice n°{input1}", color = Color.YELLOW)
			print_result(f"{get_instructions_from_docstring(exercice)}\n", Color.BLUE)
			exercice[2]()
			input(Color.cyan('Appuyez sur ENTRÉE pour continuer...'))
		except:
			print(Color.cyan('\nAu revoir :)'))
			sys.exit(1)

if __name__ == '__main__':
	menu()
