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