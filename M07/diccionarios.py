"""
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
"""
"""
import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = animalesRefugiados
animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
animalesRefugiados["gato"] -= 3
animalesRefugiados["Serpiente"] = 4
print(animalesRefugiados)
if animalesRefugiados["perro"] > 50:
    print("Lleno de perros")
    if "raton" not in  animalesRefugiados :
        print("No hay ratones")

refugioOriginal=copy.deepcopy(animalesRefugiados)
"""
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