print("Evaluación Semestral")

def solicitar_calificacion(mensaje):
    while True:
        try:
            # Intenta convertir la entrada del usuario en un número flotante
            calificacion = float(input(mensaje))
            return calificacion
        except ValueError:
            # Imprime un mensaje de error si la entrada no es un número válido
            print("Ingresa un dígito válido.")

def solicitar_calificaciones():
    calificacion1 = solicitar_calificacion("Ingresa la primera calificación: ")
    calificacion2 = solicitar_calificacion("Ingresa la segunda calificación: ")
    calificacion3 = solicitar_calificacion("Ingresa la tercera calificación: ")
    return max(calificacion1, calificacion2, calificacion3)

evaluacion_semestral = solicitar_calificaciones()
print("La evaluación semestral es:", evaluacion_semestral)
