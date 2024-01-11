#### Определить количество различных подстрок с использованием хеш-функции

def count_unique_substrings(s):
    n = len(s)
    substrings = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])

    return len(substrings)

# Пример использования
input_string = "abcde"
result = count_unique_substrings(input_string)
print(result)  # Выведет количество различных подстрок в строке


#### Закодировать любую строку по алгоритму Хаффмана
Для реализации алгоритма Хаффмана в Python можно воспользоваться сторонней библиотекой heapq.

import heapq
from collections import defaultdict

def build_huffman_tree(string):
    frequency = defaultdict(int)
    for char in string:
        frequency[char] += 1

    priority_queue = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        for pair in left[1:]:
            pair[1] = '0' + pair[1]

        for pair in right[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(priority_queue, [left[0] + right[0]] + left[1:] + right[1:])

    return priority_queue[0][1:]

# Пример использования
input_string = "hello world"
huffman_tree = build_huffman_tree(input_string)
print(huffman_tree)  # Выведет дерево кодирования Хаффмана