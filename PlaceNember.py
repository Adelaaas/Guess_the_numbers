import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def PlaceNumber(a,b):
    # Создадим переменные P и N
    P = 0
    N = 0

    # разбираем первое число на цифры
    tmp = list(str(a))
    numbers_a = []
    for i in tmp:
        i = int(i)
        numbers_a.append(i)

    # разбиваем второе число на цифры
    tmp = list(str(b))
    numbers_b = []
    for i in tmp:
        i = int(i)
        numbers_b.append(i)

    idx = [] # список для запоминания индексов элементов, которые совпадают

    # цикл для подсчета P
    for i in range(len(numbers_a)):
        for j in range(len(numbers_b)):
            if numbers_a[i] == numbers_b[j]:
                if i == j:
                    P += 1
                    idx.append(i)

    # удалим элементы, у которых совпадает и место, и значение
    # чтобы дальше при подсчете их не учитывать
    numbers_a = np.array(numbers_a)
    numbers_b = np.array(numbers_b)
    numbers_a = np.delete(numbers_a, idx).tolist()
    numbers_b = np.delete(numbers_b, idx).tolist()

    # цикл для подсчета N
    c = Counter(numbers_a)
    c2 = Counter(numbers_b)
    dict(c)
    dict(c2)

    N = 0
    for key in c.keys():
        for key2 in c2.keys():
            if key == key2:
                if c[key] == c2[key2]:
                    N += c[key]
                else:
                    N += abs(c[key]-c2[key2])

    return P, N


def getPlaceNumberList(numbers: list, dop_number: int):
    P = list()
    N = list()
    for i in numbers:
        p, n = PlaceNumber(dop_number, i)
        P.append(p)
        N.append(n)

    return P, N

def numbers_show(N, P):
    plt.plot(N, P, 'bo')
    plt.xlabel('N')
    plt.ylabel('P')
    plt.show()

# print(PlaceNumber(931771, 136879))
# print(PlaceNumber(931771, 931771))
# print(PlaceNumber(931771, 773881))
# print(PlaceNumber(931771, 000000))