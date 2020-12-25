#Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a 0).

print("Questo programma verifica se un numero è pari o dispari.")

def nuova_funzione(numero):

    if (numero%2 == 0):
         return "pari"
    elif (numero%2 == 1):
        return "dispari"
        
numero = int(input("Inserire il numero: "))
print("Il numero inserito è", nuova_funzione(numero))