#ITERATIVO
n = int(input("Ingresa un numero: "))
suma = 0
for i in range (1, n+1):
    suma += i
    
print(suma)

#RECURSIVO

def suma(n):
    if n == 0:
        return 0
    
    return n + suma (n -1)

print(suma(5))
    