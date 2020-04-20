words = input('Введите несколько слов, разделяя их пробелами').split()
number = 0
for i in range(len(words)):
	number += 1
	print(number, words[i][0:10])