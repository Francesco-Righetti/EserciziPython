#ESERCIZIO 29: dato un elenco di città, con l'indicazione per ciascuna di esse del nome e delle temperature massime e minime registrate in un giorno.
#Si devono contare quante città hanno superato nel giorno un valore prefissato per l'escursione termica, ottenuta per differenza tra temperatura massima e minima.
#Organizza un programma che, dopo aver richiesto il valore da controllare dell'escursione termica, per ogni città dell'elenco ripeta la richiesta dei dati (nome temperatura massima e minima).
#Calcola e controlla se l'escursione termica è maggiore del valore prefissato: in questo caso, incremente il contatore delle città selezionate. Alla fine della ripetizione comunica il numero delle città registrato nel contatore.

print("Programma per il calcolo dell'escursione termica di diverse città.") 
print()

nome_citta = [] #Creo le liste.
escursione_termica = []
temperature_massime = []
temperature_minime = []
listafinale = []

temp_max = 0 #Creo le variabili.
temp_min = 0
contatore_citta = 0
variabile_conteggio = 0

#Scrivo l'input e prestabilisco un numero per l'escursione termica, ed un altro per il numero massimo di città da considerare.
escursione_stabilita = (int(input("Inserire un valore per delineare un escursione termica prefissata. ")))
numero_citta = (int(input("Inserire un numero massimo di città di cui calcolare l'escursione. ")))

while variabile_conteggio != 0: #Creo il ciclo while con relativo if.
    citta = (str(input("Inserire il  nome della città.")))
    nome_citta.append(citta)
    temp_max = (int(input("Inserire la temperatura massima registrata.")))
    tem_min = (int(input("Inserire la temperatura minima registrata.")))
    temperature_massime.append(temp_max)
    temperature_minime.append(temp_min)
    variabile_conteggio = variabile_conteggio + 1
    
    if escursione_stabilita < temperature_massime - temperature_minime:
        escursione_termica.append(temperature_massime - temperature_minime)
        contatore_citta = contatore_citta +1

listafinale = zip(nome_citta, temperature_massime, temperature_minime) #Associo gli elementi come richiede l'esercizio, e concludo.
print(list(listafinale))
print("Abbiamo calcolato l'escursione termica di", numero_citta,"città e tra queste,", contatore_citta, "città hanno superato il valore d'escursione stabilito.")

