candidato1 = input("Chi è il primo candidato? ") #Creo le variabili e le aggiungo alla lista.
candidato2 = input("Chi è il secondo candidato? ")
candidati = [candidato1, candidato2]

voti1 = int(input("Quanti sono i voti del primo candidato? ")) #Creo le variabili e le aggiungo alla lista.
voti2 = int(input("Quanti sono i voti del secondo candidato? "))
voti = [voti1, voti2]

candidati.sort() #Ordino le liste in ordine alfabetico e ordine decrescente.
voti.reverse()

print (candidati)
print (voti)
