total = int(input("Dime el precio final del artículo: "))
prec = total / 1.1
ivapag = total - prec
print("El IVA pagado es de", ivapag, "y el precio sin IVA es", prec)