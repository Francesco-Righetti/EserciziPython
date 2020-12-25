#Crea un programma che scriva la differenza di due numeri "a" e "b" se il loro prodotto è maggiore di 10, oppure la loro somma se il loro prodotto è minore o uguale a 10.
#Esegui poi il programma con diverse coppie di valori per "a" e "b": (-5,2), (5,-5), (10,2), (-4,-5), (5,4), (-3,2).

numero_a = 0
numero_b = 0

numero_a = int(input("Inserire il primo valore: ")) #Creo gli input per entrambi i valori.
numero_b = int(input("Inserire il secondo valore: "))

if (numero_a * numero_b) > 10: #Faccio i prodotti in ogni statement del ciclo if/elif e poi stampo la differenza/somma dei due numeri.
    print("Il prodotto di questi due numeri è maggiore di 10, la differenza tra questi due numeri è quindi:", numero_a - numero_b)
elif (numero_a * numero_b) <= 10:
    print("Il prodotto di questi due numeri è minore o uguale di 10, la somma tra questi due numeri è quindi:", numero_a + numero_b)
