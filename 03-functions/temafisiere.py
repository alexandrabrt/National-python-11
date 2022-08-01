import csv
import datetime


def introducere_categorii():

    while True:
        with open('categorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
            decizie = input("Doriti sa introduceti o alta categorie? (Y/N)").lower()
            if decizie == 'n':
                break
    return True

#introducere_categorii()

def introducerea_taskurilor():
    while True:
        with open('taskuri.csv', 'a') as file:
            csv_writer = csv.writer(file, delimiter=',')
            task = input('Adauga un task: ')
            data_limita = input('Adauga o data limita: ')
            responsabil = input('Adauga persoana responsabila: ')
            categoria = input('Adauga o categorie: ')
            with open('categorii.txt', 'r') as file:
               line = file.readlines()
            verificare = categoria.strip()
            new_list = [x.strip() for x in line]
            while verificare not in new_list:
                intr_categ = input('Reintrodu o alta categorie: ')
                if intr_categ in new_list:
                    break
                print('Categorie inexistenta; introdu alta categorie: ')
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input("Doriti sa introduceti o alta task? (Y/N)").lower()
        print(decizie)
        if decizie == 'n':
            break


    return True
introducerea_taskurilor()
