'''
Ejercicio 2:

Program que permita al usuario ingresar números de manera repetida. El programa debe:
- Sumar solo los números positivos
- Terminar cuando el usuario ingrese un número negativo.
- Al finalizar, mostrar la suma total de los números positivos ingresados

Pistas:
- Usa un ciclo while para seguie pidiendo números al usuario.
- Usa un acumulador para sumar solo los números positivos.
'''
# %%
# Sin manejo de errores
suma = 0
while True:
    numero = int(input('Ingrese un número: '))
    if numero >= 0:
        suma += numero
    else:
        break

print(f'La Suma total de los números positivos fue: {suma}')
# %%
# Con Manejo de errores
suma = 0
while True:
    try:
        numero = int(input('Ingrese un número: '))
        if numero >= 0:
            suma += numero
        else:
            break
    except ValueError:
        print('Entrada no válida. Ingrese un número entero.')

print(f'La Suma total de los números positivos fue: {suma}')