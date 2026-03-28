import random 
i = 0
liste = []
nbre_lance = int (input("Combien de lancé souhéterez vous éffectuer ? "))

while i<nbre_lance:
    i = i+1
    face_de = random.randint(1,6)
    liste.append(face_de)
    print(liste)


    nbre_fois1 = liste.count(1)
    nbre_fois2 = liste.count(2)
    nbre_fois3 = liste.count(3)
    nbre_fois4 = liste.count(4)
    nbre_fois5 = liste.count(5)
    nbre_fois6 = liste.count(6)
    
print("la proportion de 1 est de : ",  nbre_fois1 / nbre_lance )
print("la proportion de 2 est de : ",  nbre_fois2 / nbre_lance )
print("la proportion de 3 est de : ",  nbre_fois3 / nbre_lance )
print("la proportion de 4 est de : ",  nbre_fois4 / nbre_lance )
print("la proportion de 5 est de : ",  nbre_fois5 / nbre_lance )
print("la proportion de 6 est de : ",  nbre_fois6 / nbre_lance )


    
    
    
    
    
"""
from random import randint
 
nb_roll = int(input("Numbre de lancer: "))
 
list_roll = [randint(1,6) for i in range(nb_roll)]
 
print("Le dé à été lancé %i fois" % (nb_roll))
for i in range(1,7):
    print("Le nombre %i est tombé %.2f%% de fois" % (i,list_roll.count(i)/nb_roll*100))
"""