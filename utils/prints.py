import sys

class Color:
	RED: str = '\033[91m'
	GREEN: str = '\033[92m'
	YELLOW: str = '\033[93m'
	BLUE: str = '\033[94m'
	PURPLE: str = '\033[95m'
	CYAN: str = '\033[96m'
	END: str = '\033[0m'

	@staticmethod
	def red(text: any) -> str:
		"""
		Renvoie le texte en rouge.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.RED + str(text) + Color.END

	@staticmethod
	def green(text: any) -> str:
		"""
		Renvoie le texte en vert.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.GREEN + str(text) + Color.END

	@staticmethod
	def yellow(text: any) -> str:
		"""
		Renvoie le texte en jaune.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.YELLOW + str(text) + Color.END

	@staticmethod
	def blue(text: any) -> str:
		"""
		Renvoie le texte en bleu.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.BLUE + str(text) + Color.END

	@staticmethod
	def purple(text: any) -> str:
		"""
		Renvoie le texte en violet.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.PURPLE + str(text) + Color.END

	@staticmethod
	def cyan(text: any) -> str:
		"""
		Renvoie le texte en cyan.
		:param text: Texte à colorier
		:type text: any
		:return: Texte coloré
		:rtype: str
		"""
		return Color.CYAN + str(text) + Color.END

def print_line(text = '', length = 40, color: str | None = None) -> None:
	"""
	Écrit dans la console une ligne de texte de longueur length avec un texte au milieu si nécessaire.

	:param text: Le texte au milieu à afficher si nécessaire.
	:type text: any
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
	print(color + str(result) + Color.END)