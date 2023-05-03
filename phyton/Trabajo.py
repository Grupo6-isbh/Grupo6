''' 1) Escribir la definicion de función:
Una función es una regla de correspondencia entre dos conjuntos
 de tal manera que a cada elemento del primer conjunto le corresponde uno y sólo un elemento del segundo conjunto.
En lógica, una función es una expresión que toma uno o más valores de entrada, llamados argumentos,
 y produce un valor de salida, llamado resultado. Las funciones en lógica se utilizan para definir
   proposiciones o para combinar proposiciones para construir argumentos más complejos.'''

'''2) Escribir la definición de proceso:
En matemáticas, un proceso es una sucesión de operaciones o pasos lógicos que se realizan para llegar a una conclusión o solución.
Estos procesos pueden ser numéricos o algebraicos, y pueden implicar la manipulación de variables, constantes o símbolos matemáticos.'''

'''3) Dado 2 conjuntos A y B, ¿cuando se corresponden con una función y cuando no? Dar ejemplos:
Para que se corresponda una Función(f) tiene que tener un elemento único de relación entre el conjunto A y el conjunto B.
Por ejemplo: si A es el conjunto {1, 2, 3} y B es el conjunto {a, b, c}, entonces una función f que asigna cada elemento
de A a un elemento de B.
f(1): a
f(2): d
f(3): c
En cambio no podría funcionar si se repite, es decir si A es el conjunto {1,2,3} y B es el conjunto {a,b,c,d}.
En el ejemplo que vemos a continuación, vamos a ver que el conjunto de A, se repite el número 1.
f(1): a
f(2): b
f(3): c
f(1): d'''




'''4) Escribir en simbolos una función lineal, y su correspondiente codificación en python:
La funcion Lineal en simbolo es:
    f(x)= mx + b o y=mx + b'''

def Funcion_lineal(m, x, b):
    y = m * x + b
    return y

''' 5) Escribir en simbolos una función cuadrática, y su correspondiente codificación en python:
La funcion Cuadratica en simbolo es:
    f(x)= ax² + bx + c o y = ax² + bx + c '''

'''y = a * x^2 + b * x + c'''

def Funcion_Cuadratica(a,x,b,c):
    y = a * x**2 + b * x + c
    return y

'''
6) Escribir en simbolos una función condicional, y su correspondiente codificación en python:
La funcion condicional en simbolo es:
Si (if) a>5 entonces(then) escribe "el trabajo da salud y bienestar" y si no (else) escribe "el hambre enseña mas que la universidad" devolviendo(return) el resultado.
'''
def es_positivo(x):
    if x > 0:
        resultado = "El número es positivo"
    else:
        resultado = "El número es negativo o cero"
    
    return resultado

'''
7) Escribir en simbolos una función senoidal, y su correspondiente codificación en python:
La funcion senoidal en simbolo es:
f(x)= a sin(bx+c)+d
'''

#lo tuve que comentar ya que no me dejaba importar las bibliotecas numpy y matpltlib.pyplot

'''
import numpy as np
import matplotlib.pyplot as plt

 (Crear una matriz de valores x)
x = np.linspace(0, 2*np.pi, 100)

 (Crear una función senoidal de amplitud 1 y frecuencia 1)
y = np.sin(x)

 (Graficar la función senoidal)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Función Senoidal')
plt.show()
'''

'''
8) ¿Que diferencia hay entre ecuación y función?
Una funcion es una relacion entre dos conjuntos de variables. Por otro lado, una ecuacion es una sentencia que relaciona dos o mas variables. En una funcion, una variable
se relaciona con la otra de manera unica. En una ecuacion, varias variables se relacionan entre si. 
'''
'''
9)Observe la imagen: ¿Es una función?
No, no es un funcion ya que para el valor de "a" se le asignan 2 valores de "b" y segun la difinicion solo puede tener uno y solo uno de los valores de "b"
'''