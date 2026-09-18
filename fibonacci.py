#------------ITERATIVO----------------
#Numero de fibonacci
n = 5 
#Inicializar variables 
anterior = 0 
actual = 1
print("FIBONACCI ITERATIVO")
print(anterior) # para imprimir el 0 

for i in range (n): #Recorre n veces 
    siguiente = anterior + actual #Crea una nueva variable la primera vez
    anterior = actual #La anterior pasa a ser la actual
    actual = siguiente #La actual pasa a ser la variable creada 
    print(anterior)
    
#--------------RECURSIVO CON PD-----------
print("\nFIBONACCI RECURSIVO CON PROGRAMACIÓN DINAMICA") 
memoria = {} #Memoria es un diccionario que guarda clave y valor del fibonacci

def fibonacci(n):
    #Casos base
    if n == 0: 
        return 0

    if n == 1:
        return 1
    #Si un valor estaba en memoria lo toma en lugar de buscarlo 
    if n in memoria:
        return memoria[n]

    #Los guarda en memoria 
    #n es clave 
    #El resultado de la suma es el valor
    memoria[n] = fibonacci(n - 1) + fibonacci(n - 2)
    # Fibonacci 5 necesita F(4) y F(3)
    # Primero comienza por el lado izquierdo: F(4)

    # F(4) necesita F(3) y F(2)
    # F(3) necesita F(2) y F(1)
    # F(2) necesita F(1) y F(0)

    # F(1) es caso base: devuelve 1
    # F(2) ya recibió el 1 y ahora busca F(0)
    # F(0) es caso base: devuelve 0

    # F(2) suma 1 + 0 = 1
    # Guarda memoria[2] = 1
    # F(2) devuelve 1

    # Regresamos a F(3)
    # F(3) ya recibió F(2) = 1
    # Ahora busca F(1), que devuelve 1

    # F(3) suma 1 + 1 = 2
    # Guarda memoria[3] = 2
    # F(3) devuelve 2

    # Regresamos a F(4)
    # F(4) ya recibió F(3) = 2
    # Ahora busca F(2)
    # F(2) ya está en memoria y vale 1

    # F(4) suma 2 + 1 = 3
    # Guarda memoria[4] = 3
    # F(4) devuelve 3

    # Regresamos a F(5)
    # F(5) ya recibió F(4) = 3
    # Ahora busca F(3)
    # F(3) ya está en memoria y vale 2

    # F(5) suma 3 + 2 = 5
    # Guarda memoria[5] = 5
    # F(5) devuelve 5

    return memoria[n]


for i in range (n+1):
    print(fibonacci(i))
    
#RECURSIVO SIN PD
#   Como no hay memoria vuelve a calcular todo el recorrido 
#   cada vez que necesita un valor.

print("\nFIBONACCI RECURSIVO SIN PROGRAMACIÓN DINAMICA")
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range (n+1):
    print(fibonacci(i))
  


print(fibonacci(5))    
