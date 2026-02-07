a = float(input("Entrez le  nombre a "))
b = float(input("Entrez le  nombre b "))
c = float(input("Entrez le  nombre c "))

delta = b**2 - 4*a*c
if delta < 0:
    print("pas de solution possible")
elif delta == 0:
    X1 = X2 = -b/ 2*a
    print("Une solution double X1 = X2 = ",X1)
else :
    X1 = (-b-delta**1/2) / 2*a
    X2 = (-b+delta**1/2) / 2*a
    print("Les solutions sont X1 =",X1 , "et X2 =",X2)
    