from utils.inputs import int_input

__title__ = "Suite de Syracuse"

def ex1() -> None:
	"""
	Faire un programme qui calcule une suite de Syracuse.
	L'afficher sous forme de tableau dans la console.

	Exemple :
		Entrée : 5
		Sortie :
			╔═══╦═════╗
			║ 0 ║   5 ║
			╠═══╬═════╣
			║ 1 ║  16 ║
			╠═══╬═════╣
			║ 2 ║   8 ║
			╠═══╬═════╣
			║ 3 ║   4 ║
			╠═══╬═════╣
			║ 4 ║   2 ║
			╠═══╬═════╣
			║ 5 ║   1 ║
			╚═══╩═════╝

	:return: None
	:rtype: None
	"""
	i: int = int_input()
	n: int = 0
	ascii_index_length, ascii_nbr_length = calculate_longest_nbr(i)
	ascii_index: str = '═' * (ascii_index_length + 2)
	ascii_nbr: str = '═' * (ascii_nbr_length + 2)
	print(f"╔{ascii_index}╦{ascii_nbr}╗")
	while i != 1:
		print(f"║ {n:>{ascii_index_length}} ║ {i:>{ascii_nbr_length}} ║")
		if i % 2 == 0:
			i //= 2
		else:
			i = 3 * i + 1
		n += 1
		if i != 1:
			print(f"╠{ascii_index}╬{ascii_nbr}╣")
	print(f"╚{ascii_index}╩{ascii_nbr}╝")

def calculate_longest_nbr(n: int) -> (int, int):
	"""
	Calcule le nombre le plus long de la suite de Syracuse actuelle.
	:param n: Le nombre de départ pour la suite de Syracuse.
	:type n: int
	:return: L'index et le nombre le plus long de la suite de Syracuse via n.
	:rtype: (int, int)
	"""
	i: int = n
	longest_nbr: int = 0
	longest_nbr_index: int = 0
	while i != 1:
		if i % 2 == 0:
			i //= 2
		else:
			i = 3 * i + 1
		if i > longest_nbr:
			longest_nbr = i
			longest_nbr_index = n
		n += 1

	return len(str(longest_nbr_index)), len(str(longest_nbr))

if __name__ == '__main__':
	ex1()
