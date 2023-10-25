def rendimiento(niv: float):
    din = 2400 * niv
    if(niv <= 0.3 ):
        return "Nivel inaceptable, recibirá una paga de {din}€.".format(din = din)
    elif(0.4 <= niv <= 0.5):
        return "Nivel aceptable, recibirá una paga de {din}€.".format(din = din)
    else:
        return "Nivel meritorio, recibirá una paga de {din}€.".format (din = din)
    
punt = float(input("Dime tu puntuación de rendimiento: "))
print(rendimiento(punt))