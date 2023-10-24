def paridad(n: int):
    res = n % 2
    if(res == 0):
        return "El número es par."
    else:
        return "El número es impar."
    
num = int(input("Dime un número: "))
print(paridad(num))