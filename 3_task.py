with open("text_3.txt", "r", encoding="utf-8") as my_file:
    workers = []
    line = my_file.read().split()
    for i in line:
        workers.append(i)
    for i in range(len(workers)):
        if i % 2 != 0:
            workers[i] = float(workers[i])
        if i % 2 != 0:
            if workers[i] < 20000:
                print(f'{workers[i - 1]} зарабатывает меньше 20000')
    result = 0
    for i in range(1, len(workers)):
        if i % 2 != 0:
            workers[i] = float(workers[i])
            workers[i - 2] + workers[i]
            result += workers[i]
    print(f'Средняя величина дохода сотрудников составляет: {result / (len (workers) // 2)}')