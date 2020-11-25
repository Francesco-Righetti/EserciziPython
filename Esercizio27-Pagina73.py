veicoli = []
countergiorni = 0
print("Programma per calcolare il numero di veicoli transitati in un casello autostradale in un numero definito di giorni.")
print("Inserire 0 quando si è completato il conteggio dei veicoli.")

while True:

    veicolo = int(input("Quanti veicoli hanno transitato in entrata di questo casello stradale? "))
    if veicolo == 0:
        break

    else:
        countergiorni += 1
        veicoli.append(veicolo)

totveicoli = (sum(veicoli))
print("Il totale dei veicoli che hanno transitato in autostrada in", countergiorni, "giorni =", totveicoli)