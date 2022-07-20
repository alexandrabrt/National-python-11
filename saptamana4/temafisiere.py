import csv


def introducere_categorii():
    while True:
        with open('categorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
        decizie = input('Doriti sa introduceti o alta categorie? (Y/N): ')
        print(decizie)
        if decizie.lower() == 'n':
            break
    return True


# introducere_categorii()


def introducere_taskurilor():
    while True:
        with open('taskuri.csv', 'a') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow([input('Adauga un task: ')])
        decizie = input('Doriti sa introduceti o alta task? (Y/N): ')
        print(decizie)
        if decizie.lower() == 'n':
            break
    return True


introducere_taskurilor()
