BARRAPAN = 3.49
altbarrapan = 3.49 * 0.4
round(altbarrapan,2)

totaltbarra = int(input("¿Cuántas barras que no son del día se han vendido? "))
prectotal = totaltbarra * altbarrapan
round(prectotal,2)

print("Precio barra normal:", BARRAPAN, "€")
print("A las barras que no son del día se les hace un descuento del 60%, por lo que cuestan ", altbarrapan, "€")
print("El precio total de todas las barras de pan que no son del dia que han sido vendidas es de", prectotal, "€")