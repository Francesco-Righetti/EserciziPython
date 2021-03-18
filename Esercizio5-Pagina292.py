'''
Elenca proprietà e metodi della classe 'Prodotto'
'''
class Prodotto:

    def __init__(self, name, brand, calories, flavour, price):
        self.name = name
        self.brand = brand
        self.calories = calories
        self.flavour = flavour

'''
Definisci il metodo 'assegna_prezzo' della classe 'Prodotto'
'''

def assegna_prezzo(self, price):
    self.price = price


def info():
    name = input("Nome del prodotto: ")
    brand = input("Azienda del profotto: ")
    calories = int(input("Calorie del prodotto: "))
    flavour = input("Sapore del prodotto: ")
    price = float(input("Prezzo del prodotto: "))

    product = Prodotto(name, brand, calories, flavour, price)

info()