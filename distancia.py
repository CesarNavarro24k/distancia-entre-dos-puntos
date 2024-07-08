import numpy as np 
while True:
    def distancia_dos(p1,p2):
        disx = p1[0] - p2[0]
        disy = p1[1] - p2[1]
        dist_T = np.sqrt(disx**2 + disy**2  )
        return dist_T
    print("Bienvenido al programa que te calcula la distancia entre los numeros ingresados enteros")
    x1 = int(input("Ingresa tu primer numero:"))
    x2 = int(input("Ingresa tu segundo numero:"))
    x3 = int(input("Ingresa tu tercer numero:"))
    x4 = int(input("Ingresa tu cuarto numero:"))
    print("La distancia para los numeros que has ingresado es:")
    print(distancia_dos([x1,x2],[x3,x4]))
    question = input("Quieres salir del programa?")
    if question == "si":
        break