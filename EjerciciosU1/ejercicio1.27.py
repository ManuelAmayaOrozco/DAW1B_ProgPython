product = input("Dime el nombre de un producto: ")
price = float(input("Dime el precio del producto: "))
quant = int(input("Dime la cantidad de productos que hay: "))
print("{product}: {quant:3d} unidades x {price:9.2f}€ = {total:11.2f}€".format(product = product, quant = quant, price = price, total = quant * price))