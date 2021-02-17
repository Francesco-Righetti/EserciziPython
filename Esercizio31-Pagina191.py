'''
Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in 4 zone: Nord, Centro, Sud e Isole.
Dopo aver acquisito in un array il fatturato nelle quattro zone calcola:
- Il totale del fatturato;
- Il valore in percentuale delle vendite nelle 4 zone rispetto al totale.
'''

fatturato_azienda = []

input_nord = int(input("Qual è il fatturato: Zona Nord? ")) #definisco gli input
fatturato_azienda.append(input_nord)

input_centro = int(input("Qual è il fatturato: Zona Centro? "))
fatturato_azienda.append(input_centro)

input_sud = int(input("Qual è il fatturato: Zona Sud? "))
fatturato_azienda.append(input_sud)

input_isole = int(input("Qual è il fatturato: Isole? "))
fatturato_azienda.append(input_isole)

print("Il totale del fatturato è:", sum(fatturato_azienda), "€")
print("Il valore in percentuale delle vendite nella zona Nord è:", (input_nord/sum(fatturato_azienda)) * 100, "%")
print("Il valore in percentuale delle vendite nella zona Sud è:", (input_sud/sum(fatturato_azienda)) * 100, "%")
print("Il valore in percentuale delle vendite nella zona Centro è:", (input_centro/sum(fatturato_azienda)) * 100, "%")
print("Il valore in percentuale delle vendite nelle Isole è:", (input_isole/sum(fatturato_azienda)) * 100, "%")