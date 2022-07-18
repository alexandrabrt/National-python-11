# functii lambda - se mai numesc si functii anonime (fara def/ fara nume)

element = lambda x: x * 10  # unde x este argumentul si x * 10 este expresia

# def element(x):
#     return x*10
element_2 = lambda x, y: x + y

""" FILTER """

# Program care sa returneze o lista cu nr pare dintr-o lista initiala

# Functia filter intoarce un obiect al clasei filter (car este defapt un iterator) rezultat
# prin aplicarea unei fct. fiecarui element dintr-un obiect iterabil (lista, tuplu, set ....etc.)
list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
# list_2 = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_2)
# print(type(list_2))

# ex cu for loop:
# lista_forloop = []
# for i in list_1:
#     if i % 2 == 0:
#         lista_forloop.append(i)
# print(lista_forloop)

# ex cu fct clasica

# def filtrare(variabila):
#     if variabila % 2 == 0:
#         return True
#     else:
#         return False
#
# filtrered = filter(filtrare, list_1)
# print(list(filtrered))

""" MAP """
# Functia map intoarce un obiect al clasei map (care este defapt un iterator) rezultat
# prin aplicarea unei fct. fiecarui element dintr-un obiect iterabil (lista, tuplu, set ....etc.)
list_3 = list(map(lambda x: x*2, list_1))
# print(list_3)

""" ZIP """
# Functia zip preia parametrii iterabili (pot fi 0 sau mai multi parametrii) si returneaza un obiect
# al clasei zip (care este defapt un iterator) sub forma de tupluri, formate din grupuri de elemente
# provenite din parametrii initiali.
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initale.

list_with_int = [1, 2, 3, 4, 5]
list_with_str = ('one', 'two', 'three', 'four', 'five')
# list_with_decimal = [1.1, 2.2, 3.3, 4.4, 5.5]
result = zip(list_with_int, list_with_str)
# print(result)
# result_list = list(result)
# print(result_list)

# val_1, val_2 = zip(*result)
# print('val_1 = ', list(val_1))
# print('val_2 = ', val_2)

""" COMPREHENSION LIST """

var = 'comprehension'

#CASE FOR LOOP
list_for_loop = []
for character in var:
    list_for_loop.append(character)
# print(list_for_loop)

#CASE LAMBDA
list_map = list(map(lambda x: x, var))
# print(list_map)

#CASE COMPREHENSION
list_string = [character for character in var]  # expresie for item in lista
# print(list_string)

numbers_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0 if 20 <= x <= 70]
# print(numbers_list)

# list_test = []
# for y in range(100):
#     if y % 2 == 0:
#         list_test.append(y)
#     elif y % 5 == 0:
#         list_test.append(y*y)

# obj = ['Par' if i % 2 == 0 else 'Impar' for i in range(10)]
# print(obj)

""" COMPREHENSION DICTIONARY """

# my_dict = {1: 'car', 2: 'bike'}

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

square_dict = {num: num*num for num in range(1, 11)}  # expression for variabila_temporara in iterabil
print(square_dict)
