'''
#Ingresar 15 numeros enteros y determinar cuantos son poistivos, negativos y cuantos son multiplos de 3.
#Calcular la suma de los número pares ingresados
introducir = []
positivos = 0
negativos = 0
multiplos3 = 0
suma_pares = 0
for i in range(15):
    numero = int(input(f"Ingrese el número {i+1}: "))
    introducir.append(numero)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    if numero % 3 == 0:
        multiplos3 += 1
    if numero % 2 == 0:
        suma_pares += numero

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Múltiplos de 3: {multiplos3}")
print(f"Suma de números pares: {suma_pares}")


#Solicita un entero positivo y determine la cantidad de dígitos que tiene, la suma de sus digitos y cuantos de ellos son pares

introducir = int(input("Ingrese un número entero positivo: "))
if introducir < 0:
    print("El número ingresado no es positivo.")
else:
    cantidad_digitos = 0
    suma_digitos = 0
    cantidad_pares = 0
    while introducir > 0:
        digito = introducir % 10
        cantidad_digitos += 1
        suma_digitos += digito
        if digito % 2 == 0 and digito != 0:
            cantidad_pares += 1
        introducir //= 10

    print(f"Cantidad de dígitos: {cantidad_digitos}")
    print(f"Suma de los dígitos: {suma_digitos}")
    print(f"Cantidad de dígitos pares: {cantidad_pares}")

#Una aplicación matemática que calcule la suma de la serie S= ∑_(i=1)=▒(i^2+3i)/(2i+1) para un valor n ingresado por el usuario.
#Desarrolle un programa que solicite el valor de n y calcule el resultado de la sumatoria utilizando una estructura de repetición. Muestre el resultado con cuatro decimales.
while True:
    n = int(input("Ingrese el valor de n (debe ser un entero positivo): "))

    if n >= 1:
        break  
    else:
        print("Error: El valor de n debe ser mayor o igual a 1. Intente de nuevo.")

S = 0

for i in range(1, n + 1):
    termino = (i**2 + 3 * i) / (2 * i + 1)
    S += termino

print(f"El resultado de la sumatoria S es: {S:.4f}")


#Una máquina industrial registra valores de producción durante su funcionamiento. Desarrolle un programa que solicite cantidades producidas y acumule los valores ingresados hasta que se registre una cantidad igual a cero. 
#Al finalizar, determine el total producido, el promedio y la mayor cantidad registrada.

total_producido = 0
cantidad_registrada = 0
mayor_cantidad = float('-inf')  
while True:
    cantidad = int(input("Ingrese la cantidad producida (0 para finalizar): "))
    if cantidad == 0:
        break
    total_producido += cantidad
    cantidad_registrada += 1
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad

if cantidad_registrada > 0:
    promedio = total_producido / cantidad_registrada
else:
    promedio = 0

print(f"Total producido: {total_producido}")
print(f"Promedio: {promedio:.2f}")
print(f"Mayor cantidad registrada: {mayor_cantidad}")
'''
#Desarrolle un programa que solicite un número entero positivo n y genere los primeros n términos de la siguiente secuencia:
#2, 6, 12, 20, 30, 42,…
#Calcule también la suma de los términos generados. 


while True:
    n = int(input("Ingrese la cantidad de términos (n debe ser mayor o igual a 1): "))
    if n >= 1:
        break
    else:
        print("Error: El valor debe ser un entero positivo. Intente de nuevo.")

suma_total = 0

print("\nLos primeros", n, "términos de la secuencia son:")

for i in range(1, n + 1):
    
    termino = i**2 + i
    
    if i < n:
        print(termino, end=", ")
    else:
        print(termino) 
        
    suma_total += termino
print(f"\nLa suma de los {n} términos generados es: {suma_total}")