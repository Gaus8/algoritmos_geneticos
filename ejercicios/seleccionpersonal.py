import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
habilidades = np.array([85, 92, 78, 64, 90, 88, 75, 82, 95, 70, 80, 89])
TAMAÑO_EQUIPO = 5

def calcular_aptitud_personal(cromosoma, k=5, penalizacion_lambda=100):
    candidatos_seleccionados = np.sum(cromosoma)
    habilidad_total = np.sum(cromosoma * habilidades)
    
    # Penalización por desviación cuadrática del tamaño k
    desviacion = abs(candidatos_seleccionados - k)
    fitness = habilidad_total - (penalizacion_lambda * (desviacion ** 2))
    return max(0, fitness)

def graficar_ejercicio_2(n_muestras=1000):
    np.random.seed(42)
    poblacion = np.random.randint(0, 2, size=(n_muestras, 12))
    
    tamanos = poblacion.sum(axis=1)
    aptitudes = np.array([calcular_aptitud_personal(ind, k=TAMAÑO_EQUIPO) for ind in poblacion])

    plt.figure(figsize=(8, 4.5))
    plt.scatter(tamanos, aptitudes, color='purple', alpha=0.4, label='Soluciones Evaluadas')
    plt.axvline(x=TAMAÑO_EQUIPO, color='gold', linestyle='--', linewidth=2, label=f'Equipo Requerido (k={TAMAÑO_EQUIPO})')
    plt.title('Ejercicio 2: Selección de Personal (Penalización Cuadrática)')
    plt.xlabel('Candidatos Seleccionados (Bits encendidos)')
    plt.ylabel('Aptitud (Fitness)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Ejecución de evaluación y gráfica
cromosoma_valido = np.array([1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0])    # 5 integrantes
cromosoma_invalido = np.array([1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0])  # 6 integrantes

print(f"Fitness (5 candidatos): {calcular_aptitud_personal(cromosoma_valido)}")
print(f"Fitness (6 candidatos): {calcular_aptitud_personal(cromosoma_invalido)}")
graficar_ejercicio_2()