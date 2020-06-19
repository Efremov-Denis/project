number = int(input('Введите число от 1 до 12'))
sesons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
for i in range(len(sesons)):
    if number - 1 == i:
        print(sesons[i])