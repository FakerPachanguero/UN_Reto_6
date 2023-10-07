
from Resources.funciones import *

# VARIABLES
rSphere : float
rCone : float
hCone : float

# Devuelve el volumen de la figura [1]
def figureVolume(rs:float,rc:float, h:float):
    return sphereVolume(rs) + coneVolume(rc,h)

# Devuelve el area de la figura [1]
def figureArea(rs:float,rc:float, h:float):
    return sphereArea(rs) + coneArea(rc,h)

# CODE
if __name__ == "__main__":

    rSphere : float = float(input("Escribe el radio del cirulo: "))
    rCone : float =  float(input("Escribe el radio del cono: "))
    hCone : float =  float(input("Escribe la altura del cono: "))

    print(f"{figureArea(rSphere, rCone, hCone)}")
    print(f"{figureVolume(rSphere, rCone, hCone)}")

