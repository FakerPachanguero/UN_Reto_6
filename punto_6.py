# IMPORTS
from Resources.funciones import *
import sys


# VARIABLES
poblacion : int
contagiados : int
dias : int

# CODE
if __name__ == "__main__":

    poblacion = int(input("Ingresa la población de NuncaLandia: "))
    contagiados = int(input("Ingresa la población inicial de contadiados: "))
    if contagiados > poblacion:
        print("Error: los números de infectados es superior a la población total de la NuncaLandia")
        sys.exit()
    dias = int(input("Ingresa los dias: "))

    print(f"El número total de contagiados para detntro de {dias} dias, es de: {contagiosNuncaLandia(poblacion, contagiados, dias)}")
76