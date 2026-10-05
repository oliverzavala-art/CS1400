
#Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
#Analiza el siguiente código para comprender la necesidad de los bucles.
#Código 1:

# Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")

# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
# El problema es que tendrías que escribir 100 veces la misma línea de código, lo cual es tedioso y propenso a errores.

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
# No, porque cada saludo está escrito de manera fija en el código. Para cambiar el número de saludos, tendrías que modificar manualmente cada línea, lo cual no es eficiente ni práctico.

# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.
# Con el if no preguntó una tercera vez porque el bloque dentro del if solo se ejecuta una vez. 

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
# No, porque la cantidad de veces que el usuario escribe "si" depende  de su decisión en tiempo de ejecución.
