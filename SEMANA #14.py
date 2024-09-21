# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    # Retornar el monto del descuento
    return descuento

# Programa principal
# Primera llamada con el monto total (usa el valor predeterminado del porcentaje de descuento)
monto_total1 = 150.0
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1

# Segunda llamada con el monto total y un porcentaje de descuento específico
monto_total2 = 200.0
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2

# Mostrar resultados
print(f"Compra 1:")
print(f"Monto total: ${monto_total1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

print(f"Compra 2:")
print(f"Monto total: ${monto_total2:.2f}")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
