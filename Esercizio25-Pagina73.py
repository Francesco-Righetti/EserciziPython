candidato1 = input("Chi è il primo candidato? ")
candidato2 = input("Chi è il secondo candidato? ")
candidati = [candidato1, candidato2]

voti1 = int(input("Quanti sono i voti del primo candidato? "))
voti2 = int(input("Quanti sono i voti del secondo candidato? "))
voti = [voti1, voti2]

candidati.sort()
voti.reverse()

print (candidati)
print (voti)