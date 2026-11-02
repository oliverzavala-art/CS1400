""" Escribe un programa que:

Pida el nombre del usuario.

Pida dos números enteros.

Guarde su suma en una tercera variable.

Muestre un mensaje como:

text
Ana, la suma es: 15

nombre = input("Cual es tu nombre ")
numeros1= int(input ("dame 1 numero "))
numero2 = int (input ("Dame otro numero "))
suma = numeros1 + numero2
print ("Tu nombre es ", nombre,"las suma delos numeros es ",suma)
"""
"""B. Condiciones
Pide una nota entera y muestra:

"Excelente" si es mayor o igual a 90.

"Aprobado" si es mayor o igual a 70, pero menor que 90.

"Necesita mejorar" si es menor que 70."""

calificacion = int (input ("Que calificacion tienes "))
if calificacion >= 90:
 print ("Exelente ")
elif calificacion >= 70:
 print ("aprobado")
else :
 print ("necesitas mejorar") 

 def box_print(symbol, width, height):
    if len(symbol) != 1:
       raise Exception('Symbol must be a single character string.')
    if width <= 2:
       raise Exception('Width must be greater than 2.')
    if height <= 2:
       raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print('*', 4, 4)
    box_print('O', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
   print('An exception happened: ' + str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))