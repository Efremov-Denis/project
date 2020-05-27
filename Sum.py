def MyFunc (a, b, c):
	if a < b and a < c:
		return b + c
	elif b < a and b < c:
		return a + c
	else:
		return a + b
number = 2
print(number + MyFunc (1, 2, 3))