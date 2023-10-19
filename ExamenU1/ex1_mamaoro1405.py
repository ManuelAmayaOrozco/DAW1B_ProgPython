"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
    Escribe "Dime un número: "
    Leer num
    Si (num < 0) entonces
        Escribe "Error, número no válido."
    Si (num > 10) entonces
        Escribe "Error, número no válido."
    Sino
        pareo = num % 2
        Si (pareo == 0)
            Escribe "El número " + num + " es par."
        Sino
            Escribe "El número " + num + " es impar."
Fin
"""