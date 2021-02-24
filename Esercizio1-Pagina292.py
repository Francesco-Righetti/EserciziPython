'''
Crea una classe 'Atleta' per rappresentare le informazioni su un giocatore.
La classe deve contenere un attributo booleano chiamato 'visitaMedica'.
'''
class Atleta:

    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
        self.visitaMedica = False

    def scheda_personale(self):
        print("L'atleta pesa", self.weight, "è alto", self.height, "e ha", self.age, "anni.")

def main():
        height = input("Inserire l'altezza dell'atleta: ")
        weight = input("Inserire il peso dell'atleta: ")
        age = input("Inserire l'età dell'atleta: ")
        atleta = Atleta(height, weight, age)
        atleta.scheda_personale()
        visitaMedica = str(input("L'atleta ha effettuato la visita medica? ")).lower()
        if visitaMedica == "no":
            
        
main()