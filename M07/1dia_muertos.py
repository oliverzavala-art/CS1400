#Nombre: Oliver Zavala

#Tarea 1: Preparando la Oferta (Listas y Tuplas)


# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)

ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]
# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)
NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")
# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

#Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#respuesta: Se imprime "Flor de cempasúchil" que es la segunda ofrenda en la lista.

#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 #.append("Incienso copal") y luego ordena la lista alfabéticamente usando
ofrendas.append("Incienso copal")  # Agregar un nuevo elemento a la lista

 #la función .sort().  ¿Qué notas del variable en linea #12?
ofrendas.sort()  # Ordenar la lista alfabéticamente

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
NIVELES_ALTAR[0] = "Gloria".
 #¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 #de tu lista junto co su número de posición en el altar.


 