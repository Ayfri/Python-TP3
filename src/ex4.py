class Person:
	address: str
	first_name: str
	last_name: str
	phone: str

	def __init__(self, address: str, first_name: str, last_name: str, phone: str):
		self.address: str = address
		self.first_name: str = first_name
		self.last_name: str = last_name
		self.phone: str = phone

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name} {self.address} {self.phone}"

	def set_address(self, address: str) -> None:
		self.address = address

	def set_first_name(self, first_name: str) -> None:
		self.first_name = first_name

	def set_last_name(self, last_name: str) -> None:
		self.last_name = last_name

	def set_phone(self, phone: str) -> None:
		self.phone = phone

class Student(Person):
	notes: dict[str, list[float]]

	def __init__(self, address: str, first_name: str, last_name: str, phone: str, notes: dict[str, list[float]]):
		super().__init__(address, first_name, last_name, phone)
		self.notes: dict[str, list[float]] = notes

	def __str__(self) -> str:
		return f"{super().__str__()} {self.notes}"

	def set_note(self, subject: str, note: float) -> None:
		if subject in self.notes:
			self.notes[subject].append(note)
		else:
			self.notes[subject] = [note]

	def get_average_note(self, subject: str) -> float:
		if subject in self.notes:
			return sum(self.notes[subject]) / len(self.notes[subject])
		else:
			return 0


def test_address() -> None:
	person = Person("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	assert person.address == "123 Main St"
	print(f"Adresse: {person.address} == 123 Main St")
	person.set_address(input("Entrez la nouvelle adresse: "))
	print(f"Adresse: {person.address}")

def test_first_name() -> None:
	person = Person("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	assert person.first_name == "John"
	print(f"Prénom: {person.first_name} == John")
	person.set_first_name(input("Entrez le nouveau prénom: "))
	print(f"Prénom: {person.first_name}")

def test_last_name() -> None:
	person = Person("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	assert person.last_name == "Doe"
	print(f"Last name: {person.last_name} == Doe")
	person.set_last_name(input("Entrez le nouveau nom: "))
	print(f"Nom de famille: {person.last_name}")

def test_phone() -> None:
	person = Person("123 Main St", "John", "Doe", "555-555-5555")
	print(person)
	assert person.phone == "555-555-5555"
	print(f"Téléphone: {person.phone} == 555-555-5555")
	person.set_phone(input("Entrez le nouveau numéro de téléphone: "))
	print(f"Téléphone: {person.phone}")

def ex4() -> None:
	test_address()
	test_first_name()
	test_last_name()
	test_phone()

if __name__ == "__main__":
	ex4()