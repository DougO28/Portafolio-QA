import math
import time
import argparse
import threading
import os


def calculate_heavy_load(iterations, thread_id=0):
    """
    Realiza una carga computacional intensiva con operaciones matemáticas pesadas.
    """
    result = 0.0
    for i in range(1, iterations):  # comenzamos desde 1 para evitar division por cero
        try:
            calc = math.sqrt(i) * math.sin(i) / math.cos(i)
            result += calc
            result = result % 1_000_000  # mantener numero manejable
        except Exception as e:
            print(f"[Hilo {thread_id}] Error en la iteración {i}: {e}")
    print(f"[Hilo {thread_id}] Finalizó con resultado: {result}")
    return result


def run_stress_test(iterations, threads):
    """
    Ejecuta la carga con múltiples si los especificamos
    """
    start_time = time.time()
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=calculate_heavy_load, args=(iterations, t))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    end_time = time.time()
    print(f"\n Prueba de estres finalizada en {end_time - start_time:.2f} segundos usando {threads} hilo(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa de prueba de estres CPU.")
    parser.add_argument("-i", "--iterations", type=int, default=10_000_000,
                        help="Cantidad de iteraciones por hilo (default: 10,000,000)")
    parser.add_argument("-t", "--threads", type=int, default=1,
                        help="Cantidad de hilos para simular carga concurrente (default: 1)")

    args = parser.parse_args()

    print(f"\n Iniciando prueba de estres con {args.threads} hilo(s) y {args.iterations} iteraciones por hilo.")
    run_stress_test(args.iterations, args.threads)
