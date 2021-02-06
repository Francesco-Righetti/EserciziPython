'''
Organizza con un dizionario i dati sui conti correnti bancari con numero del conto e saldo. 
Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
'''
conto_corrente = dict()

for i in range(5):

    numero_conto = input("Inserire il numero identificativo del conto: ")
    saldo_conto = int(input("Inserire il saldo del conto: "))
    conto_corrente[numero_conto] = saldo_conto

print("I rispettivi codici identificativi e saldi sono:", conto_corrente)
            
input_utente = input("Inserire il numero identificativo del conto corrente che si vuole trovare: ")

if input_utente in conto_corrente:
    print("Il saldo del tuo conto corrente è di", conto_corrente[input_utente], "€.")

else:
    print("ERRORE: il numero identificativo non corrisponde a nessun conto corrente presente nel database.")
