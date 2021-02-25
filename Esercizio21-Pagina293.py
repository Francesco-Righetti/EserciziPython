'''
Data la classe "Motociclo" creata nel problema 7 deriva la classe "Ciclomotore".
#Aggiungi le proprietà opportune e modifica il metodo che consente di visualizzare i valori delle proprietà
'''
class Motociclo:

    def __init__(self, template, color, price, max_speed, displacement):
        self.template = template
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.displacement = displacement
    

    def info(self):
        print("Modello:", self.template)
        print("Colore:", self.color)
        print("Prezzo:", self.price, "€.")
        print("Velocità massima:", self.max_speed, "km/h.")
        print("Cilindrata:", self.displacement, "cm3.")

def main():
    template = input("Inserisci il modello del motociclo: ")
    color = input("Inserisci il colore del motociclo: ")
    price = int(input("Inserisci il prezzo del motociclo: "))
    max_speed = int(input("Inserisci la massima velocità del motociclo: "))
    displacement = float(input("Inserisci la cilindrata del motociclo: "))
    m1 = Motociclo(template, color, price, max_speed, displacement)
    m1.info()


main()

class Ciclomotore(Motociclo):
    displacement = 0.0

    def info(self):
        super().info()
        self.displacement = float(input("Cilindrata del mezzo: "))

    def stampa(self):
        super().stampa()
        print("Cilindrata del mezzo:", self.displacement, "cm3.")