
"""
NOMBRE: Oliver Zavala
FECHA: 25/09/2026
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""

try:
    edad = int(input("¿Qué edad tienes? "))
except ValueError:
    edad = -1

if edad < 0:
    print("Edad no válida. Por favor, ingresa una edad correcta.")
elif edad < 18:
    print("Eres menor de edad, aún no puedes conducir.")
elif edad <= 70:

    lentes = input("¿Usas lentes? (s/n): ")
    if lentes.lower() == "s":
        print("¡Si puedes conducir pero tienes que usar tus lentes!")
    else:
        print("¡Puedes conducir! Pero recuerda siempre usar tus lentes si los necesitas.")
else:
    audifonos = input("¿Usas audífonos para escuchar? (s/n): ")
    if audifonos.lower() == "s":
        print("¡No olvides tus audífonos al manejar!.")
    else:
        print("¡Puedes conducir! Pero ten cuidado y mantén la atención en la carretera.")



#Analysis

### 1. ¿Cuántos commits hiciste

 # Hice 7 commits


### 2. ¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub los comandos en la terminal o la interfaz visual de Visual Studio Code ¿Por qué?

# Me pareció más fácil usar la interfaz visual de VS Code porque permite guardar y subir cambios con botones, sin escribir comandos.


### 3. ¿Para qué sirve ejecutar el comando `git status` antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar
# El comando "git status " Sirve para ver qué archivos cambiaron y cuáles están pendientes por guardar.


### 4. ¿Por qué es fundamental descargar (`git pull`) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto

# Sirve para actualizar el proyecto y evitar conflictos al subir mis cambios.

### 5. En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar (clone) un repositorio a tu computadora

# "Clone" copia un repositorio de GitHub a mi computadora. En cambio, "fork" crea una copia del repositorio en mi cuenta de GitHub.


### 6. ¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit (por ejemplo `Agregando mi nombre al proyecto de M4`) en lugar de usar palabras vagas como `cambios` o `listo`


 # Porque esto permite que otros colaboradores y yo entendamos qué cambio específico se realizó.


### 7. ¿Qué tipos de mensajes agregaste

# Agregué mensajes sobre la creación del archivo, la lógica de la edad y los comentarios del código.

### 8. ¿Cuál es tu sentencia preferida

 # Mi sentencia preferida es `if`, `elif` y `else`, porque me permite tomar decisiones lógicas en el programa
 #  dependiendo de si la persona cumple con la edad mínima para obtener la licencia.


### 9. ¿Cuándo entra el programa a la segunda sentencia de tu tarea

# El programa entra al segundo bloque (`elif`) cuando la edad está entre 18 y 70 años, porque la primera condición no se cumple.


### 10. ¿Qué aprendiste del `README.md` en tu carpeta M04 No olvides los comentarios!
# Aprendí la estructura que se necesita para la tarea de la licencia de conducir, la importancia de verificar los datos ingresados por el usuario 
# y cómo documentar mi código mediante comentarios (`#`) y agregar commits para describir qué hace cada sección del programa.