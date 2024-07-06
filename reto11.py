def guess_number():
    low = 1
    high = 1000
    print("Piensa en un número del 1 al 1000. Yo trataré de adivinarlo.")

    yes_responses = {"sí", "si", "s", "S", "sip", "yes", "YES", "SI"}
    no_responses = {"no", "NO", "nel", "nou", "naa", "NOU"}

    while low <= high:
        mid = (low + high) // 2
        response = input(f"¿Es tu número {mid}? (sí/no): ").strip().lower()
        
        if response in yes_responses:
            print(f"¡Genial! He adivinado que tu número es {mid}.")
            return
        elif response in no_responses:
            higher = input(f"¿Es tu número mayor que {mid}? (sí/no): ").strip().lower()
            if higher in yes_responses:
                low = mid + 1
            elif higher in no_responses:
                high = mid - 1
            else:
                print("Por favor, responde solo con 'sí' o 'no'.")
        else:
            print("Por favor, responde solo con 'sí' o 'no'.")
    
    print("No he podido adivinar tu número. ¿Estás seguro de que estaba entre 1 y 1000?")

# Ejecuta el programa
guess_number()