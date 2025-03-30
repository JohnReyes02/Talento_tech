# Programa para calcular promedio ponderado de las notas del reto
# Autor: Edwin Reyes
# 19-02-2025

# Datos de entrada
nombre = input("Ingrese el nombre del tripulante: ")
nota_reto_1 = float(input("Digite la nota del reto 1: "))
nota_reto_2 = float(input("Digite la nota del reto 2: "))
nota_reto_3 = float(input("Digite la nota del reto 3: "))
nota_reto_4 = float(input("Digite la nota del reto 4: "))
nota_reto_5 = float(input("Digite la nota del reto 5: "))
nota_reto_ingles = float(input("Digite la nota del reto Inglés: "))

# Proceso
nota_definitiva = 0.1 * nota_reto_1 + 0.1 * nota_reto_2 + 0.2 * nota_reto_3 + 0.2 * nota_reto_4 + 0.2 * nota_reto_5 + 0.2 * nota_reto_ingles

# Salida F-Strings
print(f"La nota definitiva de {nombre} es {nota_definitiva:.2f}") 
print(f"La nota definitiva de {nombre} es {nota_definitiva:.2f}") 

# Otra forma de imprimir
# print("2. La nota definitiva de " + nombre + "es " + str(nota_definitiva))

# Salida pantalla

#print("1. El alumno "+ nombre + " tuvo la nota en el reto 1 de "+ str(nota_reto_1))

# F-Strings
# f antes de las comillas
# las variables entre llaves {}
# print(f"2. El alumno {nombre} tuvo la nota en el reto 1 de {nota_reto_1}