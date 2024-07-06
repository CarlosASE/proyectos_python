def calcular_pago_y_ahorro(precios):
    precios_ordenados = sorted(precios)
    monto_a_pagar = precios_ordenados[-1]
    monto_ahorrado = sum(precios_ordenados[:2])
    return monto_a_pagar, monto_ahorrado

print("\nIngresa tus 3 artículos")

# Solicitar al usuario que ingrese los precios de los artículos y manejar errores
precios = []
for i in range(1, 4):
    while True:
        try:
            precio = float(input(f"Precio del Artículo {i}: "))
            if precio < 0:
                # Manejar el caso de números negativos
                print("Por favor, introduce un número positivo.")
            else:
                precios.append(precio)
                break  # Salir del bucle si el precio es válido
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

monto_a_pagar, monto_ahorrado = calcular_pago_y_ahorro(precios)

print("\n--- Sistema de Cálculo de Descuento ---")
print(f"\nPrecio del Artículo 1: {precios[0]} Mxn")
print(f"Precio del Artículo 2: {precios[1]} Mxn")
print(f"Precio del Artículo 3: {precios[2]} Mxn")
print(f"\nMonto a pagar: {monto_a_pagar:.2f} Mxn")
print(f"Monto ahorrado: {monto_ahorrado:.2f} Mxn")