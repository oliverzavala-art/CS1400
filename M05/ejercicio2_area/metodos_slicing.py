

# Conteo descendente
num = int(input("Introduce el número inicial: "))
"""
for i in range(num, 0, -1):
    print("Conteo:", i) 

    # 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?
# REspuesta : Inicio: 10 | Fin: 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
# Respuesta : El parámetro step  (paso)debe ser negativo para que el conteo disminuya en lugar de aumentar.

# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
# Respuesta : El valor final se configuró en 0 porque en Python no seincluye el valor final. 
# Por eso , para que el conteo se detuviera en 1 , se debe poner 0 como valor final.

# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:
for i in range(num, -1, -2):
    print("Conteo:", i) 
# Respuesta : range(num, -1, -2)
"""
import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F

# 5. ¿Resultado de la Línea A round(decNum, 2)? _________

# 6. ¿Resultado de la Línea B round(decNum, 0)? _________

# 7. ¿Resultado de la Línea C int(decNum)? _________ (Pista: ¿Redondea o trunca los decimales?)

# 8. ¿Resultado de la Línea D abs(decNum)? _________

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)? _________

# 10. ¿Resultado de la Línea F math.sqrt(intNum)? _________