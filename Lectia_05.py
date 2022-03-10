nr_candidati = int(input('Cite persoane: '))
candidati = dict()
list_14_18 = []
list_18_25 = []
list_26_45 = []
list_45 = []
for n in range (nr_candidati):
    nume = []
    Nume = input('Numele: ')
    Prenume = input('Prenume: ')
    Virsta = int(input('Virsta: '))
    if Virsta < 14:
        print('Mai cresti')
    else:
        nume.append(Nume)
        nume.append(Prenume)
        nume.append(Virsta)
        candidati[n] = nume
name_14_18 = []
name_18_25 = []
name_26_45 = []
name_45 = []
for n in range(len(candidati)):
    if 14 < candidati[n][2] < 19:
        list_14_18.append(candidati[n])
        name_14_18.append(list_14_18[-1][0])
    elif 18 < candidati[n][2] < 26:
        list_18_25.append(candidati[n])
        name_18_25.append(list_18_25[-1][0])
    elif 25 < candidati[n][2] < 46:
        list_26_45.append(candidati[n])
        name_26_45.append(list_26_45[-1][0])
    else:
        list_45.append(candidati[n])
        name_45.append(list_45[-1][0])




print(candidati)
print(name_14_18)
if len(name_14_18) > 0:
    print(f"Oameni cu vrsta de la 14-18 {','.join(name_14_18)}")
if len(name_18_25) > 0:
    print(f"Oameni cu vrsta de la 18-25 {','.join(name_18_25)}")
if len(name_26_45) > 0:
    print(f"Oameni cu vrsta de la 26-45 {','.join(name_26_45)}")
if len(name_45) > 0:
    print(f"Oamneii cu virsta mai mult de 45 {','.join(name_45)}")
