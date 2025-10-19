#  Funciones Lambda y Expresiones Funcionales 

from functools import reduce

print("--- Demostración de Funciones Lambda en Python ---") 
# 1. Lambda simple para sumar dos números 
# Define una función lambda que toma dos argumentos (a, b) y devuelve su suma. 
suma = lambda a, b: a + b 
# Llama a la función lambda 'suma' con 5 y 3, e imprime el resultado. 
print(f"Suma de 5 y 3: {suma(5, 3)}")

# 2. Lambda con la función 'map()' 
# 'map()' aplica una función (aquí, una lambda para elevar al cuadrado) a cada ítem de una lista. 
numeros = [1, 2, 3, 4, 5] 
# Define una lambda que toma un número (x) y devuelve su cuadrado (x*x). 
# 'list()' convierte el iterador en una lista para imprimir. 
cuadrados = list(map(lambda x: x * x, numeros)) 
print(f"Cuadrados de {numeros}: {cuadrados}")

# 3. Lambda con la función 'filter()' 
# 'filter()' construye un iterador con los elementos de una lista para los que una función devuelve True.
# Define una lambda que toma un número (x) y devuelve True si es par (x % 2 == 0), False en caso contrario. 
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) 
print(f"Números pares de {numeros}: {numeros_pares}")

# 4. Lambda con la función 'sorted()' 
# Se puede proporcionar una función 'key' para personalizar el criterio de ordenación. 
personas = [{'nombre': 'Alice', 'edad': 30}, {'nombre': 'Bob', 'edad': 25}, {'nombre': 'Charlie', 'edad': 35}] 
# Define una lambda que toma un diccionario 'p' (persona) y devuelve el valor asociado a la clave 'edad'. 
personas_ordenadas_por_edad = sorted(personas, key=lambda p: p['edad']) 
print(f"Personas ordenadas por edad: {personas_ordenadas_por_edad}") 

# 5. Lambda con la función 'reduce()' 
# 'reduce()' aplica una función a los elementos de un iterable para reducirlo a un único valor. 
# Define una lambda que toma dos argumentos (acumulador y elemento) y devuelve su producto. 
producto_total = reduce(lambda acumulador, elemento: acumulador * elemento, numeros) 
print(f"Producto de todos los números en {numeros}: {producto_total}") 

print("--- Fin de la demostración de Funciones Lambda ---")