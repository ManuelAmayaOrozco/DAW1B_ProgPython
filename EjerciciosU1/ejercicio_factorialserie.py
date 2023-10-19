def factorial(num: int):
    cont = num
    if (num == 0):
        res = 1
        ser = "{num}! => {res}".format(num = num, res = res)
    elif (num == 1):
        res = 1
        ser = "{num}! => {res}".format(num = num, res = res)
    else:
        ser = "{num}! => {num} x {conttext}".format(num = num, conttext = (cont - 1))
        cont -= 1
        res = num * (cont)
        while(cont > 1):
            cont -= 1
            res = res * (cont)
            ser = ser + " x {cont}".format(cont = cont)
        ser = ser + " = {res}".format(res = res)
    return ser

x = int(input("Dime un número para hacerle el factorial: "))
print(factorial(x))