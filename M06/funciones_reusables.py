# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
# respuesta: La variable "nombre"  se llama "parámetro" de la función.

# 2. ¿Qué le falta al código para ser completamente reutilizable?
# respuesta:le falta la palabrra clave "def" para definir la función. Para que sea reusable.

# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    return numero % 2 == 0

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# respuesta: la palabra clave es "def".

# 4. Escribe los nombres de las dos funciones definidas arriba.
# respesta: la primera se llama calcular_descuento y la segunda se llama es_par

# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# respuesta: como no indica el porcentaje, se utiliza el valor por defecto de 10%.  
# En este caso, el precio final será 90.0.

# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# La función aplica un descuento del 20% al precio de 200.y
# El descuento es 40 y la función devuelve 160.0

# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# 9. Cambia las funciones para que acepten decimales en el precio.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# respuesta :Se guarda None, porque mostrar_bienvenida() muestra el saludo con print, pero no devuelve un valor con return.

# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# respuesta: Porque return entrega el resultado de la función para que podamos guardarlo en una variable.

# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# respuesta : Si no has creado otra variable llamada descuento fuera de la función, muestra:
# NameError: name 'descuento' is not defined

# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# respuesta :Porque es una variable local: se crea dentro de calcular_descuento() y solo se puede usar dentro de esa función.

# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# respuesta: Si cambias 'return precio_final' por 'print(precio_final)', la función ya no devuelve un valor, por lo que al intentar sumar 'compra_1 + 5'
#  obtendrás un error del tipo TypeError, porque no puedes sumar None con un número.

# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# respuesta :  Puedes llamar a la función usando el nombre del parámetro, por ejemplo:
# calcular_descuento(200, porcentaje=20)

# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
# respuesta :Un docstring es un texto entre comillas triples que va al principio de la función y explica qué hace. 
# Aunque se parece a un comentario, es una cadena de documentación.