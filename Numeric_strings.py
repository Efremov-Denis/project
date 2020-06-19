word_list = input('Введите несколько слов, разделяя их пробелами').split()
counter = 0
for word in word_list:
    counter += 1
    print(counter, ' ', word[0:10])