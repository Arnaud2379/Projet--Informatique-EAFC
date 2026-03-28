
def calcul_prix_ttc(HTVA , TVA):
    TVA = 21/100
    return HTVA*TVA
print(calcul_prix_ttc(20.7, 0)) 
print(calcul_prix_ttc(20.7 , 6)) 