#ESERCIZIO 28: dato un elenco di studenti partecipanti ad una gara sportiva di lancio del peso (nome studente, lancio), visualizza il valore del lancio del vincitore (valore massimo).
print("Studenti partecipanti gara di lancio del peso 2020; per terminare l'elenco dei partecipanti premere 'A', per terminare quella dei lanci premere '1'.")

listapartecipanti = [] #Creo le liste
listalanci = []

while True: #Creo un ciclo while per l'elenco dei partecipanti.
  nomepartecipante = input("Qual è il nome del partecipante? ")
  if nomepartecipante == "A":
    break
  else:
    listapartecipanti.append(nomepartecipante)
print(listapartecipanti)

while True: #Creo un ciclo while per l'elenco dei lanci.
  numerolancio = int(input("Qual è il lancio del partecipante? "))
  if numerolancio == 1:
    break
  else:
    listalanci.append(numerolancio)

listafinale = zip(listapartecipanti,listalanci) #Associo gli elementi delle due liste.
print("Tutti gli studenti ed i loro relativi lanci:", list(listafinale)) #Riassunto dei nomi dei partecipanti e dei punteggi.
print("Il valore di lancio del vincitore è:",(max(listalanci))) #Dichiaro il lancio maggiore.