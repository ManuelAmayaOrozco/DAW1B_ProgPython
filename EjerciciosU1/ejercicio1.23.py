mail = input("Dime tu correo electrónico: ")
print(mail[:mail.find("@")] + "@ceu.es")

pos = mail.find("@")
print(mail[:pos+1] + "ceu.es")