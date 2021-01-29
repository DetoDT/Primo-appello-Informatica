from operator import itemgetter
'''
[
['.', '.', '.', '.', 'f', 'f', 'f', 'f'], 
['.', '.', '.', '.', '.', 'f', 'f', 'f'],
['.', '.', '.', '.', '.', '.', 'f', 'f'],
['.', '.', '.', '.', '.', '.', 'f', 'f'],
['.', '.', '.', '.', '.', '.', 'f', 'f'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.']
]
'''

campo = open('c:/Users/franc/Documents/Coding/Python/Informatica Polito/Pompieri(primo appello)/incendio.txt', 'r')
servizio = open('c:/Users/franc/Documents/Coding/Python/Informatica Polito/Pompieri(primo appello)/servizio.txt', 'r')
riserva = open('c:/Users/franc/Documents/Coding/Python/Informatica Polito/Pompieri(primo appello)/riserva.txt', 'r')
# Creo una tabella con lo schema del file incendio
tab = []
for line in campo:
    line = line.strip('\n').split(' ')
    tab.append(line)

# Dato che i pompieri agiscono in verticale creo una nuova tabella ruotata di 90 gradi
vert_tab = []
for l in range(len(tab)):
    vert = []
    for i in range(len(tab[l])):
        vert.append(tab[i][l])
    vert_tab.append(vert)

# Salvo la dimensione dell'incendio per ogni riga in un dizionario
posizioni = {}
for l in range(len(vert_tab)):
    posizioni[l] = 0
    for i in vert_tab[l]:
        if i == 'f':
            posizioni[l] += 1

pos = sorted(posizioni.items(), key=itemgetter(1), reverse=True)
# Organizzo i pompieri in un dizionario...
pompieri = {}
for line in servizio:
    line = line.strip('\n').split(';')
    pompieri[line[0]] = line[2]

# ... e anche la riserva
ris = {}
for line in riserva:
    line = line.strip('\n').split(';')
    ris[line[0]] = line[2]

serviziopompieri = sorted(pompieri.items(), key=itemgetter(1), reverse=True)
riserve = sorted(ris.items(), key=itemgetter(1), reverse=True)
serviziopompieri.append(riserve)
# Associo ogni pompiere ad una zona
pompiere_zona = {}

count = 0
for i in pos:
    if i[1] != 0 and count < 3:
        pompiere_zona[i] = serviziopompieri[count]
        count += 1
    elif i[1] != 0 and count >= 3:
        pompiere_zona[i] = riserve[count - 3]

# 'Schiero' i pompieri nella tab
for key in pompiere_zona:
    pos1 = key[1]
    pos2 = key[0]
    schedapompiere = pompiere_zona[key]
    idpompiere = schedapompiere[0]
    gradopompiere = int(schedapompiere[1])
    tab[pos1][pos2] = idpompiere
    n = pos1 - 1
    if gradopompiere <= pos1 + 1:
        for i in range(gradopompiere):
            if tab[n][pos2] == 'f':
                tab[n][pos2] = '+'
                n -= 1
    elif gradopompiere > pos1 + 1:
        for i in range(pos1 + 1):
            if tab[n][pos2] == 'f':
                tab[n][pos2] = '+'
                n -= 1
count = 1
for l in tab:
    count += 1
    if 'f' in l:
        print("Serve l'intervento dell'aereo di merda")
        break
    elif count == len(tab) and 'f' not in l:
        print('Incendio controllato')
for i in tab:
    print(i)


    
















campo.close()
servizio.close()
riserva.close()