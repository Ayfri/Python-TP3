import random
from typing import List, Set

from utils.inputs import int_input
from utils.strutils import plural

def ex3() -> None:
	"""
	Make a program that simulates the throwing of 3 dice in order to obtain in 3 throws max: 4 2 1- At each throw you can keep 1, 2 or 3 dice and as soon as you have 3 dice with 1,2,4 the game is over
	Example:
	How many games do you want to play: 3
	Roll 1 with 3 dice: 5 2 1 I keep 2 and 1 [ 2,1]
	Roll 2 with 1 dice: 3 I keep nothing [ 2.1]
	Roll 3 with 1 dice: 4 I keep 4 [ 4,2,1]
	Game 1 won in 3 moves

	:return: None
	:rtype: None
	"""
	games = int_input("How many games do you want to play: ")
	wins: int = 0

	for i in range(games):
		dices: List[int] = []
		kept_dices: Set[int] = set()
		moves: int = 0
		for moves in range(3):
			dices = [random.randint(1, 6) for i in range(1, 4 - len(kept_dices))]
			new_kept_dices = {dice for dice in dices if dice in [1, 2, 4]}
			kept_dices = {dice for dice in kept_dices if dice in [1, 2, 4]}.union(new_kept_dices)
			print(f"Lancé {moves + 1} avec {len(dices)} {plural(len(dices), 'dé'):<3} : {' '.join(map(str, dices)):<6} je garde {len(new_kept_dices)} {plural(len(new_kept_dices), 'dé')} {list(kept_dices)}")

			if len(kept_dices) == 3:
				break
		if len(kept_dices) == 3:
			wins += 1
			print(f"Partie {i + 1} gagnée en {moves + 1} {plural(moves + 1, 'mouvement')}")
		else:
			print(f"Partie {i + 1} perdu")

	print(f"Vous avez joué {games} parties, {wins} gagnées pour {games - wins} perdues soit {round(wins / games * 100, 2)}% de gain")

if __name__ == "__main__":
	ex3()