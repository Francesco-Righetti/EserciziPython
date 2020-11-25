stipendi = []

while True:
    stipendio = int(input("Quant'è lo stipendio dei dipendenti? "))
    if stipendio == -1:
        break
    else:
        stipendi.append(stipendio)

totalestipendi = len(stipendi)
sommastipendi = sum(stipendi)
print("Calcolo la media degli stipendi")

mediastipendi = sommastipendi/totalestipendi
print("La media degli stipendi dei dipendenti = ")
print (mediastipendi, "€")