"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""
pal = input("Introduzca una palabra: ")
palapoy = pal.replace(" ", "")
while (len(palapoy) < 8):
    if (len(palapoy) < 8):
        pal = input("Introduzca una palabra *mínimo 8 letras*: ")
        palapoy = palapoy.replace(" ", "")

pal = pal.replace(" ", "")
pal = pal.replace("a", "@")
pal = pal.replace("A", "@")
pal = pal.replace("b", "B")
pal = pal.replace("c", "C")
pal = pal.replace("d", "D")
pal = pal.replace("e", "3")
pal = pal.replace("E", "3")
pal = pal.replace("f", "F")
pal = pal.replace("g", "G")
pal = pal.replace("h", "H")
pal = pal.replace("i", "1")
pal = pal.replace("I", "1")
pal = pal.replace("j", "J")
pal = pal.replace("k", "K")
pal = pal.replace("l", "L")
pal = pal.replace("m", "M")
pal = pal.replace("n", "N")
pal = pal.replace("O", "o")
pal = pal.replace("p", "P")
pal = pal.replace("q", "Q")
pal = pal.replace("r", "R")
pal = pal.replace("s", "S")
pal = pal.replace("t", "T")
pal = pal.replace("U", "u")
pal = pal.replace("v", "V")
pal = pal.replace("w", "W")
pal = pal.replace("x", "X")
pal = pal.replace("y", "Y")
pal = pal.replace("z", "Z")

if (len(pal) == 8):
    pal = "*{pal}#".format(pal = pal)

print("Su palabra encriptada es {pal}".format(pal = pal))