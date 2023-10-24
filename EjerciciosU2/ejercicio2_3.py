def division(n1: int, n2: int):
    if (n2 == 0):
        return "Error, no se puede dividir por 0."
    else:
        res = n1 / n2
        return "{n1} / {n2} = {res}".format(n1 = n1, n2 = n2, res = res)
    
num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
print(division(num1, num2))