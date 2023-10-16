def ivacion(precio: float, iv: float):
    total = precio * iv
    print("El precio total con IVA es", total)

prec = int(input("Dime el precio del producto sin IVA: "))
iva = float(input("Dime el IVA a aplicar: "))
ivacion(prec, iva)