def reemplazo(x: int):
    suma = (x * (x + 1)) / 2
    return suma

print("(n * (n + 1)) / 2")
n = int(input("Elige un número para reemplazar n: "))
print("El resultado es ", reemplazo(n))