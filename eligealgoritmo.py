objetivo = int(input('Ingresa un número: '))

# bifurcacion 

camino = int(input('Si quieres usar el algoritmo de aproximacion presiona 1, Si deseas usar busqueda binaria, presiona 2: '))

# Algoritmo de busqueda binaria

if camino == 2:
    objetivo
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo} alto = {alto} respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'la raiz cuadrada de {objetivo} es {respuesta}.')

# Algoritmo de busqueda por aproximación 

elif camino == 1:
    objetivo
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontró la raíz cuadrada de {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")

# Error en elección de algoritmo

else:
    print('No ingresaste una respuesta valida')