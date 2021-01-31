'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. 
Scrivi un programma che comprenda due funzionalità:
    - L'operazione per registrare i dati dei partecipanti
    - L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si tratta dei nomi dell'elenco,
      eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco.
La funzione che produce l'elenco deve anche aggiornare l'elenco deve anche aggiornare l'elenco dei partecipanti ai quali è già stata inviata la lettera.
'''
lista_dati = []

while True: #Soddisfo il primo punto della consegna, creo un ciclo while True e aggiungo il nome dei partecipanti alla lista apposita
  dati_partecipanti = input("Inserire il nome dei partecipanti:")
  if dati_partecipanti == "STOP":
    break

  else:
    lista_dati.append(dati_partecipanti)


