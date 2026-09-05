# Práctica Algoritmos genéticos: Optimización Combinatoria con Algoritmos Genéticos y Manejo de Restricciones
Este repositorio contiene la implementación en Python de diversas técnicas de representación genotípica, funciones de aptitud penalizadas y operadores genéticos aplicados a problemas de optimización combinatoria binaria basados en el Problema de la Mochila estipulado y explicado en clase el 03 de septiembre de 2026 en la Universidad de Cundinamarca Seccional Ubaté.
---
## Arquitecctura del proyecto práctico
### Estructura de entorno
Para mantener un entorno aislado y reproducible, el proyecto gestiona sus dependencias mediante `requirements.txt`:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar entorno virtual (Windows PowerShell)
.\venv\Scripts\Activate
# (En Linux/macOS: source venv/bin/activate)

# Instalar dependencias
pip install -r requirements.txt
```
## Módulos e Implementación Técnica
### 1. Ejercicio 1: Portafolio de Inversiones (Penalización Estricta)

- **Objetivo:** Maximizar el retorno económico esperable seleccionando un subconjunto de 10 proyectos potenciales sin exceder un presupuesto máximo de $100 USD.

- **Representación:** Vector binario $x \in \{0, 1\}^{10}$.

- **Mecanismo de penalización:** Penalización Estricta (Muerte Natural). Si el costo total supera el presupuesto, la aptitud se fuerza a $0$:

> $$f(x) = \begin{cases} \sum_{i=1}^{10} r_i \cdot x_i & \text{si } \sum_{i=1}^{10} c_i \cdot x_i \le 100 \\ 0 & \text{si } \sum_{i=1}^{10} c_i \cdot x_i > 100 \end{cases}$$.

### 2. Ejercicio 2: Selección de Personal (Restricción de Igualdad Cardinal)

- **Objetivo:** Maximizar la puntuación de habilidad técnica de un equipo de desarrollo conformado por 12 candidatos.

- **Restricción Dura:** El equipo debe contener exactamente $k = 5$ integrantes ($\sum x_i = 5$).

- **Mecanismo de Penalización:** Penalización Cuadrática Progresiva basada en la distancia euclidiana/desviación absoluta respecto al tamaño objetivo:

> $$f(x) = \max\left(0, \sum_{j=1}^{12} h_j \cdot x_j - \lambda \cdot \left\vert{} \sum_{j=1}^{12} x_j - 5 \right\vert{}^2\right)$$

Donde $\lambda = 100$ actúa como factor de escala de penalización.

### 3. Ejercicio 3: Operador de Cruzamiento de Dos Puntos (Two-Point Crossover)

- **Mecanismo:** Selección aleatoria de dos índices $p_1, p_2 \in [1, N-1]$ tales que $p_1 < p_2$. Los descendientes heredan los bloques genéticos laterales de un progenitor y reemplazan el segmento central $[p_1:p_2]$ con el del segundo progenitor.

- **Ventaja Teórica:** Minimiza el sesgo posicional (positional bias) inherente al cruzamiento de un solo punto, preservando esquemas o "bloques constructores" (building blocks) ubicados en los extremos del cromosoma.

## Análisis Comparativo de Resultados (Ejercicio 4)
El análisis experimental de la dinámicas poblacionales en el Ejercicio 1 revela patrones críticos sobre cómo las estrategias de penalización condicionan la exploración y explotación del espacio de búsqueda.
---
### 1. Impacto de la Penalización Estricta (Muerte Natural)

- **Morfología del Espacio de Aptitud:** Crea un "acantilado" en el paisaje de aptitud (fitness landscape). Las soluciones adyacentes a la frontera de factibilidad pasan de tener una aptitud alta a tener una aptitud de cero absoluto.

- **Presión de Selección Desmedida:** Al anular la aptitud de cualquier cromosoma que exceda el presupuesto por tan solo $1 USD, se eliminan genotipos no factibles de forma inmediata.

- **Pérdida de Información Genética:** Si un cromosoma inválido contenía un subconjunto de proyectos altamente eficiente (un bloque constructor clave), dicha información desaparece del fondo genético (gene pool).

- **Riesgo:** Genera una pérdida drástica de diversidad genotípica en las primeras generaciones, induciendo al algoritmo a una convergencia prematura hacia óptimos locales factibles pero mediocres.

### 2. Comportamiento frente a una Penalización Suave (Progresiva)

- **Morfología del Espacio de Aptitud:** Genera una pendiente de degradación donde la aptitud disminuye proporcionalmente a la gravedad del incumplimiento: $f(x) = \text{Retorno} - \alpha \cdot \max(0, \text{Costo} - \text{Presupuesto})$.

- **Efecto de "Sombra de Factibilidad":** Permite que soluciones ligeramente infactibles sobrevivan durante algunas generaciones con una aptitud relativa baja.

- **Evolución Guiada:** Estas soluciones "casi factibles" actúan como puentes genéticos. Al cruzarse mediante el operador de dos puntos o sufrir mutaciones puntuales, con frecuencia producen descendientes factibles ubicados en la frontera exacta de optimización global.

## Conclusiones Generales

1. **Eficiencia en la Exploración Binaria:** La codificación genotípica binaria resulta altamente eficiente para problemas de optimización combinatoria de decisiones discretas (tomar/dejar).

2. **Manejo de Restricciones:** En problemas fuertemente restringidos, la penalización progresiva o el diseño de operadores genéticos reparadores son superiores a la penalización estricta, pues esta última destruye la diversidad genética requerida por los algoritmos evolutivos.

3. **Preservación de Esquemas:** El cruzamiento de dos puntos demostró ser más flexible para mantener la cohesión de bloques constructores distantes en la cadena cromosómica, facilitando la convergencia hacia el óptimo global sin romper las combinaciones exitosas desarrolladas por los progenitores.le