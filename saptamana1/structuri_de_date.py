# structuri de date

# LISTE - ordonate (pot fi indexate) / mutabile (poate fi modificat)
my_list = [8, 2, 'a', 8, '4']
# var = my_list.pop(0)
my_list.remove(8)
# my_list = []
my_list.clear()
# print(var)
# print(my_list)
# my_list.pop()
# print(my_list)
# print('Mesaj')
# print(type(my_list))  # tipul unei variabile
# print(my_list[2])
# print(my_list[3])
# print(my_list[-1])
# print(len(my_list))
# my_list.append('ANA')
# print(my_list.index(8))
# my_list.insert(7, 'A')
# print(my_list[2:5])
# my_list.append(['A', 'B', 3, 'x', [4, 7, 'w']])
# print(my_list)
# print(my_list[7][4][2])
# print(my_list[7:8])
# print(len(my_list))
# print(my_list[len(my_list) - 1])
# print(my_list[2::3])
# list_1 = [2, 3]
# list_2 = [5, 6]
# list_3 = list_2 + list_1
# print(list_3)

#  TUPLURI - ordonate (pot fi indexate)/ imutabile (nu pot fi modifcate)

# my_tuple = (8, 2, 'a', 8, '4')
# zile_anului = ('luni', )
# zile_anului = tuple()
# zile_anului = ()
# print(type(zile_anului))
# lista_1 = [1]

# lista_1 = ('Ana', 'Ion', 'Mihai', 'Bogdan', 'Ovidiu')
# (name_1, *name_2, name_3) = lista_1
# print(lista_1[-1])
# print(name_2)
# print(name_3)

#  SETURI - neordonate (nu pot fi indexate)/ imutabile (nu pot fi modifcate)

# set_1 = {'mar', 'para', 'banana'}
# # set_1.remove('caisa')
# set_1.clear()
# print(set_1)
# new_set = list(set(my_list))
# print(new_set)

#  DICTIONAR - ordonate (pot fi indexate)/ mutabile (pot fi modifcate)
# dict_1 = dict()
# dict_2 = {'key_1': '',
#           'key_2': 'valoare',
#           3: [1, 2, 3],
#           4: ('valoare_1', 'val_2'),
#           'dict_b': {'dic_c': 3},
#           2+1j: [1, 2, 5]}
# # val = dict_2.items()
# dict_2.clear()
# dict_2 = dict()
# print(dict_2)

# CONDITIOARI

# varsta = 12
# if varsta >= 18:
#     print("Sunteti eligibil pentru scoala de soferi")
# else:
#     print("Sunteti eligibil doar dupa varsta de 18 ani")
#     if varsta != 17:
#         print("Mai aveti un an pentru a fi eligibil")

# varsta = True
# varsta_1 = None, 0, ''
#
# if not varsta_1:
#     print(1)
# else:
#     print(2)
# if varsta >= 65:
#     print("varsta pensionare")
# elif varsta == 15 or varsta == 25:
#     print("varsta liceu sau facultate")
# # elif varsta >= 15:
# #     print("varsta liceu")
# # else:
# print('esti micut!')


# WHILE

# print('primul print')
# i = 0
# while i >= 0:
#     print('se respecta conditia')
#     print('valoarea este: ' + str(i))
#     i += 1
#     # i = i + 1
# print('am ajuns la sfarsit')


# FOR
list_a = []
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list_1:
    i += 1
    list_a.append(i)
print(list_a)
