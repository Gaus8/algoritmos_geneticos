import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
costos = np.array([15, 20, 30, 40, 25, 10, 35, 50, 18, 22])
retornos = np.array([35, 45, 70, 90, 55, 20, 80, 110, 40, 50])
presupuesto_max = 100

def decodificar_portafolio(cromosoma):
    costo_total = np.sum(cromosoma * costos)
    retorno_total = np.sum(cromosoma * retornos)
    return costo_total, retorno_total

def calcular_aptitud_portafolio(cromosoma, presupuesto):
    costo, retorno = decodificar_portafolio(cromosoma)
    # Penalización estricta: si excede el presupuesto, la aptitud es 0
    return 0 if costo > presupuesto else retorno

def graficar_ejercicio_1(n_muestras=300):
    np.random.seed(42)
    poblacion = np.random.randint(0, 2, size=(n_muestras, 10))
    
    costos_tot = np.array([decodificar_portafolio(ind)[0] for ind in poblacion])
    aptitudes = np.array([calcular_aptitud_portafolio(ind, presupuesto_max) for ind in poblacion])
    factibles = costos_tot <= presupuesto_max

    plt.figure(figsize=(8, 4.5))
    plt.scatter(costos_tot[factibles], aptitudes[factibles], color='forestgreen', alpha=0.7, label='Factibles (Costo ≤ 100)')
    plt.scatter(costos_tot[~factibles], aptitudes[~factibles], color='crimson', alpha=0.4, label='Penalizados (Fitness = 0)')
    plt.axvline(x=presupuesto_max, color='black', linestyle='--', label='Límite Presupuesto ($100)')
    plt.title('Ejercicio 1: Portafolio de Inversiones (Penalización Estricta)')
    plt.xlabel('Costo Total ($)')
    plt.ylabel('Aptitud (Fitness)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Ejecución de evaluación y gráfica
cromosoma_ejemplo = np.array([1, 1, 1, 0, 1, 0, 0, 0, 1, 0])
costo, retorno = decodificar_portafolio(cromosoma_ejemplo)
fitness = calcular_aptitud_portafolio(cromosoma_ejemplo, presupuesto_max)

print(f"Costo: ${costo} | Retorno: ${retorno} | Fitness: {fitness}")
graficar_ejercicio_1()