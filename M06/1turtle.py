""" TODO 1 agregar tu nombre fecha titulo de una manera bonita """
# Nombre: Oliver Zavala
# Fecha: 2024-06-12
# Título: Dibujando una casa con turtle

# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen() # # Usamos sintaxis de punto . para acceder a la función Screen()
pantalla.bgcolor("lightblue")
pantalla.title("Mi pequeña tortuga") #TODO 3 Asigna un título a la ventana usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# solo una t para hacer menos codigo despues. usaremos la t variable para usar otras funciones.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

# TODO 4 Utiliza """ """ para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6

# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("black", "blue")
# son argumentos de la función color()
t.begin_fill()  # esta línea indica que la tortuga comenzará a rellenar la forma que dibuje a continuación

# TODO 6 Este for loop que hace?
# Este for loop dibuja un cuadrado moviendo la tortuga hacia adelante y girando 90 grados cuatro veces.
for _ in range(4):  # este es un bucle que se ejecuta 4 veces
    t.forward(100)  # esta línea hace que la tortuga avance 100 unidades hacia adelante
    t.left(90)      # esta línea hace que la tortuga gire 90 grados a la izquierda

# TODO 7 En que linea de codigo empezo el fill? o relleno?
# el fill comiensa en la linea 29 con t.begin_fill()
# el fill termina en la linea 40 con t.end_fill()
t.end_fill()



# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()