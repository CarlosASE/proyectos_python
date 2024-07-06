import random
import time

def quick_sort(array, stats):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()  # Tomamos el último elemento como pivote
        greater, lesser = [], []
        for element in array:
            stats['comparisons'] += 1  # Contar cada comparación
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        
        # Contar los intercambios al concatenar sublistas y pivot
        sorted_greater = quick_sort(greater, stats)
        sorted_lesser = quick_sort(lesser, stats)
        result = sorted_greater + [pivot] + sorted_lesser
        stats['swaps'] += len(result) - 1
        return result

def validate_input(prompt, is_float=False):
    while True:
        input_value = input(prompt)
        try:
            if is_float:  # Si el dato esperado debe ser flotante
                value = float(input_value.replace(',', ''))
            else:
                value = int(input_value.replace(',', ''))
            return value
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

def main():
    n = validate_input("Ingrese el número de elementos: ")
    min_value = validate_input("Ingrese el valor mínimo para los elementos generados: ", is_float=True)
    max_value = validate_input("Ingrese el valor máximo para los elementos generados: ", is_float=True)
    if min_value >= max_value:
        print("El valor mínimo debe ser menor que el valor máximo.")
        return
    
    data = [random.uniform(min_value, max_value) for _ in range(n)]
    stats = {'swaps': 0, 'comparisons': 0}
    
    start_time = time.time()  # Captura el tiempo de inicio
    sorted_data = quick_sort(data, stats)  # Ordenamos los datos
    elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
    
    print(f"\nTiempo transcurrido para ordenar {n} elementos: {elapsed_time:.6f} segundos.")
    print(f"Total de intercambios: {stats['swaps']}")
    print(f"Total de comparaciones: {stats['comparisons']}")

if __name__ == "__main__":
    main()