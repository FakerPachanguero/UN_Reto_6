# IMPORTS
from Resources.funciones import *


# VARIABLES
pan : int
leche : int
huevos : int
money : int


# CODE
if __name__ == "__main__":

    pan = int(input("Ingresa cuántos panes vas a comprar: "))
    leche = int(input("Ingresa cuántas bolsas de leche vas a comprar: "))
    huevos = int(input("Ingresa cuántos huevos vas a comprar: "))
    money = int(input("Ingresa la cantidad de dinero: "))

    print(deudaConPan(pan, leche, huevos, money))