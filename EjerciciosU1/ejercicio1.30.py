"""
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python.

Algoritmo que pida un número de inicio, un incremento y un total de la serie.
Inicio
    Escribir "Dime un número:"
    Leer num
    inc = 0
    tot = 0
    Mientras (inc<=0 or tot<=0) hacer
        Escribir "Dime un incremento:"
        Leer inc
        Escribir "Dime un total de veces a repetir de la serie:"
        Leer tot
        Si (inc<=0 or tot<=0) entonces
            Escribir "Error. Incremento/Total no válido."
        SiNo
            cont = 0
            ser = "SERIE => " + num + " - " + (num+inc)
            num = num + inc
            Mientras (cont < tot)
                num+=inc
                ser = ser + " .. " + num
                cont+=1
            ser = ser + " - " + (num+inc)
            Escribir ser
"""

num = int(input("Dime un número: "))
inc = int(0)
tot = int(0)
while (inc<=0 or tot<=0):
    inc = int(input("Dime un incremento: "))
    tot = int(input("Dime un total de veces a repetir de la serie: "))
    if (inc<=0 or tot<=0):
        print("Error. Incremento/Total no válido.")
    else:
        cont = int(1)
        ser = "SERIE => {num}-{plus}".format(num = num,plus = (num + inc))
        num += inc
        while (cont < tot-2):
            num += inc
            ser = "{ser}..{num}".format(ser = ser,num = num)
            cont += 1
        ser = "{ser}-{plus}".format(ser = ser,plus = (num + inc))
        print(ser)