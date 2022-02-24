import sys

class Color:
	RED: str = '\033[91m'
	GREEN: str = '\033[92m'
	YELLOW: str = '\033[93m'
	BLUE: str = '\033[94m'
	PURPLE: str = '\033[95m'
	CYAN: str = '\033[96m'
	END: str = '\033[0m'

def print_line(text = '', length = 40, color: str | None = None) -> None:
	"""
	Écrit dans la console une ligne de texte de longueur length avec un texte au milieu si nécessaire.

	:param text: Le texte au milieu à afficher si nécessaire.
	:type text: str
	:param length: La longueur de la ligne à afficher.
	:type length: int
	:param color: La couleur du texte à afficher.
	:type color: str | None
	:return: None
	:rtype: None
	"""
	if len(text) > 0:
		text = f" {text} "
	if color is not None:
		sys.stdout.write(color)
	print('-' * (length // 2) + text + '-' * (length // 2) + Color.END)

def print_result(result: any, color: str = Color.PURPLE) -> None:
	"""
	Écrit dans la console un résultat.
	:param result: Le résultat à écrire.
	:type result: any
	:param color: La couleur du texte à afficher.
	:type color: str
	:return: None
	:rtype: None
	"""
	print(f"{color}{result}{Color.END}")