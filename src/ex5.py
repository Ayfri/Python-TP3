from typing import Dict, List

from src.ex4 import Personne

__title__ =  "Classe Etudiant"

class Etudiant(Personne):
	"""
	Une classe qui hérite de Person et qui représente un étudiant.
	"""
	notes: dict[str, list[float]]

	def __init__(self, address: str, first_name: str, last_name: str, phone: str, notes: dict[str, list[float]]):
		"""
		Constructeur de la classe Student.
		:param address: l'adresse de l'étudiant
		:type address: str
		:param first_name: le prénom de l'étudiant.
		:type first_name: str
		:param last_name: le nom de l'étudiant
		:type last_name: str
		:param phone: le numéro de téléphone de l'étudiant
		:type phone: str
		:param notes: les notes de l'étudiant
		:type notes: str
		"""
		super().__init__(address, first_name, last_name, phone)
		self.notes = notes

	def __str__(self) -> str:
		"""
		Méthode qui permet d'afficher un étudiant.
		:return: une chaîne de caractères représentant l'étudiant
		:rtype: str
		"""
		return f'{super().__str__()} \nÉtudiant : {str(self.notes)}'

	def get_notes(self, course: str) -> list[float]:
		"""
		Retourne les notes d'un étudiant pour une matière donnée.
		:param course: la matière dont on veut les notes
		:type course: str
		:return: les notes de l'étudiant pour la matière donnée
		:rtype: list[float]
		"""
		if course in self.notes:
			return self.notes[course]
		else:
			return []


def test_student_notes() -> None:
	"""
	Teste la méthode get_notes de la classe Student.
	:return: None
	:rtype: None
	"""
	notes: dict[str, list[int]] = {
		'Math': [20, 18, 17.5, 18.75, 19.5],
		'Anglais': [15.5, 13.25, 14.5],
		'Histoire': [17.5, 15, 14.25, 15.5, 16.5],
		'Français': [18, 16, 15.5]
	}
	student: Etudiant = Etudiant('123 Fake St', 'John', 'Doe', '123-456-7890', notes)
	print(student)
	print(f'{student.get_notes("Math") = }')
	print(student.get_notes(input("Entrez une matière : ")))

def ex5() -> None:
	"""
	Écrire une classe Étudiant qui hérite de la classe Personne

	La classe Étudiant contient en plus :
	- Les notes de l’étudiant par matière et la méthode permettant d’accéder aux notes par matière.

	Faire un script qui teste toutes les méthodes que vous avez écrites.
	:return:
	:rtype:
	"""
	test_student_notes()

if __name__ == '__main__':
	ex5()