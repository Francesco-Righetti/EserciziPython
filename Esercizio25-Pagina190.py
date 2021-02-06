'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario che ha per chiave la matricola, mentre il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali. '''

voti_studenti = {}
counter_studente = 0

while True:

  print("Studente numero:",counter_studente,)
  counter_studente += 1
  voto = float(input("Qual è il voto dello studente? "))
  voti_studenti[counter_studente] = voto

  if voto > 10:
    print("ATTENZIONE: i voti non possono superare il 10, ritenta!")
    counter_studente -= 1

  else:
    pass
  
  if counter_studente == 4:
    print("Il voto più alto in classe è stato:")
    print(max(voti_studenti.values()))
    break

  else:
    pass

print(voti_studenti.values())

