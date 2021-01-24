#Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo di chiave e valore.
#Usa il dizionario per trovare il nome della nazione, noto il nome della capitale.

lista_nazioni = ["Italia", "Svizzera", "Francia", "Austria", "Germania", "Spagna", "Portogallo", "Polonia", "Grecia", "Irlanda"] #Definisco le liste con le rispettive nazioni e capitali.
lista_capitali = ["Roma", "Berna", "Parigi", "Vienna", "Berlino", "Madrid", "Lisbona", "Varsavia", "Atene", "Dublino"]
dictionary = {}

for i in range (len(lista_nazioni)): #Per ogni nazione presente nella lista "lista_nazioni" costruisco il dizionario con "lista_nazioni" come valore e "lista_capitali" come chiave.
    dictionary[lista_capitali[i]] = lista_nazioni[i]

input_utente = input("Quale nazione vuoi trovare partendo dalla capitale? ")

if input_utente in lista_capitali:
    print("La nazione è:", dictionary[input_utente])

else:
    print("ERRORE: La capitale non è presente nella lista.")