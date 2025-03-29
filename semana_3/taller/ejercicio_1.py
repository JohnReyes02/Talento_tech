'''
Ejercicio 1: Contador de números pares e impares

Escribe un programa que pida al usuario una lista de 10 
números enteros. El programa debe:

• Contar cuántos de esos números son pares y cuántos son impares.
• Mostrar el número total de pares e impares.

Pistas:
• Usa un ciclo for para recorrer la lista de números.
• Usa un contador para contar pares e impares.
• Recuerda que un número es par si su resto al dividir entre 2 es 0 (es decir, numero % 2 == 0).
'''
# %%
pares = 0
impares = 0
for i in range(10):
    numero = int(input(f'Ingrese el número {i + 1}: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Total de números pares: {pares}')
print(f'Total de números impares: {impares}')
# %%
# Solución con manejo de errores
pares = 0
impares = 0
for i in range(10):
    while True:
        try:
            numero = int(input(f'Ingrese el número {i + 1}: '))
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            break
        except ValueError:
            print('¡Entrada no válida. Ingrese número entero!')

print(f'\nTotal de números pares: {pares}')
print(f'Total de números impares: {impares}')

# %%
