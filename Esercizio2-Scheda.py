#Scrivi un programma che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

print("Programma che calcola la lunghezza delle parole contenute in una lista. Premere STOP per terminare l'aggiunta delle parole alla lista.")
lista_parole = [] #Creo le liste.
lista_lunghezza = []
lista_totale =  []

while True: #Creo il ciclo while True per per aggiungere le parole alla lista.
  parola = str(input("Inserire la parola di cui si vuole trovare la lunghezza. "))

  if parola == "STOP": 
      break

  else:
    lista_parole.append(parola) #Aggiungo le parole (stringhe) alla lista.
    lista_lunghezza.append(len(parola))#Aggiungo lre parole (intere) alla lista.

lista_totale = (zip(lista_parole, lista_lunghezza)) #Associo le due liste e ne stampo il contenuto.
print("Le parole e le loro rispettive lunghezze:",(list(lista_totale)))