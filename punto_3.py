from Resources.funciones import *

# VARIABLES

gallinas : int
gallos : int
Pollitos : int

# CODE

if __name__ == "__main__":
    
    gallinas = int(input("Ingresa la cantidad de gallinas: "))
    gallos = int(input("Ingresa la cantidad de gallos: "))
    Pollitos = int(input("Ingresa la cantidad de pollitos"))

    print(f"La cantidad de kilos de carne son: {sadMeat(gallinas, gallos, Pollitos)}Kg")