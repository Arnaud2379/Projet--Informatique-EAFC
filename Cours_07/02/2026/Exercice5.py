a = int(input("Entrez le premier nombre "))
b = int(input("Entrez le second nombre "))

if (a > 0 and b > 0) :
    if ((a % b != 0) and (b % a != 0)):
        print("Aucun des deux nombres n'est diviseur de l'autre")
    elif ((a % b == 0) or (b % a == 0)):
        print("Au moins un des deux nombres est diviseur de l'autre ")
else:
    int(input("Entrez un nombre positif "))
    