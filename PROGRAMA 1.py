# Definimos la matriz bidimensional (3x3)
matriz = [
    [5, 3, 8],
    [2, 7, 6],
    [9, 1, 4]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Solicitamos al usuario el valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Llamamos a la función y mostramos el resultado
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)
