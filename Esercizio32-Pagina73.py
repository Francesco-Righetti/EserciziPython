#Implementa l'argoritmo per il calcolo della soluzione di un'equazione di primo grado ax + b = 0.
#Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella che segue: (tabella pagina 73).

import fractions

a = int(input("Inserire il valore di a: "))
b = int(input("Inserire il valore di b: "))

if a == 0 and b == 0:
    print("L'equazione è indeterminata.")

elif a == 0 and b != 0:
    print("L'equazione è impossibile.")

elif a != 0 and b == 0:
    print(" In questo caso x = 0.")

else: #quando a e b != 0:
    if b%a != 0: #soluzione dispari
        x = fractions.Fraction(- b , a) #La funzione ".Fraction", facente parte della libreria "fractions", crea una frazione tra i numeri/variabili indicati nella parentesi.
        print("La soluzione è x =", x) 

    else:
        x = -(b / a)
        print("La soluzione è x =", int(x))