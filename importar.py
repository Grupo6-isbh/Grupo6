import Suma
import resta
import division
import multiplicacion

# Pedir al usuario que elija una operación
operacion = input("Elija una operación (suma, resta, division, multiplicacion): ")

# Pedir al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar a la función correspondiente
if operacion == "suma":
    resultado = Suma.suma(num1, num2)
    print("La suma de los dos números es:", resultado)
elif operacion == "resta":
    resultado = resta.resta(num1, num2)
    print("La resta de los dos números es:", resultado)
elif operacion == "division":
    resultado = division.division(num1, num2)
    print("La resta de los dos números es:", resultado)
elif operacion == "mulriplicacion":
    resultado = multiplicacion.multiplicacion(num1, num2)
    print("La resta de los dos números es:", resultado)
else:
    print("Operación inválida.")
