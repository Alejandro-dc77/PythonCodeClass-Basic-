#Ejercicio 1: Ocupación de estacionamientos 
#En una matriz , 1 representa un espacio ocupado y 0 un espacio libre
#Cuenta ocupados y libres por fila y calcula el porcentaje total de ocupación
'''
m = [
    [1,0,1,1,0],
    [0,1,1,0,0],
    [1,1,1,1,0],
    [0,0,1,0,1]
    ]

ocupados = 0
libres = 0

for i in range(4):
    ocupados_fila = 0
    libres_fila = 0
    for j in range(5):
        if m[i][j] == 1:
            ocupados = ocupados + 1
            ocupados_fila = ocupados_fila + 1
        else:
            libres = libres + 1
            libres_fila = libres_fila + 1
    print(f"Fila{i}: {ocupados_fila} ocupados, {libres_fila} libres")

print("Ocupados: ",ocupados)
print("Libres: ",libres)
print(f"Ocupación %: {ocupados / (len(m) * len(m[0])) * 100:.2f}")




m = [
    [90,110,95],
    [120,105,130],
    [80,85,100],
    [150,140,135]
    ]

m_nueva= []
for i in range(4):
    fila = []
    for j in range(3):
        if m[i][j] < 100:
            nuevo = m[i][j] * 1.08
        else:
            nuevo = m[i][j] * 1.05
        fila.append(round(nuevo,2))
    m_nueva.append(fila)

print("Matriz original: ")
for fila in m:
    print(fila)

print("Matriz nueva: ")
for fila in m_nueva:
    print(fila)
'''


#Cinco lotes tienen tres mediciones de calidad sobre 100
#por cada fila calcula el promedio y clasifica:
#-Aceptable 90 o mas
#-En observación 80 a menos de 90
#-Rechazado menos de 80
m = [
    [92,88,95],
    [75,82,79],
    [90,91,89],
    [68,74,77],
    [85,87,83]
    ]
m_nueva = []
for i in range(5):
    promedio = sum(m[i]) / len(m[i])
    if promedio >= 90:
        clasificacion = "Aceptable"
    elif promedio >= 80:
        clasificacion = "En observación"
    else:
        clasificacion = "Rechazado"
    m_nueva.append([promedio, clasificacion])
    print(f"Lote {i+1}: Promedio = {promedio:.2f} -  {clasificacion}")