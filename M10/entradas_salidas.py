# nombre : Oliver Zavala

#nombre de archivo: entradas_salidas.py
#objetivo: aprender a leer y escribir archivos de texto

# Para almacenar la lista
roster = []

# Cargar la lista desde el archivo
"""
try:
    archivoRoster = open('roster.txt', 'r')
    for line in archivoRoster:
        roster.append(line.strip())
    archivoRoster.close()
except FileNotFoundError:
    print('Creando archivo para la lista.')
    archivoRoster = open("roster.txt", "x")
    archivoRoster.close()

while True:
    print(f"\nLista: {roster}")
    print('1. Agregar Nombre\n2. Eliminar Nombre \n3. Salir')
    try:
        eleccion = int(input("Seleccion: "))
    except ValueError:
        break

    if eleccion == 1:
        toAdd = input('Nombre:')
        roster.append(toAdd)
    elif eleccion == 2:
        toRemove = input('Eliminar:')
        try:
            roster.remove(toRemove)
        except:
            print('Error al eliminar')
    else:
        break

# Guarda la lista en el archivo
try:     
    archivoRoster = open('roster.txt', 'w')
    for n in roster:         
        archivoRoster.write(n + '\n')
    archivoRoster.close()
except:
    print('Error al escribir.')
    
Preguntas de Comprensión (Parte 1)
¿Cómo se llama el archivo .txt que se crea en este programa?
Respuesta: El archivo se llama "roster.txt".

¿Qué objeto de Python se utiliza para leer el archivo?
Respuesta: El objeto de Python utilizado para leer el archivo es `open()`.

¿Cuál es el propósito del bucle while al leer el archivo?
Respuesta: El propósito del bucle while es recorrer cada línea del archivo y agregarla a la lista `roster`.

¿Qué sucede con los datos a medida que se leen del archivo?
Respuesta: Los datos se almacenan en la lista `roster`.

¿Qué representa la variable n?
Respuesta: La variable n representa cada nombre en la lista `roster`.

¿Qué debe hacerse siempre con un archivo después de terminar de acceder a él?
Respuesta: Se debe cerrar el archivo utilizando el método `close()`.

Parte 2: Formato JSON

JSON es el estándar para guardar objetos complejos como diccionarios.

Permite guardar listas anidadas.
Es el estándar de internet.
"""

import json

usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# GUARDAR
with open('datos.json', 'w') as f:
    json.dump(usuario, f, indent=4)

# LEER
with open('datos.json', 'r') as f:
    datos = json.load(f)
    print(f"Usuario: {datos['nombre']}")




# Preguntas Finales
# 7. ¿Qué hace la función json.dump()?
# Respuesta: La función json.dump() se utiliza para escribir un objeto de Python en un archivo en formato JSON.

# 8. ¿Cuál es la ventaja de usar with open(...) en lugar de .close()?
# Respuesta: La ventaja de usar with open(...) es que el archivo se cierra automáticamente al salir del bloque with, incluso si ocurre un error.
