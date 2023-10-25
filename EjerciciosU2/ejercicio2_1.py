def edad(ed: int):
    if (ed >= 18):
        return "Eres mayor de edad."
    else:
       return "No eres mayor de edad."

años = int(input("Dime tu edad: "))
print(edad(años))