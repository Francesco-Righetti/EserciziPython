#Fornisci la rappresentazione in decimale di un numero binario. All'inizio si richiede il numero di cifre di cui è composto il numero binario (lunghezza); 
#Si esegue poi una ripetizione che richiede le cifre del numero binario una ad una a partire da destra per ciascuna calcola il prodotto della cifra binaria per la potenza di 2
#corrispondente alla posizione della cifra binaria e aggiunge il risultato alla somma; la ripetizione viene eseguita per il contatore che va dal valore 0 al valore di lunghezza diminuito di 1.
#Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero binario in decimale.
print("Programma per convertire un numero binario in decimale. Ricordarsi che i numeri binari comprendono solo cifre 1 e 0.")
print()

grado_esponente = 0 #Creo le variabili.
numero_decimale = 0
numero_binario = ""
variabile = 0 
numero_esponente = 0

lunghezza_binario = int(input("Quante cifre presenta il numero binario? ")) #Creo l'input per la lunghezza del numero binario.

while variabile != lunghezza_binario: #Creo il ciclo while.
    cifre = int(input("Digitare le cifre a partire da destra: "))
    numero_esponente = numero_esponente + 1
    numero_decimale += cifre * (numero_esponente ** 2)
    numero_binario = numero_binario + str(cifre)
    variabile = variabile + 1
    
print("Utilizzando il comando di python il numero risulta", int(numero_binario, 2)) #Riassunto e confronto.
print("Utilizzando il mio programma il numero risulta", numero_decimale)
