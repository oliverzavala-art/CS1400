
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
"""
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




