'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. 
Scrivi un programma che comprenda due funzionalità:
    - L'operazione per registrare i dati dei partecipanti
    - L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si tratta dei nomi dell'elenco,
      eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco.
La funzione che produce l'elenco deve anche aggiornare l'elenco deve anche aggiornare l'elenco dei partecipanti ai quali è già stata inviata la lettera.
'''
lista_dati = []
lista_lettere_si = []

while True: #Soddisfo il primo punto della consegna, creo un ciclo while True e aggiungo il nome dei partecipanti alla lista apposita
  dati_partecipanti = input("(Digitare 'STOP' per terminare) Inserire il nome dei partecipanti: ").upper()
  lettera = input("(Digitare 'STOP' per terminare) Bisogna inviare la lettera al partecipante? ")

  if dati_partecipanti == "STOP":
    break
  else:
    lista_dati.append(dati_partecipanti)
  
  if lettera == "sì":
    lista_lettere_si.append(lista_dati.pop(lista_dati.index(dati_partecipanti))) #Ho aggiunto a "lista_lettere_si" l'elemento estratto dalla lista_dati che ha lo stesso indice di dati_partecipanti in lista_dati
  elif lettera == "no":
    pass
print("Le prenotazioni per il convegno sono:", lista_dati)
print("La lista dei partecipanti è:", lista_dati)
print("La lista dei partecipanti a cui mandare la lettera è:", lista_lettere_si)
