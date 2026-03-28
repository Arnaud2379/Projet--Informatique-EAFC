def conv_temp(temp, n):
    if n == 1:
        return (9/5) * temp + 32
    elif n == 2:
        return (5/9) * (temp - 32)
    else:
        return None

print(" 100 dégrés Celsius équivalent à " , conv_temp(100,1) , "dégrés Fahrenheit" )
print(" 68 dégrés Fahrenheit équivalent à " , conv_temp(68,2) , "dégrés Celsius" )
