nr_person = int(input("Introduceti cite persoane vor fi: "))
dict_persone = dict()
date = dict()
list_14_18 = dict()
list_18_25 = dict()
list_26_45 = dict()
list_45 = dict()
for n in range(nr_person):
    Nume = input(f"Numele {n +1} persoane: ")
    Prenume = input(f'Prenumele {n+1}:  ')
    Virsta = int(input(f'Virsta {n+1}: '))
    if Virsta <= 14:
        print("Mai cresti")
    else:
        date['Nume'] = Nume
        date['Prenume'] = Prenume
        date['Virsta'] = Virsta
        dict_persone[Nume] = date
        if Virsta < 19:
            list_14_18[Nume] = date['Nume']
        elif 18 < Virsta < 25:
            list_18_25[Nume] = date['Nume']
        elif 24 < Virsta < 45:
            list_26_45[Nume] = date['Nume']
        else:
            list_45[Nume] = date
print(f'People between ages 14 and 18 :  {list_14_18[Nume]}' )
print(f'People between ages 18 and 25 :  {list_18_25[Nume] }' )
print(f'People between ages 26 and 45 :  {list_26_45[Nume] }' )
print(f'People above age 45  :  {list_45[Nume]}' )
