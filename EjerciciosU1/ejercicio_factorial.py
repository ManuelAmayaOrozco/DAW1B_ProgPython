def factorial(num: int):
    cont = num
    if (num == 0):
        num = 1
    else:
        while(cont > 1):
            num *= (cont-1)
            cont -= 1
    return num

x = int(input("Dime un número para hacerle el factorial: "))
print("El factorial del número es {res}".format(res = factorial(x)))