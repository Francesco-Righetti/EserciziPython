'''
I nomi delle città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseriti da tastiera e memorizzati in un dizionario dov'è il CAP è la chiave.
Fornito poi da tastiera il nome di una citta, costruisci un programma che visualizzi il suo CAP, oppure un messaggio nel caso la città non sia compresa nell'elenco.
Analogamente, fornendo il CAP il programma restituisce il nome della città oppure un messaggio d'errore.
'''

dizionario_CAP = {}

while True:

    input_città = input("Inserire il nome della città: ")
    
    if input_città == "STOP":
        break

    else:
        input_CAP = int(input("Inserire il corrispettivo CAP: "))
        dizionario_CAP[input_CAP] = input_città

domanda = input("Di che città vuoi sapere il CAP? ")
if domanda in dizionario_CAP:
    print("Il CAP di", domanda, "è", dizionario_CAP[domanda])
else:
    print("La città inserita non è presente nell'elenco")