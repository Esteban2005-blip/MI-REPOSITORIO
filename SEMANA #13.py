def calcular_promedio_temperatura(ciudades_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde la clave es el nombre de la ciudad y el valor es
                                  una lista de listas con las temperaturas de cada semana.

    Retorna:
    dict: Un diccionario con el nombre de la ciudad y su temperatura promedio.
    """
    promedios = {}

    for ciudad, semanas in ciudades_temperaturas.items():
        total_temperaturas = 0
        total_dias = 0

        for semana in semanas:
            total_temperaturas += sum(semana)
            total_dias += len(semana)

        promedio = total_temperaturas / total_dias
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso:
ciudades_temperaturas = {
    "Ciudad A": [[30, 32, 31], [29, 28, 30], [31, 32, 33], [30, 29, 28]],
    "Ciudad B": [[22, 24, 23], [25, 24, 26], [27, 26, 25], [24, 23, 22]],
    "Ciudad C": [[15, 17, 16], [14, 15, 16], [16, 17, 18], [15, 14, 16]]
}

promedios = calcular_promedio_temperatura(ciudades_temperaturas)
print(promedios)
