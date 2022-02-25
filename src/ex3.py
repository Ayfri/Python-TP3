import random
from typing import List, Set

from utils.inputs import int_input
from utils.strutils import plural

__title__ =  "421"

def ex3() -> None:
	"""
	Faire un programme qui simule le lancer de 3 dés afin d’obtenir en 3 lancers max : 4 2 1- A chaque coup on peut garder 1, 2 ou 3 dés et dès que l’on a 3 dés avec 1,2,4 le jeu est
	terminé
	Exemple :
			Combien de parties voulez vous jouer : 3
		Lancer 1 avec 3 dés : 5 2 1 je garde 2 et 1 [ 2,1]
		Lancer 2 avec 1 dé  : 3     je ne garde rien [ 2,1]
		Lancer 3 avec 1 dé  : 4     je garde 4 [ 4,2,1]
			Partie 1 gagnée en 3 coups
		Lancer 1 avec 3 dés : 2 2 1 je garde 2 et 1 [ 2,1]
		Lancer 2 avec 1 dé  : 4     je garde 4 [ 4,2,1]
			Partie 2 gagnée en 1 coup
		Lancer 1 avec 3 dés : 6 2 1 je garde 2 et 1 [ 2,1]
		Lancer 2 avec 1 dé  : 3     je ne garde rien [ 2,1]
		Lancer 3 avec 1 dé  : 6     je ne garde rien [ 2,1]
			Partie 3 Perdue
		Vous avez joué 3 parties, 2 gagnées pour 1 perdue soit 66,66% de gain

	:return: None
	:rtype: None
	"""
	games: int = int_input("Combien de parties voulez-vous jouer : ")
	wins: int = 0

	for i in range(games):
		dices: List[int] = []
		kept_dices: Set[int] = set()
		moves: int = 0
		for moves in range(3):
			dices = [random.randint(1, 6) for i in range(1, 4 - len(kept_dices))]
			new_kept_dices: Set[int] = {dice for dice in dices if dice in [1, 2, 4]}
			kept_dices = {dice for dice in kept_dices if dice in [1, 2, 4]}.union(new_kept_dices)

			kept: str = ' et '.join(map(str, new_kept_dices)) if len(new_kept_dices) > 0 else 'rien'
			print(f"Lancé {moves + 1} avec {len(dices)} {plural(len(dices), 'dé'):<3} : {' '.join(map(str, dices)):<6} je garde {kept} {list(kept_dices)}")

			if len(kept_dices) == 3:
				break
		if len(kept_dices) == 3:
			wins += 1
			print(f"Partie {i + 1} gagnée en {moves + 1} {plural(moves + 1, 'coup')}")
		else:
			print(f"Partie {i + 1} perdue")

	loses: int = games - wins
	percentage: float = round(wins / games * 100, 2)
	print(f"Vous avez joué {games} {plural(games, 'partie')}, {wins} {plural(wins, 'gagnée')} pour {loses} {plural(loses, 'perdue')} soit {percentage}% de gain")

if __name__ == "__main__":
	ex3()