def ivacion(precio: float):
    iva = float(input("Dime el IVA a aplicar: "))
    total = prec * iva
    print("El precio total con IVA es", total)

prec = int(input("Dime el precio del producto sin IVA: "))

ivacion(prec)