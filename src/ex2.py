import random

from utils.inputs import int_input

def ext2() -> None:
	"""
	La règle : il y a plusieurs allumettes (autant qu'on le veut) et on en retire
1,2 ou 3 et celui qui prend la dernière a perdu.
Vous jouez contre l’ordinateur
Le joueur de départ est choisi aléatoirement
	:return: None
	:rtype: None
	"""
	player: bool = random.randint(0, 1) == 0
	playerName: str = input("Entrez votre nom : ")
	nbr_matches: int = int_input("Combien d'allumettes voulez-vous ? ", 0)
	max_matches: int = nbr_matches

	while nbr_matches > 0:
		player = not player
		if player:
			nbr_matches -= int_input(f"{'|' * nbr_matches:>{max_matches}} {playerName} enlève : ", 1, lambda _: nbr_matches if nbr_matches < 3 else 3)
			continue

		else:
			nbr_matches_computer: int = random.randint(1, nbr_matches if nbr_matches < 3 else 3)
			print(f"{'|' * nbr_matches:>{max_matches}} L'ordinateur enlève : {nbr_matches_computer}")
			nbr_matches -= nbr_matches_computer
			continue

	if not player:
		print(f"{playerName} a gagné >:D \nL'ordinateur a perdu :[")
	else:
		print(f"{playerName} a perdu :'( \nL'ordinateur a gagné :]")

if __name__ == "__main__":
	ext2()