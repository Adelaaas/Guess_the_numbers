def PlaceNumber(a,b):
    # разбираем первое число на цифры
    tmp = list(str(a))
    numbers_a = []
    for i in tmp:
        i = int(i)
        numbers_a.append(i)

    tmp = list(str(b))
    numbers_b = []
    for i in tmp:
        i = int(i)
        numbers_b.append(i)

    return numbers_a, numbers_b

print(PlaceNumber(931771, 136879))