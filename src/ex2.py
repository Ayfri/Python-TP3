import random
import sys

from utils.inputs import int_input

__title__ = "Jeu des allumettes"

from utils.prints import Color, print_result

def ex2() -> None:
	"""
	La règle : il y a plusieurs allumettes (autant qu'on le veut) et on en retire 1,2 ou 3 et celui qui prend la dernière a perdu.
	Vous jouez contre l’ordinateur.
	Le joueur de départ est choisi aléatoirement.
	:return: None
	:rtype: None
	"""
	player: bool = random.randint(0, 1) == 0
	player_name: str = input("Entrez votre nom : ")
	nbr_matches: int = int_input("Combien d'allumettes voulez-vous ? ", 0)
	max_matches: int = nbr_matches
	print(f"{Color.yellow(player_name if not player else '''L'ordinateur''')} commence")

	while nbr_matches > 0:
		player = not player
		sys.stdout.write(f"{'|' * nbr_matches:>{max_matches}} {Color.yellow(player_name if player else '''L'ordinateur''')} enlève : ")

		if player:
			nbr_matches -= int_input('', 1, lambda _: nbr_matches if nbr_matches < 3 else 3)
			continue

		else:
			nbr_matches_computer: int = random.randint(1, nbr_matches if nbr_matches < 3 else 3)
			print(nbr_matches_computer)
			nbr_matches -= nbr_matches_computer
			continue

	if not player:
		print_result(f"{player_name} a gagné :D \nL'ordinateur a perdu :[")
	else:
		print_result(f"{player_name} a perdu :'( \nL'ordinateur a gagné :]")

if __name__ == "__main__":
	ex2()