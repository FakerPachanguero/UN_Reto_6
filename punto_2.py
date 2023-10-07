from Resources.funciones import *

# VARIABLES
Rectangle : float
bRectangle : float
radio : float

# FUNTIONS

def figureArea(a:float, b:float, r:float):
    rectangleArea(a, b) + circleArea(r)*2

def figurePerimter(a:float, b:float, r:float):
    rectanglePerimeter(a, b) + circlePerimeter(r)*2
    
# CODE
if __name__ == "__main__":

    aRectangle : float = float(input("Escribe el lado A del rectángulo: "))
    bRectangle: float =  float(input("Escribe el lado B del rectángulo: "))
    radio : float =  float(input("Escribe el radio de los circulos: "))

    print(f"el are")