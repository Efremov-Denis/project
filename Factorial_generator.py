def getFiboGen():
    fact = 1
    n = 2

    yield fact
    while n <= 15:
        fact *= n
        yield fact
        n += 1
print(list(getFiboGen()))