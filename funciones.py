import math


# Devuelve el volumen de una esfera
def sphereVolume(r:float):
    return (4 * math.pi*r**3)/3

# Devuelve el area de una esfera
def sphereArea(r:float):
    return 4*math.pi*r**2

# Devuelve el volumen de un cono regular
def coneVolume(r:float, h:float):
    return (h*math.pi*r**2)/3

# Devuelve el area de un cono regular
def coneArea(r:float, h:float):
    return  math.pi*r*(r+((r**2 + h**2)**0.5))

# Calcula el area de un rectángulo
def rectangleArea(a:float, b:float):
    return a * b

# Calcula el perímetro de un rectángulo
def rectanglePerimeter(a:float, b:float):
    return (a*2)+(b*2)

# Calcula el area de un círculo
def circleArea(r:float):
    return math.pi * r**2

# Calcula el perímetro de un circulo
def circlePerimeter(r:float):
    return 2*math.pi*r**2

# Calcula la cantidad de carne en kilos de: gallinass, gallos y pollitos
def sadMeat(ga:int, go:int, po:int):
    return (ga*6)+(go*7)+(po*1)

# Calcula si le debemos al panadero
def deudaConPan (p:int, l:int, h:int, m:int):
    mTotal : int = (p*300)+(l*3300)+(h*350)
    mTotal = m - mTotal
    
    if mTotal < 0:
        return f"Mala suerte, tienes una deuda de {mTotal}$ con el panadero"
    elif mTotal > 200:
        return f"Te Sobrarón {mTotal}$, siguente parada kof98 o lo que este libre"

# Calcula el interes compuesto 
def loan(mi:float, i:float, t:float):
    t = t*(1/12)
    valorTotalPrestamo = mi*(1+t*i)
    return valorTotalPrestamo

# Calcula el número de contagiados para x día a partir de y población
def contagiosNuncaLandia(p:int,c:int,t:int):

    if p > c:
        if c > 0:
            for i in range(0,t + 1):
                c *= 2
                if c >= p:
                    c = p
                    break
        return c
    elif p < c:
        print("Error")
    elif p == c:
        print("Toda la población ya esta contagiada")
    