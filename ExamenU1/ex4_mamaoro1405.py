"""
Corrige los errores para que el siguiente programa funcione correctamente cómo se explica a continuación...

Recorre la lista y dependiendo del tipo de dato de cada elemento muestra la siguiente información:
   1. int => "Tienes N años".

   2. float => "El producto vale N€, pero está en oferta por (N*0.85)€", donde el primer precio se muestra con 0 decimales y el segundo, que está en oferta al 85% de su precio original, con 2 decimales.

   3. str => "Te llamas N1 pero todos te conocen cómo N2." N1 será el nombre completo y N2 solo el primer nombre. N1 cambiará la a por una @ y tendrá las iniciales de cada nombre en mayúsculas y el resto en minúsculas. N2 tendrá todas las letras en mayúsculas.

   4. bool => Si es True dice la verdad, sino dice la mentira.

   El resultado de ejecutar este programa debe ser el siguiente:

   Tienes 43 años.
   Te llamas Pedro P@blo, pero todos te conocen cómo PEDRO.
   El producto vale 18€, pero está en oferta por 15.01€
   El producto vale 9€, pero está en oferta por 7.64€
   Te llamas M@rí@ Jesús, pero todos te conocen cómo MARÍA.
   Estás diciendo una mentira.
   Te llamas @n@ Esper@nz@, pero todos te conocen cómo ANA.
   Tienes 25 años.
   Estás diciendo la verdad.
   El producto vale 10€, pero está en oferta por 8.49€
"""

miLista = [43, "pedro pablo", 17.66, 8.99, "maría jesús", False, "ANA esperanza", 25, True, 9.99]

cont = 0
while (cont < len(miLista)):
    if type(miLista[cont]) is int:
        edad = miLista[cont]
        print("Tienes {años} años.".format(años = miLista[cont]))
    elif type(miLista[cont]) is float:
        precio = float(miLista[cont])
        precioOferta = 0
        print("El producto vale {precio:.0f}€, pero está en oferta por {precioOferta:.2f}€".format(precio = miLista[cont], precioOferta = (miLista[cont] * 0.85)))
    elif type(miLista[cont]) is str:
        nombreCompleto = str(miLista[cont]).title()
        nombreCompleto = nombreCompleto.replace("A", "@")
        nombreCorto = str(miLista[cont]).upper()
        print("Te llamas", nombreCompleto.replace("a", "@"), ", pero todos te conocen cómo", nombreCorto[:nombreCorto.find(" ")], ".")
    elif type(miLista[cont]) is bool:
        verdad = bool(miLista[cont])
        if (verdad == False):
            print("Estás diciendo una mentira.")
        else:
            print("Estás diciendo la verdad.")
    cont += 1
    
"""
Sale un supuesto error al final siempre pero si le das para arriba puedes ver el resultado correctamente.
"""    