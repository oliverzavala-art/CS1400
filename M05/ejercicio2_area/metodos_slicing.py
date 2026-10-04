
"""
# Conteo descendente
num = int(input("Introduce el número inicial: "))

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

import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F

# 5. ¿Resultado de la Línea A round(decNum, 2)? -34.57 Respuesta: Redondea a los primeros 2 decimales.

# 6. ¿Resultado de la Línea B round(decNum, 0)?  -35 Respuesta: Redondea ya que no se muestran decimales.

# 7. ¿Resultado de la Línea C int(decNum)? -34  (Pista: ¿Redondea o trunca los decimales?) respuesta: Trunca los decimales.

# 8. ¿Resultado de la Línea D abs(decNum)? 34.5678 Respuesta: Devuelve el valor absoluto.

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)?  81 Respuesta: Calcula intNum (9) elevado a la potencia de 2.

# 10. ¿Resultado de la Línea F math.sqrt(intNum)? 3.0 Respuesta: Calcula la raíz cuadrada de intNum (9 ).
miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)

# 11. Antes de ejecutar: ¿Cuál crees que será el resultado devuelto por max()?

#Predicción: "Zanahoria"
# 12. Ejecuta el código. ¿Cuál fue el resultado real devuelto?

#Resultado: "manzana"

# 13. Sabiendo que en la tabla ASCII las mayúsculas tienen valores numéricos menores que las minúsculas, explica por qué "manzana" fue seleccionada como la mayor frente a "Zanahoria".

# 14. Cambia la función de max() a min(). ¿Qué valor obtienes ahora y por qué?
miMin = min("Banano", "manzana", "Zanahoria")
print("El mínimo es:", miMin)

#Resultado: "Banano"
#Explicación: "Banano" es el mínimo porque en la tabla ASCII las mayúsculas tienen valores numéricos menores que las minúsculas.

import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(2 * 9.8 * d)
print("Velocidad estimada del auto:", round(v, 2), "km/h")  

# 15. Completa la asignación v = en el código superior utilizando la función math.sqrt() y la fórmula entregada. Escribe la línea completa a continuación:
#Respuesta: v = math.sqrt(2 * 9.8 * d)

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])

# 16. ¿Qué carácter imprime exactamente nombre[0]? Respuesta: "B"

# 17. ¿En qué posición (índice) exacta se encuentra el espacio en blanco entre ambas palabras? Respuesta: 8
"""
# 18. Modifica los índices en nombre[X:Y] para extraer e imprimir exactamente la palabra "Puentes".
print("Palabra 'Puentes':", nombre[9:15])
print("Palabra 'Puentes' (límite implícito):", nombre[9:])
#Opción con 2 valores: nombre[9:15]
#Opción con límite implícito: nombre[9:]