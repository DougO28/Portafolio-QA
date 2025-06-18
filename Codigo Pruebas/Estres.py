import math

def calculate_heavy_load(iterations):
    """
   carga computacional intensiva realizando cálculos repetitivos.
    """
    result = 0
    for i in range(iterations):
        # Operaciones que consumen rendimiento CPU
        result += math.sqrt(i) * math.sin(i) / math.cos(i if i != 0 else 1)
        result = result % 1_000_000 # Colocar un número manejable


    return result

if __name__ == "__main__":
    print("Este es un programa de ejemplo para pruebas de estrés.")
    print("Puedes llamarlo desde otro script para aplicar carga.")
    # Ejemplo de cómo se usaría directamente
    # resultado = calculate_heavy_load(10_000_000)
    # print(f"Resultado de la carga: {resultado}")