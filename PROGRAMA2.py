# Definimos la matriz bidimensional (3x3)
matriz = [
    [5, 3, 8],
    [2, 7, 6],
    [9, 1, 4]
]

# Función para ordenar una fila específica de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitamos al usuario la fila que desea ordenar
fila_a_ordenar = int(input("Ingrese el número de la fila que desea ordenar (0, 1 o 2): "))

# Ordenamos la fila especificada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
