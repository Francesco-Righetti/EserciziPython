'''
Aggiungi alla classe 'Atleta' un metodo per visualizzare i dati del giocatore.
'''
class Atleta:

    def __init__(self, name, surname, age, birthplace):
        self.name = name
        self.surname = surname
        self.age = age
        self.birthplace = birthplace

    def dati_personali(self):
        return f"Dati personali:\n Name: {self.name}\n Surname: {self.surname}\n Age: {self.age}\n Birthplace: {self.birthplace}"

atleta = Atleta("Mario", "Rossi", "25", "New York")
print(Atleta.dati_personali(atleta))