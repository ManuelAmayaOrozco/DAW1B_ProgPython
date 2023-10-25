price = input("Dime el precio de un producto, usando dos decimales: ")
print("Son", price[:price.find(".")], "euros y", price[price.find(".")+1:], "céntimos.")