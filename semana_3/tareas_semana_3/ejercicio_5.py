'''
Ejercicio 5

Ejercicio: Adivina el número (con pistas)

Escribe un programa que:

1. Pida al usuario que adivine un número del 1 al 5.
2. El programa debe dar pistas de si el número es mayor o menor que el número
correcto.
3. Si el número adivinado es correcto, termina el ciclo y muestra un mensaje de
felicitación.
4. El programa permite un máximo de 3 intentos. Si no acierta en esos intentos,
termina el juego.

Este ejercicio utiliza while para los intentos, if para dar las pistas y un for
para contar los intentos.

1. while: El ciclo while se encarga de seguir pidiendo al usuario que adivine el
número mientras queden intentos. El ciclo que repite hasta que el usuario acierte
o se acaben los intentos.
2. if: Dentro del ciclo, usamos if para verificar si el número adivinado es el 
correcto. Dependiendo de la comparación, damos pistas (si el número es mayor o
menor fque el correcto).
3. Contador de intentos. Los intentos se cuentan usando la variable intentos. Se
decrementan en cada intento.
4. break: Si el usuario adivina el número correcto, usamos break para salir del 
ciclo
'''
# %%
# Importar librerías
import random
# Declaracion de constantes
MAX_INTENTOS = 3 # Define el número máximo de intentos como una constante
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 5

# %%
# Genera un entero aleatorio entre el minimo y el maximo
numero_a_adivinar = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

intentos_inicial = MAX_INTENTOS # Guarda el número de intentos iniciales
intentos = MAX_INTENTOS
# %%
while intentos > 0:
    try:
        numero = int(input(f'Adivina el número (entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}) solo tienes {intentos} intentos: '))

        if numero < NUMERO_MINIMO or numero > NUMERO_MAXIMO:
            print(f'El número debe estar entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}')
            continue # Vuelve al inicio del ciclo sin decrementar los intentos

        if numero > numero_a_adivinar:
            print(f'El número es menor que {numero}. Te quedan {intentos - 1} intentos.')
        elif numero < numero_a_adivinar:
            print(f'El número es mayor que {numero}. Te quedan {intentos - 1} intentos.')
        else:
            print(f"\n¡Felicidades! Adivinaste el número '{numero}'ß en {intentos_inicial - intentos + 1}' intentos.")
            break

        intentos -= 1
    
    except ValueError:
        print('Entrada inválida. Debes ingresar un número entero.')

else:
    print(f'\n¡Lo siento! No adivinaste el número correcto. El número era {numero_a_adivinar}.')



# %%
