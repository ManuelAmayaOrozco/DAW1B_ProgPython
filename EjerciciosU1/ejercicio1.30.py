"""
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