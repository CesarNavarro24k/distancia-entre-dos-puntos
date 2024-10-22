import random
import time
import numpy as np
while True:
    time.sleep(1)
    print(f"Bienvenidos a este programa, vamos a calcular la distancia entre dos puntos")
    time.sleep(1)
    p1 = float(input("Ingresa el valor para el primer punto:"))
    time.sleep(1)
    p2 = float(input("Ingresa el valor para el segundo punto:"))
    time.sleep(1)
    print("Los otros dos valores son aleatorios")
    time.sleep(1)
    p3 = random.randint(1,100)
    p4 = random.randint(10,200)
    time.sleep(1)
    print(f"Tus valores ingresados son: {p1} y {p2}, los valores 3 y 4 son aleatorios y son :{p3} y {p4}")
    def distancia(x1,x2,y1,y2):
        dis = np.sqrt((x2 - x1 )**2 + (y2 - y1)**2)
        return dis
    time.sleep(1)
    print(f"El valor de la distancia, para los puntos ingresados es:{distancia(p1,p2,p3,p4)}")
    time.sleep(1)
    pre = input("Te gustaria colocar nuevamente numeros:")
    if pre == "no":
        break
