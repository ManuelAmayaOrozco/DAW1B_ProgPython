"""
Algoritmo que soolicite nombre y edad.
Inicio
    Escribe "Dime tu nombre:"
    Leer nom
    Si (nom=="" or " ") entonces
        nom = "Desconocido"
    edad = 0
    Mientras(edad<0 or edad>125) hacer
        Escribe "Dime tu edad entre 0 y 125 años:"
        Leer edad
        Si (edad<0 or edad>125) entonces
            Escribe "Edad no válida."
    tiemp = 125-edad
    Escribir "Te llamas " + nom + " y tienes " + edad + " años, te quedan aún " + tiemp + " años por cumplir."
Fin
"""

nom = input("Dime tu nombre: ")
if (nom==""):
    nom = "Desconocido"
elif (nom==" "):
    nom = "Desconocido"
edad = int(-1)
while (edad<0 or edad>125):
    edad = int(input("Dime tu edad entre 0 y 125 años: "))
    if (edad<0 or edad>125):
        print("Edad no válida.")
tiemp = 125 - edad
print("Te llamas", nom, "y tienes", edad, "años, te quedan aún", tiemp, "años por cumplir.")