# IMPORTS
from Resources.funciones import *


# VARIABLES
capital : float
interes : float
tiempo : float


# CODE
if __name__ == "__main__":

    capital = float(input("Ingresa la cantidad del prestamo: "))
    interes = float(input("Ingresa la cantidad de interes intervalo(1 - 0): "))
    tiempo = float(input("Ingresa la cantidad de tiempo en meses: "))

    print(f"El valor total de tu prestamo es de: {loan(capital, interes, tiempo)}")