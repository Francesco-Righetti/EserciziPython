'''
Aggiungi alla classe 'Atleta' un metodo per assegnare all'atleta il nome della squadra in cui gioca
'''
class Atleta:
    def __init__(self, squadra):
        self.squadra = squadra

    def main():
        squadra = input("In che squadra gioca l'atleta? ")
        print("L'atleta gioca per la squadra", squadra)

    main()  