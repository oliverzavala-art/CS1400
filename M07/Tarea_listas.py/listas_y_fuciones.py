# Nombre: Oliver Zavala

"""
Guía de Práctica: Listas y Funciones en Python

Listas (Lists)

Agregar, reemplazar y eliminar elementos de una lista
Lee detenidamente el siguiente código y responde a las preguntas planteadas.
"""
#Python

# Manejo de textos y listas

mensaje = "bienvenido al curso de python"
comidas = ["tacos", "pizza", "hamburguesa"]

# Mostrar datos

#print(mensaje)
#print(comidas[0])
"""
Análisis inicial:
1. Ejecuta el código. ¿Cómo se muestra el texto de la variable mensaje en la consola?
Respuesta: Se muestra  el mesaje "bienvenido al curso de python" en minúsculas tal como está definido en la variable mensaje.

2. Observa la instrucción print(comidas[0]). ¿Qué comida se imprimió en pantalla y en qué posición de la lista se encuentra?
#Respuesta: Se imprimió "tacos" que se encuentra en la primera posición que es 0 de la lista comidas.

 Modificación 1: Métodos de cadenas (Strings)

Aplica el método .upper() a la variable mensaje para transformarla a mayúsculas. Puedes hacerlo directamente en el print() o asignándolo a una nueva variable:

"""
print(mensaje.upper())

#Python
# Ejemplo de modificación:

#print(mensaje.upper())

# 3. Ejecuta el programa modificado. ¿Qué cambio ocurrió en la salida del texto respecto al código original?
#Respuesta: El texto del mensaje se muestra en mayúsculas.

#Modificación 2: Acceso a elementos de una lista
#En Python, los índices de las listas comienzan a contar desde 0.

#4. Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
#print(comidas[1])
#Respuesta: Tuve que cambiar a 1 porque los índices comienzan desde 0, y por eso la segunda comida se encuentra en la posición 2 de la lista.

# 5. Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.
# Observa las opciones y complete las definiciones. Métodos disponibles: insert, append, remove, pop y clear.
comidas = ["sushi", "pupusas", "panes con pollo"]
print(comidas[1])

#6.¿Qué método elimina todos los elementos de la lista? RESPUESTA: __________
# Respuesta: clear()

#7.¿Qué método elimina un elemento de la lista por su valor de índice? RESPUESTA: __________
# Respuesta: pop()
#8.¿Qué método elimina un elemento de la lista usando el valor del elemento? RESPUESTA: __________
# Respuesta: remove()

#9.¿Qué método agrega un elemento al final de la lista? RESPUESTA: __________
# Respuesta: append()

#10.¿Qué método agrega un elemento en una ubicación específica? RESPUESTA: __________
# Respuesta: insert()

# DESAFÍO DE CÓDIGO 1:

#Python
playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:

# 2. Elimine el primer número de la lista (5) usando 'pop':

# 3. Use 'append' para agregar estas variables a sus listas:
#name = "Lucas" 
#num = 7

# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:

#Contadores e Iteradores (Counters and Iterators)
#Analiza la siguiente función que genera datos para los ejercicios:

#Python
#import random

#def Generate_Numbers():
    #numbers = []
    # i in range(20):
    #    num = random.randint(1, 50)
    #    numbers.append(num)
   # return numbers

# Llamada a la función
#mis_numeros = Generate_Numbers()
#¿Qué tipo de datos se está agregando a la lista numbers? RESPUESTA: __________

#¿Cuántos números se están agregando exactamente a la lista? RESPUESTA: __________

#¿Qué devuelve (return) la función al final de su ejecución? RESPUESTA: __________

#DESAFÍO DE CÓDIGO 2:

#Completa las funciones de análisis de datos:

#Python
#def Even_Numbers(lista_origen):
   # even = []
    # TODO: Itere la lista_origen y agregue a 'even' solo los números pares
    #return even

#def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
   # pass

#def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    # Ejemplo: [10, 7, 15] -> [3, 8]
    #pass
#Listas 2D (2D Lists)
#DESAFÍO DE CÓDIGO 3:

#Observa la siguiente matriz 2D que representa un tablero de Tic-Tac-Toe:

#Python
#tictactoe = [
 #   ["X", "X", "X"],
  #  ["-", "O", "-"],
   # ["O", "-", "-"]
#]

# Escriba el 'if' para detectar si la fila superior (índice 0) tiene tres "X":
# Pista: Debe revisar las posiciones [0][0], [0][1] y [0][2]
#¿Qué valor devolvería la instrucción tictactoe[1][1] en el tablero anterior? RESPUESTA: __________

#¿Para qué sirve un print() vacío que se coloca al final de un bucle que imprime una matriz? RESPUESTA: __________

#Elegir un tipo de presentación





