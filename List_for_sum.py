def calcSum():
    result = 0
    while True:
        numberslist = input('Введите числа, разделяя их пробелами').split()
        sum = 0
        ending_symbol = 'q'

        for elem in numberslist:
            if elem != ending_symbol:
                elem = int(elem)
                sum += elem
            else:
                result += sum
                return result
        result += sum
        print(result)

print(calcSum())
print('Конец программы')