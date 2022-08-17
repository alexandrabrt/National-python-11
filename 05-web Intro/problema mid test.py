""" Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7]. Sa se insereze in acest sir dupa fiecare element par,
dublul acestuia (2 puncte)"""

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_result = []
for i in list_1:
    list_result.append(i)
    if i % 2 == 0:
        i *= 2
        list_result.append(i)


print(list_result)
