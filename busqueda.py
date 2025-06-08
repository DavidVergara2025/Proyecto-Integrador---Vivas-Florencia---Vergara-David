#Busqueda lineal de un lugar en la lista de distancias
def busqueda_lineal(distancias, lugar):
    for i in distancias:
        if i[0].lower() == lugar.lower():
            return i
    if lugar.lower() not in [i[0].lower() for i in distancias]:
        print(f"{lugar} no se encuentra en la lista.")
        return None  # Si no se encuentra el lugar, devuelve None