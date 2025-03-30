'''
Ejercicio 3

Escribe un programa que pida al usuario que ingrese un palabra. El programa debe:

- Contar cuantas vocales  (a, e, i , o, u) hay en la palabra.
- Mostrar el número total de vocales.

Pistas:

- Usa un ciclo for para recorrer cada letra de la palabra.
- Usa un contador para contar cuántas letras son vocales.
- Puedes comparar las letras con una cadena que contenga "aeiou"
'''
# %%
cuenta_vocales = 0
palabra = input('Ingresa una palabra: ')
for char in palabra:
    print(char)
    if char in 'aAeEiIoOuU': # Pregunta por las Mayúsculas y minúsculas
        cuenta_vocales += 1

print(f"La palabra '{palabra}' tiene {cuenta_vocales} vocal(es).'")
# %%
