'''
Ejercicio 4

Escribe un programa que pida tres números y luego calcule y 
muestre el promedio de esos números. La fórmula para calcular
el promedio es:

    promedio = (número 1 + número 2 + número 3) / 3

Instrucciones:

1. Pide al usuario que ingrese tres números.
2. Suma los tres números.
3. Divide la suma entre 3 para obtener el promedio.
4. Usa print() para mostrar el promedio.
'''

# %%
# Sin manejo de errores
suma = 0
for n in range(3):
    numero = float(input(f'Ingrese el número {n + 1} '))
    suma += numero

promedio = suma / 3
print(f'\nEl promedio de los números es {promedio:.1f}')

# %%
# Con manejo de errores
suma = 0
for n in range(3):
    while True:
        try:
            numero = float(input(f'Ingrese el número {n + 1} '))
            print(numero) # Para ir mostrando el número en pantalla
            suma += numero
            break
        except ValueError:
            print('¡Entrada no válida. Ingrese un número!')

promedio = suma / 3
print(f'\nEl promedio de los números es {promedio:.1f}')
# %%
