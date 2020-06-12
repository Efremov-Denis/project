my_f = open("test.txt", "w")
text = input('Введите несколько строк.  Для завершения программы нажмите энтер').split()

for elem in text:
	my_f.write(elem+"\n")

my_f.write("")
my_f.close()