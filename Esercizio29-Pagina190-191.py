'''
Nella maggior parte dei sistemi fiscali la tassazione dei redditi avviene con aliquote progressive (o a scaglioni di reddito).
Considera le seguenti aliquote:
- Fino a 15.000 euro, aliquota al 23%;
- Da 15.001 a 28.000 euro, aliquota al 27%; 
- Da 28.001 a 55.000 euro, aliquota al 38%;
- Da 55.001 a 75.000 euro, aliquota al 41%;
- Oltre 75.000 euro, aliquota al 43%.
Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la tassazione media.
'''

input_reddito = int(input("Inserire qui il proprio reddito per ricavare la tassazione media e l'imposta da pagare: "))


if input_reddito <= 15000: #Definisco gli scaglioni.
    imposta_reddito = input_reddito * 0.23
    tassazione_media = imposta_reddito/input_reddito * 100
    print("L'imposta da applicare sul reddito è", imposta_reddito,"€","e la tassazione media è al", tassazione_media,"%")

elif 15001 < input_reddito <= 28000:
    imposta_reddito = 3450 + (28000 - input_reddito) * 0.27
    tassazione_media = imposta_reddito/input_reddito * 100
    print("L'imposta da applicare sul reddito è", imposta_reddito,"€","e la tassazione media è al", tassazione_media,"%")

elif 28001 < input_reddito <= 55000:
    imposta_reddito = 3450 + 3510 + (55000 - input_reddito) * 0.38
    tassazione_media = imposta_reddito/input_reddito * 100
    print("L'imposta da applicare sul reddito è", imposta_reddito,"€","e la tassazione media è al", tassazione_media,"%")

elif 55001 < input_reddito <= 75000:
    imposta_reddito = 3450 + 3510 + 4940 + (75000 - input_reddito) * 0.41
    tassazione_media = imposta_reddito/input_reddito * 100
    print("L'imposta da applicare sul reddito è", imposta_reddito,"€","e la tassazione media è al", tassazione_media,"%")

else:
    imposta_reddito = 3450 + 3510 + 4940 + 8200 + (input_reddito - 75001)
    tassazione_media = imposta_reddito/input_reddito * 100
    print("L'imposta da applicare sul reddito è",imposta_reddito,"€","e la tassazione media è al", tassazione_media,"%")