# Definimos los datos
ciudades = ["Quito", "Guayaquil", "Cuenca"]  # Dimensión 1: Ciudades
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado",
               "Domingo"]  # Dimensión 2: Días de la semana
semanas = 2  # Dimensión 3: Semanas

# Creamos una matriz 3D para las temperaturas
temperaturas = [
    [  # Datos de temperaturas para la ciudad de Quito
        [20, 22, 24, 21, 19, 18, 17],  # Semana 1
        [23, 25, 21, 22, 24, 20, 19]  # Semana 2
    ],
    [  # Datos de temperaturas para la ciudad de Guayaquil
        [30, 31, 32, 29, 30, 28, 27],  # Semana 1
        [33, 35, 32, 34, 31, 30, 29]  # Semana 2
    ],
    [  # Datos de temperaturas para la ciudad de Cuenca
        [15, 14, 16, 13, 12, 13, 11],  # Semana 1
        [17, 18, 16, 15, 14, 15, 13]  # Semana 2
    ]
]

# Calculamos y mostramos los promedios de temperatura para cada ciudad por semana
for i in range(len(ciudades)):  # Itera sobre las ciudades
    print(f"Promedios de temperatura para {ciudades[i]}:")
    for semana in range(semanas):  # Itera sobre las semanas
        # Sumamos las temperaturas de todos los días de la semana y calculamos el promedio
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):  # Itera sobre los días de la semana
            suma_temperaturas += temperaturas[i][semana][dia]

        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")


