votiTrump = 0
votiBiden = 0

votiTrump = int(input("Voti candidatura Trump "))
votiBiden = int(input("Voti candidatura Biden "))

votiTot = votiBiden + votiTrump

percentualeTrump = votiTrump * 100 / votiTot
print("La percentuale di voti del candidato Trump = ")
print(percentualeTrump)

percentualeBiden = votiBiden * 100 / votiTot
print("La percentuale di voti del candidato Biden = ")
print(percentualeBiden)

if percentualeBiden > percentualeTrump:
  print("Il candidato Biden vince le elezioni")

else:
  print("Il candidato Trump vince le elezioni")
