
#Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
#Analiza el siguiente código para comprender la necesidad de los bucles.
#Código 1:
"""
#Python
# Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")

#Análisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
# El problema es que tendrías que escribir 100 veces la misma línea de código, lo cual es tedioso y propenso a errores.

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
# No, porque cada saludo está escrito de manera fija en el código. Para cambiar el número de saludos, tendrías que modificar manualmente cada línea, lo cual no es eficiente ni práctico.

# Sección 2: Bucle while (Iteración Indefinida)

# Analiza cómo la estructura condicional if difiere del bucle while.

#Código 2:

#Python
# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

#Análisis:
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.
# Con el if no preguntó una tercera vez porque el bloque dentro del if solo se ejecuta una vez. 

#Modificación 1A (Cambio a while):
#Sustituye la palabra if por la palabra while en el código anterior y ejecútalo de nuevo.

#Código 2 modificado a while:

#Python
respuesta = input("¿Deseas repetir el proceso? (si/no): ")
while respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")
# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
# Con el while, el programa seguirá preguntando y ejecutando el bloque tantas veces como el usuario ingrese "si", a diferencia del if que solo lo hace una vez.

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
# no, porque la cantidad de veces que el usuario escribe "si" depende de su decisión en tiempo de ejecución.

#Modificación 1B (Bucle Infinito):
#Comenta la línea respuesta = input(...) que está dentro del bloque while. Ejecuta el programa e introduce "si".
#Python
respuesta = input("¿Deseas repetir el proceso? (si/no): ")
while respuesta == "si":
    print("Ejecutando el bloque...")

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
# El programa entrará en un bucle infinito, ya que la condición del while nunca cambiará y el bloque dentro del while se ejecutará repetidamente sin fin.

# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
# La combinación de teclas utilizada en la terminal para detener un bucle infinito en ejecución es Ctrl+C (o Cmd + C en macOS )

#Sección 3: Bucle for y la Función range() (Iteración Definida)
#Usamos for cuando queremos iterar sobre un número conocido de repeticiones o sobre una secuencia.

# Codigo 3:

#Python
# Ejemplo de range() simple
num = int(input("Introduce un número límite: "))

for i in range(10):
    print("Iteración:", i)

#Análisis:
# 8. Ejecuta el programa e ingresa el valor 10. ¿Cuántas veces se imprimió la palabra "Iteración"? ¿Influyó en algo el número ingresado por teclado en este primer intento?
# La palabra "Iteración" se imprimió 10 veces, ya que el bucle for se ejecuta 10 veces (de 0 a 9). El número ingresado por teclado no se ejecutó en este primer intento.

# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?
# El valor inicial de i es 0 y el valor final  es 9.

## 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().
# No, el número 10 no se imprimió en la consola. Python excluye el límite superior en range() porque la función genera una secuencia de números que comienza desde 0 y termina justo antes del número especificado.

# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?
#python
num = int(input("Introduce un número límite: "))
for i in range(0, 10):
    print("Iteración:", i)

# La salida será la misma que con range(10), ya que range(0, 10) genera los mismos números de 0 a 9.

#Modificación 2A (Rango con Variable Límite):
#Cambia la línea del rango para usar la variable num: range(1, num).

for i in range(1, num):
    print("Iteración:", i)

# 12. Ejecuta e ingresa 20. ¿El conteo se detuvo en 20 o en 19?
# El conteo se detuvo en 19.

# 13. ¿Qué ajuste matemático debes hacer dentro de range() para que la cuenta incluya exactamente el número ingresado por el usuario?
#Respuesta: range(1, num + 1)
for i in range(1, num + 1):
    print("Iteración:", i)  

#Modificación 2B (Uso del Argumento Step / Paso):
# Modifica la línea a: range(2, 11, 2)
 #Python
for i in range(2, 11, 2):
    print("Iteración:", i)

## 14. Ejecuta el programa. ¿Qué valores se imprimieron y qué función cumple el tercer argumento dentro de range(inicio, fin, paso)?
# Los valores imprimidos son 2, 4, 6, 8 y 10.
# El tercer argumento dentro de range(inicio, fin, paso) especifica el incremento entre cada número consecutivo. En este caso, el paso es 2, por lo que los números se imprimen con un incremento de 2.

#Sección 4: Iteración sobre Secuencias (Cadenas y Listas)
#Un bucle for permite iterar directamente sobre los elementos de una colección sin necesidad de usar contadores manualmente.

#código 4: 
# Python
# Iteración sobre una cadena de texto
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

   # Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta) 

#Análisis:

# 15. En el primer bucle for letra in palabra:, ¿qué representa la variable letra en cada paso del bucle?
# La variable letra representa cada carácter individual de la palabra "Python".
# En el segundo bucle for fruta in frutas:, la variable fruta representa cada elemento de la lista "frutas" en cada paso del bucle.

## 16. En el segundo bucle for fruta in frutas:, contrasta la iteración directa (for fruta in frutas:) con el acceso por índices (for i in range(len(frutas)):). ¿Cuál de las dos opciones resulta más legible para un principiante y por qué?
# La iteración directa (for fruta in frutas:) es más legible para un principiante, ya que permite acceder directamente a cada elemento de la lista sin necesidad de manejar índices manualmente.

#Sección 5: Sentencias de Control de Bucles (break y continue)
#Podemos alterar el flujo normal de un bucle mediante instrucciones de control.
"""
#Codigo 5
# Python
# Uso de break y continue
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)

#Análisis:
## 17. Observa la salida de la Demostración de continue. ¿Qué número falta en la secuencia impresa y por qué ocurrió esto?
# El número 3 falta en la secuencia impresa porque la instrucción continue hace que el bucle salte a la siguiente iteración sin ejecutar el resto del código.

## 18. Observa la salida de la Demostración de break. ¿Qué números se imprimieron y qué hace la instrucción break al ejecutarse?
# Los números impresos son 1 y 2. La instrucción break termina la ejecución del bucle por completo, sin procesar el resto.

# 19. Supón que construyes un bucle while True: para solicitar claves de acceso. ¿Qué sentencia te permitiría salir del bucle una vez que el usuario ingrese la clave correcta?

    clave = input("Ingrese la clave de acceso: ")
    if clave == "clave_correcta":
        break
    print("Clave incorrecta, inténtelo de nuevo.")
print("Acceso concedido.")

#Sección 6: Patrones de Acumulación y Conteo

#Un patrón común en programación consiste en acumular valores o contar ocurrencias a medida que iteramos.
#codigo 6
 # Python
 # Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)

# Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)

#   Análisis:
# 20. ¿Con qué valor deben inicializarse las variables suma_total y mayores_a_cinco antes de comenzar el bucle? ¿Qué pasaría si las inicializas dentro del bucle?
# Las variables suma_total y mayores_a_cinco deben inicializarse en 0 antes de comenzar el bucle. Si se inicializan dentro del bucle, cada iteración reiniciará los valores, 
# lo que provocará que la suma y el contador no acumulen correctamente los valores.