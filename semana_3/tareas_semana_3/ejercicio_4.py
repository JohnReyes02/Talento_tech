'''
Ejercicio 4

Escriba un programa que pida al usuario tres números y luego calcule y muestre
el promedio de esos números. La fórmula para calcular el promedio es:

            Promedio = (número 1 + número 2 + número 3) / 3

Instrucciones:

1. Pida al usuario que ingrese tres números.
2. Suma los tres números.
3. Divide la suma entre 3 para obtener el promedio.
4. Usa print() para mostrar el promedio.
'''
# %%
# Sin manejo de errores
suma = 0
for n in range(3):
    nota = float(input(f'Ingrese la nota {n + 1}: '))
    suma += nota
promedio = suma / 3
print(f'\nEl promedio de las notas es {promedio:.1f}')
 # %%
# Con manejo de errores
suma = 0
for n in range(3):
    while True:
        try:
            nota = float(input(f'Ingrese la nota {n + 1}: '))
            suma += nota
            break
        except ValueError:
            print('Entrada no válida. Ingrese una nota')
promedio = suma / 3
print(f'\nEl promedio de las notas es {promedio:.1f}')