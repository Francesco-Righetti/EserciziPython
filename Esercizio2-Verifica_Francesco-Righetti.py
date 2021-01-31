#Esercizio 2. Dati i risultati in un test di una classe di 10 studenti, con nome e giudizio (sufficiente S, buono B, distinto D, ottimo O), calcolare la media dei giudizi assegnando a ciascuno di essi un peso da 1 a 4 nell'ordine. 

voti_studenti = []
voto_finale = ()

for i in range(10):

    nome_studenti = input("Inserire il nome dello studente: ")
    voti_studenti = input("Inserire il giudizio dello studente: ").lower #Converte sempre in minuscolo il testo. 

    if voti_studenti == "sufficiente": 
        voto_finale = 1

    elif voti_studenti == "buono":
        voto_finale = 2

    elif voti_studenti == "distinto":
        voto_finale = 3

    elif voti_studenti == "ottimo":
        voto_finale = 4

    voti_studenti.append(voto_finale)

print("La media dei voti è : ", sum(voti_studenti) / len(voti_studenti))