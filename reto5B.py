def calcular_pago_y_ahorro(precios):
    # Ordenar los precios de mayor a menor para maximizar el beneficio al cliente
    precios_ordenados = sorted(precios, reverse=True)
    monto_a_pagar = 0
    monto_ahorrado = 0
    
    # Calcular el monto a pagar y ahorrado por cada trío de artículos
    for i in range(0, len(precios_ordenados), 3):
        monto_a_pagar += precios_ordenados[i]  # Pagar el artículo más caro de cada trío
        monto_ahorrado += sum(precios_ordenados[i+1:i+3])  # Los dos más baratos son gratis
    
    return monto_a_pagar, monto_ahorrado

print("\n--- Sistema de Cálculo de Descuento Extendido ---")
print("\nPromoción: De cada tres artículos, paga solo el más caro. Máximo 12 artículos.")
print("Introduce los precios de los artículos (escribe 'fin' para terminar)")

# Solicitar al usuario que ingrese los precios de los artículos y manejar errores
precios = []
while True:
    entrada = input(f"Precio del Artículo {len(precios)+1} o 'fin': ")
    if entrada.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'
    try:
        precio = float(entrada)
        if precio < 0:
            print("Por favor, introduce un número positivo.")
        else:
            precios.append(precio)
            if len(precios) == 12:
                print("\nSe ha alcanzado el límite máximo de artículos.")
                break
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número válido.")

if len(precios) > 0:
    monto_a_pagar, monto_ahorrado = calcular_pago_y_ahorro(precios)
    print(f"Monto a pagar: {monto_a_pagar:.2f} Mxn")
    print(f"Monto ahorrado: {monto_ahorrado:.2f} Mxn")
else:
    print("No se introdujeron artículos.")