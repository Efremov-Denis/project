def int_func(word):
    return word.title()
words_list = input('Введите несколько слов, разделяя их пробелами').split()
new_list = []
for i in words_list:
    new_list.append(int_func(i))
print(' '.join(new_list))