import hashlib

# Función que calcula el hash SHA-256 de una cadena
def hash_func(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Función que ordena los datos según sus hashes
def sort_data_using_hash(data_list):
    # Crea un diccionario donde las claves son los hashes y los valores son los datos originales
    hash_dict = {hash_func(data): data for data in data_list}
    # Ordena el diccionario por clave (hash) y devuelve los valores ordenados
    sorted_data = [value for key, value in sorted(hash_dict.items())]
    return sorted_data

# Pedir datos al usuario y guardarlos en una lista
data_list = []
print("Introduce los datos (escribe 'fin' para terminar):")
while True:
    dato = input("Dato: ")
    if dato.lower() == 'fin':
        break
    data_list.append(dato)

# Ordenar los datos usando sus hashes
datos_ordenados = sort_data_using_hash(data_list)
print(f"Datos ordenados: {datos_ordenados}")