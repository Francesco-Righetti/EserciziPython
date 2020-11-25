print("Calcolo la media degli stipendi di una azienda")
print("Inserire -1 per terminare l'acquisizione dei dati")
stipendi = [] #Creo la variabile.

while True: #Creo un ciclo while per il calcolo per l'acquisizione dati degli stipendi.
    stipendio = int(input("Quant'è lo stipendio dei dipendenti? "))
    if stipendio == -1:
        break
    else:
        stipendi.append(stipendio)

totalestipendi = len(stipendi) #Calcolo la media.
sommastipendi = sum(stipendi)
print("Calcolo la media degli stipendi")

mediastipendi = sommastipendi/totalestipendi
print("La media degli stipendi dei dipendenti = ")
print (mediastipendi, "€")
