import random

def obtener_apuesta(creditos):
    while True:
        try:
            apuesta = int(input(f"Tienes {creditos} Pesos. ¿Cuántos Pesos quieres apostar? "))
            if 0 < apuesta <= creditos:
                return apuesta
            else:
                print("Apuesta no válida. Debe ser un número positivo y no puedes apostar más dinero del que tienes.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def adivinar_numero(creditos):
    numero_secreto = random.randint(1, 10)
    intentos = 0
    apuesta = obtener_apuesta(creditos)
    
    print("Adivina el número entre 1 y 10.")
    
    while intentos < 3:
        try:
            intento = int(input("Tu intento: "))
            if intento < 1 or intento > 10:
                print("Número fuera de rango. Por favor, elige un número entre 1 y 10.")
                continue  # Esto hace que el intento sea inválido y no cuenta como un intento válido.
            intentos += 1
            if intento < numero_secreto:
                print("Más alto.")
            elif intento > numero_secreto:
                print("Más bajo.")
            else:
                print(f"¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")
                return apuesta * 2  # Duplica la apuesta si gana
            if intentos == 3:
                print("Perdiste, alcanzaste el maximo de intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    return -apuesta

def blackjack_simplificado(creditos):
    carta_jugador = random.randint(1, 10) + random.randint(1, 10)
    carta_casa = random.randint(1, 10) + random.randint(1, 10)
    apuesta = obtener_apuesta(creditos)
    
    print(f"Tus cartas suman {carta_jugador}. Las cartas de la casa suman {carta_casa}.")
    
    if carta_jugador > 21 or carta_jugador < carta_casa <= 21:
        print("La casa gana.")
        return -apuesta
    else:
        print("¡Ganaste!")
        return apuesta * 1.5  # Gana 1.5 veces su apuesta

def lanzamiento_moneda(creditos):
    resultado = random.choice(["aguila","sol"])
    apuesta = obtener_apuesta(creditos)
    eleccion = input("Elige Aguila o Sol: ").lower()
    
    if eleccion in ['aguila','águila','a','A','Aguila','Águila','AGUILA','ÁGUILA']: eleccion = 'aguila'
    elif eleccion in ['sol','s','SOL','Sol','S']: eleccion = 'sol'
    else: print ("Entrada no válida. Por favor elige 'Aguila' o 'Sol'. ")

    print(f"La moneda cayó en {resultado}.")
    
    if eleccion == resultado:
        print("¡Ganaste!")
        return apuesta * 2  # Duplica la apuesta si gana
    else:
        print("Perdiste.")
        return -apuesta

def main():
    creditos = 100  # Créditos iniciales
    juegos = {'1': adivinar_numero, '2': blackjack_simplificado, '3': lanzamiento_moneda}
    
    while creditos > 0:
        print("\nBienvenido al casino tercermundista")
        print("Elige un juego: \n1) Adivinar el número \n2) Blackjack \n3) Lanzamiento de moneda. \nEscribe 'salir' para terminar.")
        eleccion = input()
        
        if eleccion in juegos:
            resultado = juegos[eleccion](creditos)
            creditos += resultado
            print(f"Ahora tienes {creditos} Pesos.")
        elif eleccion.lower() == 'salir':
            break
        else:
            print("Opción no válida.")
    
    print("Juego terminado. Gracias por jugar.")

if __name__ == "__main__":
    main()