def tributar(ed: int, din: int):
    if (ed < 16 or din < 1000):
        return "Usted no tiene que tributar."
    else:
        return "Usted tiene que tributar."
    
edad = int(input("Dime tu edad: "))
ing = int(input("Dime tus ingresos mensuales en euros: "))
print(tributar(edad, ing))