"""
Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.

> Dame 3 números:
> 14
> 7
> 10
> Tus números son 7 10 14

Inicio

	Escribe "Dame 3 números: "
	Lee n1
	Lee n2
	Lee n3
	
	Si (n1 < n2 and n1 < n3) entonces
		Si (n2 < n3) entonces
			Escribe n1 + " " + n2 + " " + n3
		Sino
			Escribe n1 + " " + n3 + " " + n2
	Sino
		Si (n2 < n1 and n2 < n3) entonces
			Si (n1 < n3) entonces
				Escribe n2 + " " + n1 + " " + n3
			Sino
				Escribe n2 + " " + n3 + " " + n1
		Sino
			Si (n3 < n1 and n3 < n2) entonces
				Si (n1 < n2) entonces
					Escribe n3 + " " + n1 + " " + n2
				Sino
					Escribe n3 + " " + n2 + " " + n1

Fin
"""

n1 = int(input("Dame 3 números: "))
n2 = int(input())
n3 = int(input())

if (n1 < n2 and n1 < n3):
    if (n2 < n3):
        print("Tus números son {n1}<{n2}<{n3}".format(n1 = n1, n2 = n2, n3 = n3))
    else:
        print("Tus números son {n1}<{n3}<{n2}".format(n1 = n1, n3 = n3, n2 = n2))
elif (n2 < n1 and n2 < n3):
    if (n1 < n3):
        print("Tus números son {n2}<{n1}<{n3}".format(n2 = n2, n1 = n1, n3 = n3))
    else:
        print("Tus números son {n2}<{n3}<{n1}".format(n2 = n2, n3 = n3, n1 = n1))
elif (n3 < n1 and n3 < n2):
    if (n1 < n2):
        print("Tus números son {n3}<{n1}<{n2}".format(n3 = n3, n1 = n1, n2 = n2))
    else:
        print("Tus números son {n3}<{n2}<{n1}".format(n3 = n3, n2 = n2, n1 = n1))