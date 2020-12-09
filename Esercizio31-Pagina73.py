#Fornisci la rappresentazione in binario di un numero decimale. Dopo aver acquisito il valore del Numero da trasformare, se esegue la divisione del numero per 2, e si calcola quoziente e resto.
#Il resto è la prima cifra della rappresentazione binaria. SI ripete il procedimento assegnando il quoziente ottenuto a Numero e ricalcolando la divisione per 2.
#La ripetizione prosegue mentre il quoziente ottenuto si mantiene diverso da 0. La rappresentazione binaria del numero decimale è costituita dalle cifre binarie ottenute come resti, lette in ordine inverso.
#Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero decimale in binario.

print("Programma per convertire un numero decimale in binario. Ricorda che i numeri binari comprendono solo cifre 1 e 0.")
print()

numero_decimale = int(input("Inserire il numero da trasformare da decimale a binario. ")) #Creo l'input per il numero decimale.
binario = [] #Creo la lista.
resto = 0
quoziente = 0
x = numero_decimale 

while x != 0:
    resto = x % 2
    x = x // 2
    binario.append(resto)

binario.reverse() #Inverto la lista del resto del numero decimale, riassumo e confronto.
print("Il numero tradotto con il comando python risulta", bin(numero_decimale))
print("Il numero", numero_decimale, "tradotto con il mio programma risulta", binario)
