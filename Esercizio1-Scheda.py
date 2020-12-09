#Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure meno.

print("Programma che riconosce le parole palindrome.")
parola = str(input("Inserire la singola parola che si vuole analizzare. ")) 
parola_reversed = "" #Creo la variabile affinchè possa confrontare la parola girata con quella normale.

parola_reversed = (parola[::-1]) #Tratto la parola come una lista e la inverto.

if parola_reversed == parola: #Stabilisco se la parola è palindroma o meno.
  print("Complimenti ha trovato una parola palindroma.")
else:
  print("Purtroppo questa parola non è palindroma.") 