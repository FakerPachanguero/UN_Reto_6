# UN - Reto 6
### En este repositorio encontrarás un archivo con toda una serie de funciones que podrás importar en tu proyecto. Adicional a esto habrán una serie de programas haciendo uso de estas funciones.

## PUNTO 1
### Función: calcular el volumen y el area de la figura dada.
```py
# IMPORTS
from Resources.funciones import *

# VARIABLES
rSphere : float
rCone : float
hCone : float

# Devuelve el volumen de la figura [1]
def aFigureVolume(rs:float,rc:float, h:float):
    return sphereVolume(rs) + coneVolume(rc,h)

# Devuelve el area de la figura [1]
def aFigureArea(rs:float,rc:float, h:float):
    return sphereArea(rs) + coneArea(rc,h)

# CODE
if __name__ == "__main__":

    rSphere : float = float(input("Escribe el radio del cirulo: "))
    rCone : float =  float(input("Escribe el radio del cono: "))
    hCone : float =  float(input("Escribe la altura del cono: "))

    print(f"{aFigureArea(rSphere, rCone, hCone)}")
    print(f"{aFigureVolume(rSphere, rCone, hCone)}")
```

## PUNTO 2
### Función: Halla el area y el perímetro de la figura dada.
```py
# IMPORTS
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
```
## PUNTO 3
### Calcula la cantidad total de carne, dado un peso en kilos de gallinas, gallos y pollitos.
```py
# IMPORTS
from Resources.funciones import *

# VARIABLES

gallinas : int
gallos : int
Pollitos : int

# CODE

if __name__ == "__main__":
    
    gallinas = int(input("Ingresa la cantidad de gallinas: "))
    gallos = int(input("Ingresa la cantidad de gallos: "))
    Pollitos = int(input("Ingresa la cantidad de pollitos: "))

    print(f"La cantidad de kilos de carne son: {sadMeat(gallinas, gallos, Pollitos)}Kg")
```
## PUNTO 4
### Determina nuestro balance cuando en la panaderia compramos pan, leche y huevos.
```py
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
```
## PUNTO 5 
### Calcula el valor de un préstamo con un interés compuesto.
```py
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
```
## PUNTO 6 
### Para x día, determina cuantas perosnas van a estar contagiadas dada una población inicial.
```py
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

```
## PUNTO 7 - 8
### Aqui encuentras las funciones del repositorio (TALLER 1), pero en forma de función.
```py



```
## SISTEMA PIP
### PIP - Es es el sistema que utiliza pyhton para gestionar sus paquetes de archivos, Permite instalar y gestionar bibliotecas y paquetes de software desarrollados por la comunidad de Python, así como también distribuciones específicas del lenguaje.

### Con el siguiente codigo podrás instalar el paquete que quieras.
```
pip uninstall nombre_del_paquete
```

### Con el siguiente codigo podrás instalar el paquete que desees. a contiación encontrarás una lista de los más populares
    Requests
        Una librería HTTP de Python que permite realizar peticiones web de manera sencilla y eficiente.
    Pandas
        Proporciona estructuras de datos flexibles y herramientas para el análisis de datos.
    NumPy
        Poderosa librería para el cálculo numérico y manipulación de arrays y matrices.
    Matplotlib
        Librería para la creación de gráficos y visualizaciones de datos en Python.
    Django
        Framework web de alto nivel para el desarrollo rápido y limpio.
    Flask
        Micro-framework web para Python simple y fácil de aprender.
    Scikit-learn
        Librería de aprendizaje automático de código abierto para Python.
    TensorFlow
        Plataforma de código abierto para aprendizaje automático y desarrollo de modelos de aprendizaje profundo.
    PyTorch
        Marco de trabajo de aprendizaje automático que facilita la creación y entrenamiento de modelos de aprendizaje profundo.
    SQLAlchemy
        Herramienta SQL y sistema de mapeo objeto-relacional (ORM) para Python.

