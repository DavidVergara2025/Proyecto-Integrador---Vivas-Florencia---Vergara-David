
import funciones
import ordenamiento
import busqueda

print("""========PROYECTO INTEGRADOR - PROGRAMACIÓN I=========
        2025 - UTN - TUPaD 
        Autores: Vivas, Florencia - Vergara, David
      
        Bienvenido al gestor de distancias entre lugares.
        Este programa genera una lista de lugares con coordenadas aleatorias.
        Luego, el usuario puede elegir uno de ellos para calcular la distancia a los demás puntos.
        A continuación, se ordena la lista mediante distintos métodos de ordenamiento, se comparan 
        los tiempos de ejecución y se permiten realizar búsquedas.
      """)

n = funciones.inicio()
destinos = funciones.generar_destinos(n)    #Genera lugares con coordenadas "x" e "y" aleatorias

funciones.mostrar_lista(n, destinos)    # Si la lista es pequeña, muestra cada lugar con sus coordenadas

base = funciones.elegir_base(destinos)  # Elección del lugar (base) para calcular distancias a los demás puntos

 # Pausa para que el usuario pueda leer el lugar elegido antes de continuar

# Cálculo de distancias desde el lugar elegido a los demás puntos
distancias = funciones.calcular_distancia(destinos, base, n)

input("Presione Enter para continuar a la sección de ordenamiento.") 

# =============Ordenamiento de la lista de distancias===================
print("\n=== Ordenamiento de distancias ===")

#Bubble Sort (Ordenamiento por burbuja):
distancias_bubble = ordenamiento.ordenamiento_bubble(distancias.copy()) #Ordenamiento por Burbuja
#Quick Sort (Ordenamiento rápido):

distancias_seleccion = ordenamiento.ordenamiento_seleccion(distancias.copy())  #Selection Sort (Ordenamiento por selección)

distancias_insercion = ordenamiento.ordenamiento_insercion(distancias.copy())  #Insertion Sort (Ordenamiento por inserción)

funciones.mostrar_listas_ordenadas(n, distancias_seleccion, distancias_insercion,distancias_bubble)   #Muestra las listas ordenadas si son chicas

input("Presione Enter para continuar a la sección de búsqueda.")    

# =============Búsqueda en la lista de distancias===================
print("""\n=== Búsqueda de lugares ===
      Ingrese el lugar que desea buscar (Se mostrará la distancia hasta su ubicación, y la posición que ocupa en el ranking de distancias)\n
      """)
lugar = input("Lugar: ")

