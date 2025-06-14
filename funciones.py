import random
import math

def inicio():
    n = 0
    while n <= 0:  # Manejo de errores de datos de entrada
        try:  
            n = int(input("Ingrese la cantidad de lugares a generar: \n"))
            if n <= 0:
                print("Ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número positivo válido.")
    return n

#Si la lista es chica, se muestra por pantalla
def mostrar_lista(n, destinos):
    if n < 20:
        for i in destinos:
            print(f"{i['Lugar']}, Coordenadas: ({i['x']}, {i['y']})")  
    else:
        print("La lista fue guardada pero es demasiado extensa para mostrarla por pantalla")

#Genera una lista de lugares con coordenadas aleatorias
def generar_destinos(n):
    destinos = []
    for i in range(1, n+1):
        destino = {
            "Lugar" : f"Lugar {i}",
            "x" : random.randint(0, 1000000),
            "y" : random.randint(0, 1000000)
        }
        destinos.append(destino) #Se agrega cada lugar generado con sus coordenadas a la lista destinos
    return destinos

#Devuelve el elemento elegido por el usuario (Lugar y coordenadas)
def elegir_base(destinos, n):
    base = 0
    print(f"\nElija su ubicación (número entre 1 y {len(destinos)}) para calcular la distancia a los demas puntos: \n")
    while base <= 0 or base > n : 
        try:
            base = int(input("\nLugar: "))
            if base <= 0 or base > n :
                print("Valor incorrecto.")
            else:
                print(f"Lugar elegido : {base}(x : {destinos[base -1]['x']}, y :{destinos[base -1]['y']})")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
    return destinos[base -1]

#Cálculo de las distancias desde cada punto al elegido por el usuario (con teorema de pitágoras)
def calcular_distancia(destinos, base, n):
    distancias = []
    for i in destinos:
        x2 = i["x"]
        y2 = i["y"]
        x1 = base["x"]
        y1 = base["y"]
        distancia = round((math.sqrt((x2-x1)**2 + (y2-y1)**2)), 2)
        distancias.append((i["Lugar"], distancia)) #Va formando una lista de tuplas con el nombre del lugar y la distancia calculada
    if n < 20:
        input("Presione Enter para ver las distancias desde este lugar.") 
        for i in distancias:
            print(f"{i[0]}, Distancia: {i[1]}") # Muestra el lugar y la distancia calculada desde el lugar elegido
    else : print("Se guardaron las distancias, pero la lista es demasiado grande para mostrarse")
    return distancias #Devuelve la lista de tuplas 

def mostrar_listas_ordenadas(n, distancias_bubble, distancias_quick, distancias_seleccion, distancias_insercion): 
    if n < 15:
        input("Presione Enter para continuar.")
        print("\nLista ordenada por Bubble sort:")
        for i in distancias_bubble:
            print(f"{i[0]}, Distancia: {i[1]}")
        input("Presione Enter para continuar.")
        print("\nLista ordenada por quick sort:")
        for i in distancias_quick:
            print(f"{i[0]}, Distancia: {i[1]}")   
        input("Presione Enter para continuar")
        print("\nLista ordenada por selección:")
        for i in distancias_seleccion:
            print(f"{i[0]}, Distancia: {i[1]}")
        input("Presione Enter para continuar.")
        print("\nLista ordenada por inserción:")
        for i in distancias_insercion:
            print(f"{i[0]}, Distancia: {i[1]}")      
        return None
    
def obtener_objetivo():
    print("A continuación, puede buscar la distancia más cercana a un valor objetivo mediante búsqueda binaria y lineal.")        
    # Se solicita al usuario la distancia deseada
    objetivo = -1
    while objetivo < 0:
        try:
            objetivo = float(input("Ingrese la distancia que desea buscar (se mostrará el lugar más cercano): "))
            if objetivo < 0:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")  
    return objetivo
