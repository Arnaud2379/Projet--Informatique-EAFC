n = int(input("Quel type de conversion souhéterez vous faire ? "))
temp = float(input("Quel est la valeur de la température à convertir ? "))

def conv_temp(temp, n):
    if n == 1:
        #return (9/5) * temp + 32
        print(" 100 dégrés Celsius équivalent à " , (9/5) * temp + 32 , "dégrés Fahrenheit" )
    elif n == 2:
        #return (5/9) * (temp - 32)
        print(" 68 dégrés Fahrenheit équivalent à " , (5/9) * (temp - 32) , "dégrés Celsius" )
    else:
        print("la valeur de la convertion  doit être 1 ou 2")

conv_temp(temp, n)