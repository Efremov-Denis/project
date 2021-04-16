list = []
temp = 0
list = input('Введите данные через пробел').split()

for i in range(len(list)):
	if i % 2 != 0:
		temp = list[i]
		list[i] = list[i - 1]
		list[i - 1] = temp
print(list)