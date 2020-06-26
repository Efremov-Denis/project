my_f = open("test.txt", "r", encoding='utf-8')
counter = 0
for line in my_f:
    counter += 1
    print(f"Количество слов в строке {counter}, - {line.count(' ') + 1}")
print(f"Всего строк - {counter}")
my_f.close()