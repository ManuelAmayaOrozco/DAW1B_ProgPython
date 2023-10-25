clown = 112
doll = 75
nclown = int(input("¿Cuántos payasos va a llevar este pedido? "))
ndoll = int(input("¿Cuántas muñecas va a llevar este pedido?"))

tweight = (clown * nclown) + (doll * ndoll)

print("El peso total del paquete será", tweight, "g")