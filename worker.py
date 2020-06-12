class Worker:
	name = ""
	surname = ""
	position = ""
	_income = {"wage": 0, "bonus": 0}

class Position(Worker):
	def __init__(self, name, surname, position, wage, bonus):
		Position.name = name
		Position.surname = surname
		Position.position = position
		Position._income["wage"] = wage
		Position._income["bonus"] = bonus

	def get_full_name(self):
		print(Position.name)
		print(Position.surname)

	def get_total_income(self):
		print(Position._income["wage"] + Position._income["bonus"])


programmer = Position("Denis", "Batkovich", "Programmer", 100000, 10000)
print(Position.position)
programmer.get_full_name()
programmer.get_total_income()

manager = Position("Petr", "Batkovich", "Project manager", 90000, 20000)
print(Position.position)
manager.get_full_name()
manager.get_total_income()