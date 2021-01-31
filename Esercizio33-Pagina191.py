'''
In un laboratorio di analisi i pazienti sono sottoposti ad un esame specialistico secondo l'ordine di arrivo (suggerimento: utilizza una struttura di pila per memorizzare i nomi dei paziente): scrivi il programma che consenta di registrare i nomi dei pazienti che man mano arrivano. Visualizza poi il nome del paziente che deve essere sottoposto all'esame perché è il della coda in attesa.
'''
coda_pazienti = []

while True:
    print("Per smettere di aggiornare la coda digitare 'STOP'.")
    input_pazienti = input(
        "Inserire il nome del paziente che si vuole aggiungere alla coda: ").upper()
    if input_pazienti == "STOP":
        break

    else:
        coda_pazienti.append(input_pazienti)

print()
for paziente in coda_pazienti:
    print("Ora è il turno di", paziente)
