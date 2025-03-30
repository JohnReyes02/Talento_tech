'''
Ejercicio 1
Contador de números pares e impares
Escribe un programa que pida al usuario una lista de 10 números enteros. El programa debe:

• Contar cuántos de esos números son pares y cuántos son impares.
• Mostrar el número total de pares e impares.

Pistas:
• Usa un ciclo for para recorrer la lista de números.
• Usa un contador para contar pares e impares.
• Recuerda que un número es par si su resto al dividir entre 2 es 0 (es decir, numero % 2 == 0).
'''
# Se valida el error si el usuario digita un valor diferente a un entero positivo
while True:
    try:
        cantidad_de_mumeros = int(input('Ingrese la cantidad de números a contar: '))
        if cantidad_de_mumeros <= 0:
            print('Por favor, ingrese un número mayor que 0.')
            continue
        break
    except ValueError:
        print('Entrada no válida. Ingrese un número entero positivo.')

# 
pares = 0
impares = 0
for i in range(cantidad_de_mumeros):
    while True:
        try:
            numero = int(input(f'Ingrese el número {i + 1}: '))
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            break
        except ValueError:
            print('Entrada no válida. Ingrese un número entero.')

# Salida
print(f'\nNúmeros pares: {pares}')
print(f'Números impares: {impares}')

