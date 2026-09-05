import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# EJERCICIO 3: OPERADOR DE CRUZAMIENTO DE 2 PUNTOS
# ==========================================

def cruzamiento_dos_puntos(padre1, padre2):
    longitud = len(padre1)
    
    # 1. Seleccionar dos índices aleatorios únicos y ordenarlos (p1 < p2)
    p1, p2 = map(int, sorted(np.random.choice(range(1, longitud), size=2, replace=False)))    
    # 2. Copiar los genotipos originales
    hijo1 = np.copy(padre1)
    hijo2 = np.copy(padre2)
    
    # 3. Intercambiar el segmento central
    hijo1[p1:p2] = padre2[p1:p2]
    hijo2[p1:p2] = padre1[p1:p2]
    
    return hijo1, hijo2, (p1, p2)


def graficar_cruzamiento(padre1, padre2, hijo1, hijo2, puntos):
    p1, p2 = puntos
    matriz = np.vstack([padre1, padre2, hijo1, hijo2])

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.matshow(matriz, cmap='Blues', vmin=-0.2, vmax=1.2)

    # Configuración de ejes y etiquetas
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(['Padre 1', 'Padre 2', 'Hijo 1', 'Hijo 2'], fontsize=11, fontweight='bold')
    ax.set_xticks(range(len(padre1)))
    ax.set_xticklabels([f'Bit {i}' for i in range(len(padre1))])

    # Dibujar líneas discontinuas en los dos puntos de corte
    ax.axvline(x=p1 - 0.5, color='red', linestyle='--', linewidth=2.5, label=f'Corte 1 (p1={p1})')
    ax.axvline(x=p2 - 0.5, color='crimson', linestyle='--', linewidth=2.5, label=f'Corte 2 (p2={p2})')

    # Superponer el valor de cada bit dentro de su respectiva casilla
    for i in range(4):
        for j in range(len(padre1)):
            val = matriz[i, j]
            color_texto = 'white' if val == 1 else 'black'
            ax.text(j, i, str(val), ha='center', va='center', color=color_texto, fontsize=12, fontweight='bold')

    plt.title(f'Ejercicio 3: Cruzamiento de Dos Puntos [Cortes en {p1} y {p2}]', fontsize=12, pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0))
    plt.grid(False)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    np.random.seed(42) # Semilla para reproducibilidad
    
    # 1. Definición de dos padres con cadenas binarias contrastantes
    padre1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    padre2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # 2. Aplicación del operador de cruzamiento de 2 puntos
    hijo1, hijo2, puntos = cruzamiento_dos_puntos(padre1, padre2)

    print("=== RESULTADOS DEL EJERCICIO 3 ===")
    print(f"Puntos de corte aleatorios seleccionados: {puntos}")
    print(f"Padre 1 : {padre1}")
    print(f"Padre 2 : {padre2}")
    print("-" * 40)
    print(f"Hijo 1  : {hijo1}  (Recibe extremos de P1 y centro de P2)")
    print(f"Hijo 2  : {hijo2}  (Recibe extremos de P2 y centro de P1)")

    # 3. Generar la gráfica del cruzamiento
    graficar_cruzamiento(padre1, padre2, hijo1, hijo2, puntos)