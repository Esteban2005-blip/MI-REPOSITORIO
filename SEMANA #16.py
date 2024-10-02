# Escritura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo de escritura ('w')
# Esto creará el archivo si no existe o lo sobreescribirá si ya existe.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Aprender Python es muy útil.\n")
    file.write("Me gusta practicar nuevas habilidades.\n")
    file.write("Leer y escribir archivos es fácil con Python.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el archivo línea por línea utilizando un bucle
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Usamos strip() para eliminar los saltos de línea adicionales

# El archivo se cierra automáticamente al salir de los bloques 'with'
