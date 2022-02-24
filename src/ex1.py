from utils.inputs import int_input

def ex1() -> None:
	"""
	Faire un programme qui calcule une suite de Syracuse.
	:return: None
	:rtype: None
	"""
	i: int = int_input()
	n: int = 0
	while i != 1:
		n += 1
		if i % 2 == 0:
			i //= 2
		else:
			i: int = 3 * i + 1
	print(n)

if __name__ == '__main__':
	ex1()