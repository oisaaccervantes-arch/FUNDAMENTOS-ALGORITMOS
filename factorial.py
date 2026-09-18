#FACTORIAL ITERATIVO
n = int(input("Ingresa un numero: "))
factorial = 1
for i in range (1, n+1):
    factorial *= i

print(factorial)

#FACTORIAL RECURSIVO
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

