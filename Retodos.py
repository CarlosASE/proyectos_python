# Mensaje inicial
print("Se realizará el cálculo del promedio ponderado")

# Solicitar al usuario las tres calificaciones
calificacion1 = float(input("Ingrese la primera calificación (20%): "))
calificacion2 = float(input("Ingrese la segunda calificación (30%): "))
calificacion3 = float(input("Ingrese la tercera calificación (50%): "))

# Calcular el promedio ponderado
promedio_ponderado = (calificacion1 * 0.20) + (calificacion2 * 0.30) + (calificacion3 * 0.50)

# Mostrar la evaluación semestral
print(f"La evaluación semestral es: {promedio_ponderado}")