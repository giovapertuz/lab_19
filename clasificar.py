#programa para clasificar puntos

n=int(input("Ingrese la cantidad de puntos a procesar(De 1 a 4: "))
cant1=0
cant2=0
cant3=0
cant4=0


for i in range(n):
    print(f"punto {i+1}")
    x=int(input("Ingrese la coordenada x: "))
    y=int(input("Ingrese la coordenada y: "))
    #determinar en que cuadrante se encuentra el punto
    if x>0 and y>0:
        cant1+=1 
    elif x<0 and y>0:
        cant2+=1 
    elif x<0 and y<0:
        cant3+=1 
    elif x>0 and y <0:
        cant4+=1 
    else:
        print(" el punto no es valido")
#mostrar resultados
print(f"punto en el primer cuadrante: {cant1}")
print(f"punto en el segundo cuadrante: {cant2}")
print(f"punto en el tercer cuadrante: {cant3}")
print(f"punto en el cuarto cuadrante: {cant4}")

