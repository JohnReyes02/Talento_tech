'''
Ejercicio 3

Escribe un programa que pida al usuario que ingrese una palabra. El programa
debe:

- Contar cuántas vocales (a, e, i, o, u) hay en la palabra.
- Mostrar el número total de vocales.

Pistas:

- Usar un ciclo for para recorrer cada letra de la palabra.
- Usa un contador para contar cuántas letras son vocales.
- Puedes comparar las letrar con una cadena que contenga "aeiou".


'''
# %%
# Sin manejo de errores
cuenta_vocales = 0
# pasa a minúscula todas las letras
palabra = input('Ingresa una palabra: ').lower()
for char in palabra:
    if char in 'aeiou':
        cuenta_vocales += 1

print(f"\nLa palabra '{palabra}' tiene {cuenta_vocales} vocal(es)")
