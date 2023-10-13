"""
 Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...

> Introduce un número: 4
> Introduce otro: 8
> 4-5-6-7-8

> Introduce un número: 12
> Introduce otro: 3
> 3-4-5-6-7-8-9-10-11-12

Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x >= y) entonces
		numIni = x - 1
		numFin = y
	Sino
		numIni = y - 1
		numFin = x
		
	Para i en (numIni...numFin) hacer
		Escribe i + 
		Si (numIni != numFin) entonces
			Escribe "-"

Fin
"""

x = int(input("Introduce un número: "))
y = int(input("Introduce otro: "))

if (x >= y):
    numIni = y
    numFin = x
    ser = "{y}".format(y = numIni)
else:
    numIni = x
    numFin = y
    ser = "{x}".format(x = numIni)

while (numIni < numFin):
    ser = "{ser}-{sig}".format(ser = ser, sig = (numIni + 1))
    numIni += 1
print(ser)