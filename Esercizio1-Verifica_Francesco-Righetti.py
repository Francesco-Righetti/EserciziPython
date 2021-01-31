#Esercizio 1. Si chieda all'utente di inserire 5 studenti universitari, con nome e voto in un esame (da 18 a 30), si calcoli e si mostri quindi il valore medio dei voti e lo studente che ha preso il voto più alto.

voti_studenti = []
nomi_studenti = []

for i in range(5): 

    nome = str(input("Inserire il nome dello studente: " ))
    voto = int(input("Inserire il voto dello studente da 18 a 30: "))

    nomi_studenti.append(nome)
    voti_studenti.append(voto)

print("Il voto più alto è:", max(voti_studenti))
print("la media dei voti è:", sum(voti_studenti) / len(voti_studenti))