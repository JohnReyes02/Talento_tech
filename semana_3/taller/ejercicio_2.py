'''
Ejercicio 2

Escribe un programa que permita ingresar números de manera repetida.
El programa debe:

- Sumar solo los números positivos.
- Terminar cuando el usuario ingrese un número negativo.
- Al finalizar mostrar la suma total de los números positivos ingresados.

Pistas:

- Usa un ciclo while para seguir pidiendo números al usuario
- Usa un acumulador para sumar solo los números positivos.
'''
# %%
# Sin manejo de errores
numero = 1
suma_positivos = 0
while numero >= 0:
    numero = int(input('Ingresa un número: '))
    if numero >= 0:
        suma_positivos += numero

print(f'\nSuma total de los números positivos es: {suma_positivos}')

# %%
# Con manejo de errores
numero = 1
suma_positivos = 0
while numero >= 0:
    while True:
        try:
            numero = int(input('Ingresa un número: '))
            if numero >= 0:
                suma_positivos += numero
            break
        except ValueError:
            print('¡Entrada no válida. Ingrese un número entero')

print(f'\nSuma total de los números positivos es: {suma_positivos}')
