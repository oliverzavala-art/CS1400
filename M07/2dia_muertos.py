#nombre: Oliver Zavala


# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

#4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
 # para imprimir una frase por cada ancestro.
#(Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").
for anscestro, platillo in altares_familiares.items():
    print(f"Para {anscestro} preparamos: {platillo}")

#5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.

print("Ancestros:")
for ancestro in altares_familiares.keys():
    print(ancestro)

print("Platillos:")
for platillo in altares_familiares.values():
    print(platillo)

#6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
#  convierte la lista flores_recibidas en un set usando la función set().
flores_recibidas = set(flores_recibidas)
print("Flores únicas recibidas:", flores_recibidas)

#7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron
 #en el conjunto? ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?
#respuesta: La lista original de flores tenía 6 elementos, mientras que el conjunto resultante tiene 3 elementos únicos. 
