my_list = input('Введите данные, разделяя их пробелами').split()
temp = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        temp = my_list[i]
        my_list[i] = my_list[i - 1]
        my_list[i - 1] = temp
print(my_list)