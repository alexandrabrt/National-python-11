# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2

# a. 2 4 # correct
# b. error
# c. 2 4 6 8 10 ...
# d. 2 3

# list1 = [2, 33, 222, 14, 25]
# print(list1[-1])

# x = ['ab', 'cd']
# for i, v in enumerate(x):
#     x[i] = v.upper()
# for i in x:
#     print(i.upper())
# print(x)

# a. ['ab', 'cd'] # correct
# b. ['AB', 'CD']
# c. niciuna dintre variante
# d. [None, None]

# def my_function(my_list):
#     length = len(my_list)
#     temp = my_list[-1]
#     my_list[0] = my_list[length - 1]
#     my_list[length - 1] = temp
#     return my_list
#
#
# print(my_function([22, 11, 9, 44, 56]))

# a. [22, 11, 9, 44, 56]
# b. [56, 11, 9, 44, 56] # correct
# c. index error
# d. [56, 22, 11, 9, 44]

# my_list = [1, 2, 3]
# try:
#     x = my_list[3]
# except IndexError:
#     msg = "Indexul nu a fost gasit"
# except NameError:
#     msg = "Variabila nu a fost definita"
# finally:
#     msg = "Totul a mers perfect"
#
# print(msg)

# a. Variabila nu a fost definita
# b. Totul a mers perfect # correct
# c. Indexul nu a fost gasit

# my_var = ['a', 'b', {'x': 1, 'z': {'key': 30}, 'w': 2}, 10]
# valoarea 30

# a. my_var[2]['z']['key'] # correct
# b. my_var['key']
# c. my_var[2]['key']

lista = ['a', 'b', '12', 'cde']


def my_function(lista):
    lista = [1, 2, 'abc']
    # new_list = [i for i in lista]
    new_list = []
    for i in lista:
        new_list.append(i)
    return new_list


print(my_function(lista))

# a. [1, 2, 'abc'] # correct
# b. Niciunul din cele mentionate
# c. ['a', 'b', '12', 'cde']
# d. ['abc', 2, 1]
