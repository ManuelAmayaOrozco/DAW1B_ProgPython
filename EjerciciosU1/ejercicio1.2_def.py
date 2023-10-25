def imprt(horas: int, coste: float):
    imptot = horas * coste
    return imptot

htrab = int(input("Dime las horas de trabajo: "))
chora = int(input("Dime el coste por horas: "))
print("Horas de trabajo:", htrab)
print("Coste por hora:", chora)
print("Importe total:", imprt(htrab, chora))