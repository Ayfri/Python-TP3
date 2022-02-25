__title__ = "Classe Personne"

class Personne:
	"""
	Une classe qui représente une personne
	"""
	address: str
	first_name: str
	last_name: str
	phone: str

	def __init__(self, address: str, first_name: str, last_name: str, phone: str):
		"""
		Constructeur de la classe Person
		:param address: l'adresse de la personne
		:type address: str
		:param first_name: le prénom de la personne
		:type first_name: str
		:param last_name: le nom de la personne
		:type last_name: str
		:param phone: le numéro de téléphone de la personne
		:type phone: str
		"""
		self.address: str = address
		self.first_name: str = first_name
		self.last_name: str = last_name
		self.phone: str = phone

	def __str__(self) -> str:
		"""
		Méthode qui permet d'afficher une personne
		:return: une chaîne de caractères représentant une personne
		:rtype: str
		"""
		return f"Personne : {self.first_name} {self.last_name} {self.address} {self.phone}"

	def set_address(self, address: str) -> None:
		"""
		Méthode qui permet de modifier l'adresse d'une personne
		:param address: la nouvelle adresse de la personne
		:type address: str
		:return: None
		:rtype: None
		"""
		self.address = address

	def set_first_name(self, first_name: str) -> None:
		"""
		Méthode qui permet de modifier le prénom d'une personne
		:param first_name: le nouveau prénom de la personne
		:type first_name: str
		:return: None
		:rtype: None
		"""
		self.first_name = first_name

	def set_last_name(self, last_name: str) -> None:
		"""
		Méthode qui permet de modifier le nom de la personne
		:param last_name: le nouveau nom de la personne
		:type last_name: str
		:return: None
		:rtype: None
		"""
		self.last_name = last_name

	def set_phone(self, phone: str) -> None:
		"""
		Méthode qui permet de modifier le numéro de téléphone d'une personne
		:param phone: le nouveau numéro de téléphone de la personne
		:type phone: str
		:return: None
		:rtype: None
		"""
		self.phone = phone

def test_address() -> None:
	"""
	Test de la méthode set_address
	:return: None
	:rtype: None
	"""
	person: Personne = Personne("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	print(f"{person.address = }")
	person.set_address(input("Entrez la nouvelle adresse: "))
	print(f"{person.address = }")

def test_first_name() -> None:
	"""
	Test de la méthode set_first_name
	:return: None
	:rtype: None
	"""
	person: Personne = Personne("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	print(f"{person.first_name = }")
	person.set_first_name(input("Entrez le nouveau prénom: "))
	print(f"{person.first_name = }")

def test_last_name() -> None:
	"""
	Test de la méthode set_last_name
	:return: None
	:rtype: None
	"""
	person: Personne = Personne("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	print(f"{person.last_name = }")
	person.set_last_name(input("Entrez le nouveau nom: "))
	print(f"{person.last_name = }")

def test_phone() -> None:
	"""
	Test de la méthode set_phone
	:return: None
	:rtype: None
	"""
	person: Personne = Personne("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	print(f"{person.phone = }")
	person.set_phone(input("Entrez le nouveau numéro de téléphone: "))
	print(f"{person.phone = }")

def ex4() -> None:
	"""
	Écrire une classe personne qui contient :
	• le nom,
	• le prénom,
	• l’adresse,
	• le numéro de téléphone,
	La classe contient les méthodes de
	• création ,
	• modification,
	• affichage de la personne,
	Faire un script qui teste toutes les méthodes que vous avez écrites.
	:return: None
	:rtype: None
	"""
	test_address()
	test_first_name()
	test_last_name()
	test_phone()

if __name__ == "__main__":
	ex4()