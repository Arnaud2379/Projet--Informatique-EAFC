Liste_nombre = []

def div_prop(n):
    for i in range(1,n):
        if n%i == 0:
            Liste_nombre.append(i)

div_prop(28)    
print(Liste_nombre)       
        
def est_parfait():
   if sum(div_prop)