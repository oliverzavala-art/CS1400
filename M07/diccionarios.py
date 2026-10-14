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

