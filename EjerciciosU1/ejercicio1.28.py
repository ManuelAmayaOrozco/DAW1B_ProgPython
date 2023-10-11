"""
Algoritmo que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
Inicio
    Escribir "Dime un número:"
    Leer num1
    Escribir "Dime otro número:"
    Leer num2
    Si (num1==num2) entonces
        Escribir "Los números no pueden ser iguales."
    Sino
        Si (num1<num2) entonces
            dist = num2-num1
            Escribir "El número menor es el " + num1 + " y entre ellos existen " + dist + " números enteros."
        SiNo
            dist = num1-num2
            Escribir "El número menor es el " + num2 + " y entre ellos existen " + dist + " números enteros."
Fin
"""

num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
if (num1==num2):
    print("Los números no pueden ser iguales.")
else:
    if (num1<num2):
        dist = num2 - num1
        print("El número menos es", num1, "y entre ellos esxisten", dist, "números enteros.")
    else:
        dist = num1 - num2
        print("El número menos es", num2, "y entre ellos esxisten", dist, "números enteros.")