from src.ex4 import Person

class Student(Person):
	notes: dict[str, list[float]]

	def __init__(self, address: str, first_name: str, last_name: str, phone: str, notes: dict[str, list[float]]):
		super().__init__(address, first_name, last_name, phone)
		self.notes = notes

	def get_notes(self, course: str) -> list[float]:
		if course in self.notes:
			return self.notes[course]
		else:
			return []

	def __str__(self) -> str:
		return super().__str__() + '\n' + str(self.notes)


def test_student_notes() -> None:
	notes = {
		'Math': [10, 9, 8],
		'English': [8, 7, 6],
		'History': [9, 9, 9]
	}
	student = Student('123 Fake St', 'John', 'Doe', '123-456-7890', notes)
	print(student)
	assert student.get_notes('Math') == [10, 9, 8]
	print(f'{student.get_notes("Math")} == [10, 9, 8]')
	print(student.get_notes(input("Entrez une matière :")))

def ex5() -> None:
	test_student_notes()

if __name__ == '__main__':
	ex5()