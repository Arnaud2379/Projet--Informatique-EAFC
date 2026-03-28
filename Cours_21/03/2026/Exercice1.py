import math 

angle = float(input("Entrez un angle en dégrés: "))
angle_rad = math.radians(angle)
resultat = math.sin(angle_rad) 
print("le sinus de " , angle,"dégrés est ", resultat)