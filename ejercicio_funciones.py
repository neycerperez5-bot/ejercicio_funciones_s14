# Ejercicio Semana 14
# Funciones con parámetros y retorno de valores

def calcular_total(precio, cantidad, descuento):
    """
    Calcula el valor final de una compra aplicando descuento.

    Parámetros:
    precio: valor unitario del producto
    cantidad: número de productos comprados
    descuento: porcentaje de descuento aplicado

    Retorna:
    total_final: valor total de la compra
    """

    subtotal = precio * cantidad
    valor_descuento = subtotal * (descuento / 100)
    total_final = subtotal - valor_descuento

    return total_final


# Programa principal

print("=== Calculadora de compra ===")

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad comprada: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

resultado = calcular_total(precio, cantidad, descuento)

print("\nResumen de compra")
print("-------------------------")
print(f"Subtotal: ${precio * cantidad:.2f}")
print(f"Descuento aplicado: {descuento}%")
print(f"Total a pagar: ${resultado:.2f}")
