class Matrix:
	def __init__ (self, elements):
		self.elements = elements.copy()

	def __str__ (self):
		s = ''
		for row in self.elements:
			for cell in row:
				s += str(cell) + ' '
			s += '\n'
		return s

	def __add__(self, other):
		new_elements = self.elements.copy()

		for i in range(len(new_elements)):
			len2 = len(new_elements[i])
			for j in range(len2):
				new_elements[i][j] += other.elements[i][j]
			

		new_matrix = Matrix(new_elements)
		return new_matrix

a = Matrix([[1]])
b = Matrix([[2]])

print(str(a))

c = a + b

print(str(c))

a = Matrix([[1,1,1],[2,2,2],[3,3,3]])
b = Matrix([[1,1,1],[1,1,1],[1,1,1]])

print(str(a+b))


