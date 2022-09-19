# class Dog:
#
#     legs_no = 4  # variabila de clasa / atribut de clasa
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def nume_de_familie(self):
#         return self.__name
#
#     @nume_de_familie.getter
#     def nume_de_familie(self):
#         return self.__name
#
#     @nume_de_familie.setter
#     def nume_de_familie(self, prenume):
#         self.__name = prenume
#
#     @nume_de_familie.deleter
#     def nume_de_familie(self):
#         del self.__name

# def change_name(self, name):
#     self.name = name
#     return self.name
#
# @staticmethod
# def speak():
#     return "Ham ham"

# def __str__(self):
#     return str(self.__name)


# caine = Dog("Rex")
# rasa = Dog("Max")
# print(caine.nume_de_familie)
# print(caine.__dict__, 'inainte')
# caine.nume_de_familie = 'John'
# print(caine.nume_de_familie)
# print(caine.__dict__, 'dupa')
# del caine.nume_de_familie
# print(caine.nume_de_familie)
# print(caine.__dict__)
# print(caine._Dog__name)
# print(caine, caine.name)
# print(rasa.name)
# print(caine.change_name("rex1"))
# print(Dog.change_name('Rex2'))
# print(caine.speak())
# print(Dog.speak())
# Dog.legs_no = 2
# caine.legs_no = 3
# print('rasa', rasa.legs_no, 'legs no class', Dog.legs_no)
# print('caine', caine.legs_no, 'legs no class', Dog.legs_no)

#
# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
# #
# #
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# @decorator_simplu
# def functie_complexa():
#     return "Noapte buna"
#

# print(functie_simpla())
# print(functie_complexa())


# def decorator_depozit(functia_noastra):
#     def ambalaj_metoda(carti):
#         return f"Ambalam produse din {functia_noastra.__name__} care contine cartea {carti}"
#     return ambalaj_metoda
#
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume
#
# print(impachetare_carti("Baltagul"))


# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*carte):
#             return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine " \
#                    f"cartea {', '.join(x for x in carte)}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume


# print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# print(impachetare_carti("Amintiri din copilarie"))
# print(impachetare_carti())

def decorator(simbol):
    def adauga_simbol(functie):
        def functie_upper(parametru, nume):
            def functie_auxiliara():
                return 'Noapte buna'
            return parametru.upper() if parametru.upper()[-1] == '.' else parametru.upper() + simbol + functie_auxiliara()
        return functie_upper
    return adauga_simbol


@decorator(".")
def functie(propozitie, nume):
    return propozitie
#
#
print(functie("Ana are mere", "Ana"))
import time


# def calculeaza_timpul(functia):
#     def functie_interiora(*param):
#         inceput = time.time()
#         suma = functia(*param)
#         sfarsit = time.time()
#         print(f"Timp total de executie: {sfarsit - inceput}")
#         return suma
#     return functie_interiora
#
#
# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma


# print(adunare(1, 2, 3))

def calculeaza_timpul(functia):
    def functie_interiora(param):
        inceput = time.time()
        suma = functia(param)
        sfarsit = time.time()
        print(f"Timp total de executie: {sfarsit - inceput}")
        return suma
    return functie_interiora


@calculeaza_timpul
def adunare(number):
    suma = 0
    for i in range(number):
        suma += i
    return suma


# print(adunare(100000000))
