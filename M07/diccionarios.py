# nombre:Oliver Zavala

# Diccionarios.
#Agregar, reemplazar y eliminar elementos de un diccionario

#Observa el segmento de código a continuación y luego responde las preguntas.

"""
1.  Observa el diccionario num_salon en el código de abajo. ¿Qué signo de puntuación separa la clave (key) del valor (value)?
 Respuesta: Dos puntos (:) separa la palabra clave del valor en un diccionario.

2. Nota la coma al final de cada par clave-valor. ¿Por qué crees que no hay una coma después de "Cruz"?
Respuesta: No hay una coma después de "Cruz" porque es el último par clave-valor en el diccionario. 

3. ¿Cuántos pares clave-valor hay inicialmente en el diccionario?
Respuesta: Inicialmente hay 6 pares clave-valor en el diccionario.

4. Ejecuta el programa. ¿Qué reporta la función len() como la longitud del diccionario?
Respuesta: La función len() reporta la longitud del diccionario como 6.

5. Agrega a "DeLeon" al diccionario asignándole el salón 147.
Respuesta: Se agrega "DeLeon" al diccionario con el número de salón 147 usando la sintaxis num_salon["DeLeon"] = 147.

6. Ejecuta el programa. ¿Cambia la longitud del diccionario al agregar a DeLeon?
Respuesta: Sí, la longitud del diccionario cambia a 7 después de agregar a DeLeon.

7. Observa la puntuación para agregar elementos adicionales al diccionario. Agrega un instructor adicional "Hernandez" con el número de salón 323. Asegúrate de usar los corchetes [] para agregar al instructor.
Respuesta: Se agrega "Hernandez" al diccionario con el número de salón 323 usando la sintaxis num_salon["Hernandez"] = 323. 

8. Ejecuta el programa. ¿Qué se imprime cuando se usa el método .get() al imprimir el instructor Valle? ¿La clave o el valor?
Respuesta: Cuando se usa el método .get() para imprimir el instructor Valle, se imprime el valor asociado a la clave "Valle", que es 216.

9. ¿Qué se imprime cuando usas los corchetes para imprimir los datos?
Respuesta: Cuando se usan los corchetes para imprimir los datos, se imprime el valor asociado a la clave especificada. Por ejemplo, num_salon["Murphy"] imprimirá 304.

10. ¿Ves alguna diferencia entre acceder a los datos usando los corchetes [] y el método .get()?
Respuesta: Sí, hay una diferencia. Usar los corchetes [] para acceder a un valor lanzará un error si la clave no existe en el diccionario, mientras que el método .get() devolverá None (o un valor predeterminado si se proporciona) si la clave no se encuentra.

11. Agrega una sentencia print para imprimir el número de salon de Murphy."""
#print(num_salon["Murphy"])  # Esto imprimirá 304, que es el número de salón de Murphy.

num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101,
}
len (num_salon)
print("La longitud es", len(num_salon))

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216
num_salon["DE leon"] = 147
num_salon["Hernandez"] = 323
print("La longitud ahora es ", len(num_salon))

print( num_salon.get("Valle") )
print( num_salon["Murphy"])


""" Copia Superficial vs. Copia Profunda
(Shallow VS Deep Copy)

Los siguientes pares clave-valor representan la cantidad de animales en un refugio. Practica observando y programando lo siguiente.

¿Cuántos perros hay en el refugio al principio?
Respuesta: Al principio hay 49 perros en el refugio.    

¿Cuántos perros se están agregando al refugio?
Respuesta: Se están agregando 2 perros al refugio.

Escribe la línea de código para eliminar 3 gatos del refugio.
Respuesta: la línea de código es: animalesRefugiados["gato"] -= 3   

Observa el código para agregar los hurones. ¿Cuántos se agregaron?
Respuesta: Se agregaron 2 hurones al refugio.

Escribe el código para agregar 4 serpientes al refugio.
Respuesta: la línea de código es: animalesRefugiados["Serpiente"] = 4

Escribe una sentencia if para imprimir "Lleno" si el número de perros es mayor a 50.
Respuesta: 
 if animalesRefugiados["perro"] > 50:
    print("Lleno")  

Escribe una sentencia if para imprimir "No Ratones" si "raton" no es una clave en el diccionario animalesRefugiados.
Respuesta:
 if "raton" not in animalesRefugiados: 
    print("No hay ratones")

Nota que la variable refugioOriginal es igual a la variable animalesRefugiados. ¿Es esta una copia superficial o profunda?
Respuesta: Es una copia superficial, ya que ambas variables apuntan al mismo diccionario en memoria.

Escribe el comando para mostrar los animales de refugioOriginal al final del segmento de código. ¿Muestra los animales originales?
Respuesta: El comando es: print(refugioOriginal).

Cambia refugioOriginal para que sea una copia profunda (deep copy) de animalesRefugiados (recuerda importar la librería copy). ¿Muestra los animales originales ahora?
Respuesta: Sí, al hacer una copia profunda, refugioOriginal contendrá los animales originales 
y no reflejará los cambios realizados en animalesRefugiados.

¿Qué diferencia notas entre una copia profunda y una copia superficial? 

Respuesta: La diferencia principal es que una copia superficial crea una nueva referencia al mismo objeto, 
por lo que los cambios en uno afectan al otro. En cambio, una copia profunda crea un nuevo objeto independiente, por lo que los cambios en uno no afectan al otro."""
import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = animalesRefugiados
animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
animalesRefugiados["gato"] -= 3
animalesRefugiados["Serpiente"] = 4
print(animalesRefugiados)
if animalesRefugiados["perro"] > 50:

    print("Lleno ")
    if "raton" not in  animalesRefugiados :
        print("No hay ratones")
print(refugioOriginal)

refugioOriginal=copy.deepcopy(animalesRefugiados)


"""  Uso de Diccionarios
El siguiente segmento de código contará cuántas veces aparece cada palabra en el texto dado.

1. Observa la variable listaNotas. ¿Es una lista o un diccionario?
Respuesta: listaNotas es una lista, ya que se crea a partir de la función split() aplicada a la cadena de texto notas.

2. ¿Qué hace la función split()? (Puedes consultar lecciones anteriores).
Respuesta: La función split() divide una cadena de texto en una lista de palabras, utilizando espacios como delimitadores por defecto.
3. Observa la variable notasDiccionario. ¿Está definida como una lista o un diccionario?

4. ¿Hay valores en el diccionario o está vacío?

5. Observa el bucle for. ¿Está iterando a través de la lista o del diccionario?

6. Dado que la primera puntuación en listaNotas es "A", ¿el código ejecutaría la sentencia if o la sentencia else dentro del bucle?

7. El comando es notasDiccionario[i] = 1, cuando i es igual al texto "A", ¿cuál es el par clave-valor que se agrega al diccionario?

8. La calificación "A" se agrega varias veces. La primera vez, pasa por el if. La segunda vez, pasará por el comando else. Hablando de esa segunda vez cuando i = "A", el par clave-valor es inicialmente "A": 1, ¿a qué valor se actualiza cuando se ejecuta el comando notasDiccionario[i] += 1?

9. Ejecuta el programa, ¿cuántas veces aparece la calificación "A" en los puntajes?"""
# Ejemplo de conteo de palabras
text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy"

lst = text.split()  #esta función separa el texto en palabras y las guarda en una lista
plbList = dict() # esta línea crea un diccionario vacío 
for x in lst: # recorre la lista de palabras
    if x not in plbList: # si la palabra no está en el diccionario, la agrega con valor 1
        plbList[x] = 1 # esta función agrega la palabra al diccionario con valor 1
    else:
        plbList[x] += 1 # si la palabra ya está en el diccionario, incrementa su valor en 1

for i in plbList: # recorre el diccionario y muestra la palabra y su cantidad de apariciones
    print (i, plbList[i]) # esta línea imprime la palabra y su cantidad de apariciones en el texto

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict() 

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1 
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])