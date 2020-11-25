veicoli = [] #Creo la variabile.
countergiorni = 0 #Creo un counter per tenere conto del periodo di tempo considerato per il calcolo dei veicoli transitati.
print("Programma per calcolare il numero di veicoli transitati in un casello autostradale in un numero definito di giorni.")
print("Inserire 0 quando si è completato il conteggio dei veicoli.")

while True: #Creo il ciclo while per l'acquisizione dei veicoli transitati in un arco definito di tempo.
    veicolo = int(input("Quanti veicoli hanno transitato in entrata di questo casello stradale? "))
    if veicolo == 0:
        break
    else:
        countergiorni += 1
        veicoli.append(veicolo)

totveicoli = (sum(veicoli)) #Calcolo la somma dei veicoli totali transitati in un arco definito di tempo.
print("Il totale dei veicoli che hanno transitato in autostrada in", countergiorni, "giorni =", totveicoli)
