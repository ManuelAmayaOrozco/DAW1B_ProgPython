def convgrad():
    tempc = int(input("Dime la temperatura en grados Fahrenheit:"))
    tempf = (tempc - 32) * 5 / 9
    return tempf

print("La temperatura en Celsius es", convgrad()) 