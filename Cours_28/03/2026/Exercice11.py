
def calcul_prix_ttc(HTVA , TVA = 21):
    return HTVA*(1+TVA/100)
print(calcul_prix_ttc(20.7)) 
print(calcul_prix_ttc(20.7 , 6)) 