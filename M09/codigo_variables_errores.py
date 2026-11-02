
"""
Parte 1: Código Vulnerable a Errores
Observa y analiza el siguiente segmento de código antes de ejecutarlo:
"""
lst = [1, 3, 7, 3]

# Entrada de datos
num = int(input("Ingrese un número entero: "))

# Operación 1: División
print(10 / num)

# Operación 2: Acceso a Lista
print(lst[num])

# Operación 3: Continuación
print("El programa continuó con éxito.")
"""
Preguntas
1-Analiza las operaciones antes de ejecutar:
a-¿Por qué la Operación 1 (10 / num) fallará si el usuario ingresa 0?
respuesta: La operación fallará porque no es posible dividir entre cero.
b-¿Por qué la Operación 2 (lst[num]) fallará si el usuario ingresa 100?
respuesta: La operación fallará porque el índice 100 está fuera del rango de la lista lst.

2-Ejecución y pruebas: Ejecuta el programa tres veces con las entradas indicadas y completa la siguiente tabla de resultados:
Entrada del usuario	¿Llegó a imprimirse "El programa continuó..."? (Sí/No)	Nombre exacto de la excepción generada en consola
"dos"	respuesta 	No		ValueError
0	No	respuesta ZeroDivisionError
100	No		respuesta IndexError

3-¿Qué ocurre con la ejecución de las líneas de código subsiguientes cuando Python encuentra un error no capturado en una línea previa?
respuesta: La ejecución de las líneas de código subsiguientes se detiene y el programa termina abruptamente.

Parte 2: Control de Flujo con try / except
Para evitar que el programa se detenga, envolvemos el código propenso a errores dentro de un bloque try y capturamos las fallas con except.
"""
try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

except ValueError:
    print("❌ Error: Debes ingresar un número entero válido (sin letras).")
except:
    print("❌ Ocurrió un error general.")

print("El programa continúa su ejecución normal...")
"""
Preguntas y Modificaciones
Ejecuta el código anterior e ingresa "dos". ¿Qué mensaje se imprime? ¿Se ejecuta la última línea de "El programa continúa..."?
Ejecuta el código e ingresa 0. ¿Por qué se activa el mensaje "Ocurrió un error general" en lugar del de ValueError?
Modificación de código 1: Agrega un bloque except ZeroDivisionError específico con el mensaje: "❌ Error: No es posible dividir entre cero."
Modificación de código 2: Identifica el tipo de error que ocurre al intentar acceder a un índice inexistente en la lista lst (al ingresar 100). Agrega un bloque except específico para capturar dicho error con un mensaje descriptivo.
Pega tu código corregido con las 3 excepciones específicas aquí.
Parte 3: Rastrear Errores con traceback y Controlar raise / finally
A. Diagnóstico técnico con traceback
A veces necesitamos registrar el detalle técnico del error para los desarrolladores sin detener la aplicación.
"""
import traceback

try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError as e:
    print("⚠️ Capturamos un ValueError. Detalle técnico:")
    s = traceback.format_tb(e.__traceback__)
    print(s)

print("El programa continúa...")
"""
En la línea except ValueError as e, ¿qué representa la variable e?
¿Qué ventaja ofrece la función traceback.format_tb() frente a simplemente mostrar un mensaje amigable al usuario?
B. Validación explícita con raise y garantía con finally
Podemos forzar la creación de nuestras propias excepciones usando raise cuando un dato no cumple con nuestras reglas de negocio, y asegurar la ejecución de código final con finally.
"""
print("--- Validación de Rango ---")
num = 0

while num < 1 or num > 10:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        
        if num < 1 or num > 10:
            raise Exception("El número está fuera del rango permitido.")
            
    except ValueError:
        print("❌ Error: Formato incorrecto, se esperaba un número.")
    except Exception as e:
        print(f"⚠️ Error de validación: {e}")
    finally:
        print("🔔 [Bloque Finally] Intento de entrada finalizado.")

print(f"¡Número válido ingresado con éxito! ({num})")
"""
¿En qué situaciones se ejecutará el código dentro del bloque finally?
¿Qué función cumple la palabra clave raise en el condicional if num < 1 or num > 10?
¿Qué ocurre en el bucle while cuando el usuario ingresa un valor válido (ejemplo: 5)?
Parte 4: Aplicación Práctica — Calculadora Robusta
Completa el motor de la calculadora interactiva. Debe mantenerse en ejecución continua pidiendo datos hasta que el cálculo se complete correctamente sin ningún error.

Código Base
Copia este fragmento en tu editor y completa los bloques señalados con # TODO:
"""
def calculadora_segura():
    print("\n--- Calculadora Robusta ---")
    
    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                # TODO 1: Lanza (raise) un ValueError con el mensaje "Operador no válido"
                pass

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break  # Salir del bucle si el cálculo se realizó con éxito

        # --- MANEJO DE EXCEPCIONES ---

        # TODO 2: Captura el error de formato cuando el usuario ingresa texto en lugar de números
        # except ...:
        #     print("❌ Error: Ingrese valores numéricos válidos.")

        # TODO 3: Captura la división por cero
        # except ...:
        #     print("❌ Error: No se puede dividir entre cero.")

        # TODO 4: Captura el ValueError (generado por el operador inválido) y muestra e
        # except ValueError as e:
        #     print(f"❌ Error de entrada: {e}")

        except Exception as e:
            print(f"❌ Error no esperado: {e}")
        
        finally:
            # TODO 5: Muestra siempre un mensaje de cierre de intento
            pass
"""
calculadora_segura()
Preguntas de Reflexión
¿Cuál es el propósito de la instrucción break colocada al final de la sección try?
Si el usuario ingresa n2 = 0 y op = '/', ¿se llega a ejecutar la línea print(f"✅ Resultado: {resultado}")? Explica la secuencia del flujo de ejecución.
¿Qué sucedería con la experiencia de usuario si omitimos el bucle while True en este programa?
Criterios de Entrega
Documento con las respuestas numéricas a todas las preguntas (1 a 16).
Capturas de pantalla ejecutando la calculadora en tres casos:
Entrada de texto en lugar de número.
División por cero.
Cálculo exitoso.
Código fuente completo de la calculadora_segura() resuelta y funcional.
Elegir un tipo de presentación
"""