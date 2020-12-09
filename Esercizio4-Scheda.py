#Scrivi un programma che a scelta dall'utente calcoli l'area di un quadrato, rettangolo, triangolo e cerchio.

import math #Libreria che ho importato per poter sfruttare il pi greco.

print("Programma che calcola l'area di quadrato, rettangolo, triangolo e cerchio.")

quadrato = "" #Creo le variabili intere e stringhe.
rettangolo = ""
triangolo = "" 
cerchio = ""

lato = 0
altezza = 0
base = 0
raggio = 0

area_quadrato = 0
area_rettangolo = 0
area_cerchio = 0
area_triangolo = 0

figura = str(input("Di che figura vuoi calcolare l'area? (Scrivere in minuscolo!). ")) 

if figura == "quadrato": #Creo un if ed un elif così che al cambiare della variabile figura, cambiano anche le operazioni per calcolare le aree.
    lato = int(input("Quanti centimetri misura il lato del quadrato? "))
    area_quadrato = lato * lato 
    print("L'area del quadrato è'", area_quadrato, "centimetri.")

elif figura == "triangolo":
    base = int(input("Quanti centimetri misura la base del triangolo? "))
    altezza = int(input("Quanti centimetri misura l'altezza del triangolo? "))
    area_triangolo = altezza * (base / 2)
    print("L'area del triangolo è", area_triangolo, "centimetri.")

elif figura == "rettangolo":
    base = int(input("QUanti centimetri misura la base del rettangolo? "))
    altezza = int(input("Quanti centimetri misura l'altezza del rettangolo? "))
    area_rettangolo = base * altezza 
    print("L'area del rettangolo è", area_quadrato, "centimetri.")

elif figura == "cerchio":
    raggio = int(input("QUanti centimetri misura il raggio del cerchio? "))
    area_cerchio = math.pi * (raggio * raggio)
    print("L'area del triangolo è", area_cerchio, "centimetri.")
