'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. 
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente nella rubrica.
'''
numeri_telefonici = {} 

while True: #Creo un ciclo while True per inserire nome e numero telefonico dell'utente. Definisco anche il dizionario.
  nome_utente = input("Inserire il nome dell'utente (Digitare 'STOP' per terminare): ")

  if nome_utente == "STOP":
    break

  else:
    numero_cellulare = int(input("Inserire il numero telefonico: "))
    numeri_telefonici[nome_utente] = numero_cellulare

input_nome = input("Quale utente vuole cercare? ")
if input_nome in numeri_telefonici.keys():
  print("Il numero telefonico dell'utente è:", numeri_telefonici[input_nome])

else:
  print("SPIACENTI: Il nome non è nella rubrica.")