import numpy as np

# Datos de población (millones) y PIB (miles de millones de USD)
poblacion = np.array([9.2, 12.4, 15, 6.7, 7.4, 10.7, 6.8, 2.9, 2.5, 2.8, 5.2, 4.9, 3.5, 4.3, 2.9, 1.6, 3.9, 4.7, 2.7, 2.2, 3.4, 1.5, 1.1, 0.8, 1.5, 0.7, 1.6, 1.5, 1.3, 1, 1.8])
pib = np.array([411, 337, 112, 172, 95, 94, 166, 30, 40, 26, 50, 93, 44, 55, 42, 26, 34, 66, 57, 15, 30, 60, 20, 10, 12, 12, 14, 21, 18, 8, 45])

# Calcular promedio y desviación estándar
promedio_poblacion = np.mean(poblacion)
desviacion_poblacion = np.std(poblacion)

promedio_pib = np.mean(pib)
desviacion_pib = np.std(pib)

(promedio_poblacion, desviacion_poblacion, promedio_pib, desviacion_pib)
