def pizzatime(elec: str):
    if (elec == "V"):
        ing = input("Elige un ingrediente (Pimiento, Tofu): ")
        return "Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}.".format(ing = ing)
    else:
        ing = input("Elige un ingrediente (Peperoni, Jamón, Salmón, Pimiento, Tofu): ")
        if (ing == "Pimiento" or ing == "Tofu"):
            return "Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}.".format(ing = ing)
        else:
            return "Su pizza lleva: Mozzarella, Tomate, {ing}.".format(ing = ing)
    
def main():
    eleccion = input("¿Quieres que tu pizza sea vegetariana? (V para Vegetariana, N para Normal): ")
    print(pizzatime(eleccion))
    if __name__ == '__main__':
        main()