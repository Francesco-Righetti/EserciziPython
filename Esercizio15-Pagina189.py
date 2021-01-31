#Dato un elenco di nazioni contenuto in una lista ed uno delle rispettive capitali in una seconda lista (nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste).
#Visualizza la capitale di una nazione della quale viene fornito da tastiera il nome, segnalando con un messaggio di errore il caso in cui la nazione richiesta non sia compresa nell'elenco.

lista_nazioni = ["Italia", "Svizzera", "Francia", "Austria", "Germania", "Spagna", "Portogallo", "Polonia", "Grecia", "Irlanda"] #Dichiaro le liste con le rispettive nazioni e capitali.
lista_capitali = ["Roma", "Berna", "Parigi", "Vienna", "Berlino", "Madrid", "Lisbona", "Varsavia", "Atene", "Dublino"]

input_utente = input("Di quale nazione vuoi trovare la capitale? ")

if input_utente in lista_nazioni:
    index = lista_nazioni.index(input_utente)
    print("La capitale è:", (lista_capitali[index]))

else:
    print("ERRORE: La nazione non è presente nella lista.")

