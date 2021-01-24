#Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
#Successivamente interroga il dizionario per visualizzare la capitali di una nazione.

lista_nazioni = ["Italia", "Svizzera", "Francia", "Austria", "Germania", "Spagna", "Portogallo", "Polonia", "Grecia", "Irlanda"] #Definisco le liste con le rispettive nazioni e capitali.
lista_capitali = ["Roma", "Berna", "Parigi", "Vienna", "Berlino", "Madrid", "Lisbona", "Varsavia", "Atene", "Dublino"]
dictionary = {}

for i in range (len(lista_nazioni)): #Per ogni nazione presente nella lista "lista_nazioni" costruisco il dizionario con "lista_nazioni" come chiave e "lista_capitali" come valore.
    dictionary[lista_nazioni[i]] = lista_capitali[i]

input_utente = input("Di quale nazione vuoi trovare la capitale? ")

if input_utente in lista_nazioni:
    print("La capitale è:", dictionary[input_utente])

else:
    print("ERRORE: La nazione non è presente nella lista.")