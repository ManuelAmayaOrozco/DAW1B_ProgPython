"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio
    days = -1
    Mientras (days < 0) hacer
        Escribir "Introduzca los días trabajados: "
        Leer days
        Si (days < 0) entonces
            Escribir "*** Error - el valor no puede ser negativo ***"
            
    years = days // 365
    months = (days - (years * 365)) // 30
    enddays = days - (years * 365) - (months * 30)
    
    Si (years == 1) entonces
        yeartext = "año"
    Sino
        yeartext = "años"
    
    Si (months == 1) entonces
        monthtext = "mes"
    Sino
        monthtext = "meses"

    Si (enddays == 1) entonces
        enddaytext = "día"
    Sino
        enddaytext = "días"
        
    Escribir "Ha cotizado " + years + " " + yearstext + ", " + months + " " + monthtext + " y " + enddays + " " + enddaytext + "."
Fin
"""
days = -1
while (days < 0):
    days = int(input("Introduzca los días trabajados: "))
    if (days < 0):
        print("*** Error - el valor no puede ser negativo ***")
        
years = days // 365
months = (days - (years * 365)) // 30
enddays = days - (years * 365) - (months * 30)

if (years == 1):
    yeartext = "año"
else:
    yeartext = "años"
    
if (months == 1):
    monthtext = "mes"
else:
    monthtext = "meses"
    
if (enddays == 1):
    enddaytext = "día"
else:
    enddaytext = "días"
    
print("Ha cotizado {years} {yeartext}, {months} {monthtext} y {enddays} {enddaytext}.".format(years = years, yeartext = yeartext, months = months, monthtext = monthtext, enddays = enddays, enddaytext = enddaytext))