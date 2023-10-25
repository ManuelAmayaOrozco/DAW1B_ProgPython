peso = float(input("Dime tu peso en kilogramos: "))
alto = float(input("Dime tu altura en metros: "))
masac = peso / alto ** 2
round(masac,2)
print("Tu indice de masa corporal es ", masac)