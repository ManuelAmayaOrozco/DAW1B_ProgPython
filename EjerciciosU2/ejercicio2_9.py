def precio(ed: int):
    if(ed < 4):
        return "Entrada gratis."
    elif(4 <= ed <= 18):
        return "Tiene que pagar 5€."
    else:
        return "Tiene que pagar 10€."
  
def main():  
    edad = int(input("Dime tu edad: "))
    print(precio(edad))
    if __name__ == '__main__':
        main()