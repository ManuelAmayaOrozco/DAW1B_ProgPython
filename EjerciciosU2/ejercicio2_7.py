def renta(din: int):
    if(din < 10000):
        return "Tu tipo impositivo es del 5%."
    elif(10000 <= din < 20000):
        return "Tu tipo impositivo es del 15%."
    elif(20000 <= din < 35000):
        return "Tu tipo impositivo es del 20%."
    elif(35000 <= din < 60000):
        return "Tu tipo impositivo es del 30%."
    else:
        return "Tu tipo impositivo es del 45%."
    
dinren = int(input("¿Cuánto pagas por tu renta (en euros)?: "))
print(renta(dinren))