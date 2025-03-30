# -*- coding: utf-8 -*-
"""
Este código fue creado por:
Maximo Romero Diaz
Propósito: Calcula el calibre real de un material con superficie arenosa
a partir de la resina aplicada y el gramaje.
Fecha de creación: [Fecha]
"""

import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.preprocessing import StandardScaler
#from colorama import Fore, Style, init # <-- Importante

# Inicializa colorama (esto es necesario en Windows)
#init(autoreset=True)

# Función para pedir datos al usuario
def obtener_datos_del_usuario():
    resina_aplicada = []
    gramaje = []
    calibre_real = []
    num_muestras = int(input("Ingrese el número de muestras: "))

    for i in range(num_muestras):
        while True:  # Bucle para permitir la corrección
            try:
                print(f"\nDatos para la Muestra {i+1}:")
                resina = float(input("  Resina Aplicada (g/m²): "))
                gram = float(input("  Gramaje (g/m²): "))
                calibre = float(input("  Calibre Real (micras): "))
                break  # Sale del bucle si los datos son válidos
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        resina_aplicada.append(resina)
        gramaje.append(gram)
        calibre_real.append(calibre)

    return np.array(resina_aplicada), np.array(gramaje), np.array(calibre_real)

# Función para revisar y corregir los datos
def revisar_y_corregir_datos(resina_aplicada, gramaje, calibre_real):
    while True:
        print("\nDatos Ingresados:")
        for i in range(len(resina_aplicada)):
            print(f"Muestra {i+1}: Resina = {resina_aplicada[i]:.2f}, Gramaje = {gramaje[i]:.2f}, Calibre Real = {calibre_real[i]:.2f}")

        opcion = input("¿Desea corregir algún dato? (s/n): ").lower()
        if opcion == 'n':
            return resina_aplicada, gramaje, calibre_real  # <-- Devolver los valores originales
            break  # Sale del bucle si no hay correcciones
        elif opcion == 's':
            try:
                indice = int(input("Ingrese el número de la muestra a corregir: ")) - 1
                if 0 <= indice < len(resina_aplicada):
                    while True:  # Bucle para corregir la muestra
                        try:
                            resina = float(input(f"  Nueva Resina Aplicada para la Muestra {indice+1} (g/m²): "))
                            gram = float(input(f"  Nuevo Gramaje para la Muestra {indice+1} (g/m²): "))
                            calibre = float(input(f"  Nuevo Calibre Real para la Muestra {indice+1} (micras): "))
                            resina_aplicada[indice] = resina
                            gramaje[indice] = gram
                            calibre_real[indice] = calibre
                            break  # Sale del bucle de corrección
                        except ValueError:
                            print("Error: Ingrese valores numéricos válidos.")
                else:
                    print("Error: Número de muestra inválido.")
            except ValueError:
                print("Error: Ingrese un número de muestra válido.")
        else:
            print("Error: Opción inválida. Ingrese 's' o 'n'.")

    return resina_aplicada, gramaje, calibre_real # si sale de la correción

# Datos de la densidad
densidad = float(input("Ingrese la Densidad del material base (g/micras*m²): "))

# Obtener datos del usuario
resina_aplicada, gramaje, calibre_real = obtener_datos_del_usuario()

# Revisar y corregir los datos
resina_aplicada, gramaje, calibre_real = revisar_y_corregir_datos(resina_aplicada, gramaje, calibre_real)

# Calcular el calibre base (esto ya no es crucial para la regresión, pero puede ser informativo)
calibre_base = gramaje / densidad

# Verificar que haya datos suficientes
if len(resina_aplicada) < 2:
    print("Se necesitan al menos dos muestras para realizar la regresión.")
    exit()

# # **Centrar y Escalar las Variables**
# scaler = StandardScaler() # <-- Crear el Scaler
# X = np.column_stack((resina_aplicada, gramaje)) # <-- Combinar las variables independientes
# X_escalado = scaler.fit_transform(X) # <-- Centrar y Escalar

# # Crear un objeto de regresión lineal
# modelo = LinearRegression()

# # Ajustar el modelo a los datos: ¡IMPORTANTE! Ahora usamos los datos escalados
# modelo.fit(X_escalado, calibre_real)

# # Obtener los coeficientes
# intercepto = modelo.intercept_
# pendiente_resina = modelo.coef_[0]
# pendiente_gramaje = modelo.coef_[1]

# # Imprimir la ecuación de regresión para el Calibre Real
# print("\nModelo para el Calibre Real (micras) - Variables Estandarizadas:")
# print(f"Calibre Real = {intercepto:.2f} + ({pendiente_resina:.2f} * Resina Aplicada_escalada) + ({pendiente_gramaje:.2f} * Gramaje_escalada)")

# # Calcular el R²
# y_predicciones = modelo.predict(X_escalado)
# r2 = r2_score(calibre_real, y_predicciones)

# # Imprimir el R²
# print(f"\nR² (Coeficiente de Determinación): {r2:.4f}")

# # Evaluar la bondad del ajuste del modelo
# if r2 > 0.8:
#     print("\nEl modelo tiene un buen ajuste a los datos.")
# elif r2 > 0.6:
#     print("\nEl modelo tiene un ajuste moderado a los datos.")
# else:
#     print("\nEl modelo no tiene un buen ajuste a los datos. Considera explorar otros modelos o variables.")

# # Predicción del Calibre Real
# resina_nueva = float(input("\nIngrese un valor de Resina Aplicada (g/m²) para predecir el Calibre Real: "))
# gramaje_nuevo = float(input("Ingrese el valor del Gramaje (g/m²) para predecir el Calibre Real: "))

# # **Escalar los Nuevos Datos**
# X_nuevo = np.array([[resina_nueva, gramaje_nuevo]])
# X_nuevo_escalado = scaler.transform(X_nuevo) # <-- Usar el scaler YA AJUSTADO

# calibre_real_predicho = modelo.predict(X_nuevo_escalado)[0]

# print(f"Calibre Real Predicho: {calibre_real_predicho:.2f} micras")

print("\n---")
print("Programa para el cálculo del Calibre Real")
print("Código creado por Maximo Romero Diaz")
print("---")

input("\nPresione Enter para salir...") # <-- Agregar esta línea
