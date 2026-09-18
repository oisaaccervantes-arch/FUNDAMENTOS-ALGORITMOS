#Encontrar número menor en un arreglo (Práctica 2) 

arreglo = [5,10,23,2,3,4]
menor = arreglo[0]

for i in arreglo:
    if i < menor:
        menor = i
                
print(menor)

