
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

n = funciones.inicio()  # Solicita al usuario la cantidad de lugares a generar

destinos = funciones.generar_destinos(n)    #Genera lugares con coordenadas "x" e "y" aleatorias

funciones.mostrar_lista(n, destinos)    # Si la lista es pequeña, muestra cada lugar con sus coordenadas

base = funciones.elegir_base(destinos, n)  # Elección del lugar (base) para calcular distancias a los demás puntos

distancias = funciones.calcular_distancia(destinos, base, n)  # Cálculo de distancias desde el lugar elegido a los demás puntos

input("Presione Enter para continuar a la sección de ordenamiento.") 

# =============Ordenamiento de la lista de distancias===================

print("\n=== Ordenamiento de distancias ===")

#Bubble Sort (Ordenamiento por burbuja):
distancias_bubble = ordenamiento.ordenamiento_bubble(distancias.copy()) #Ordenamiento por Burbuja
#Quick Sort (ordenamiento rapido):
distancias_quick = ordenamiento.ordenamiento_quick(distancias.copy())
#Selection Sort (Ordenamiento por seleccion):
distancias_seleccion = ordenamiento.ordenamiento_seleccion(distancias.copy())  #Selection Sort (Ordenamiento por selección)
#Insertion Sort(Ordenamiento por insercion):
distancias_insercion = ordenamiento.ordenamiento_insercion(distancias.copy())  #Insertion Sort (Ordenamiento por inserción)

funciones.mostrar_listas_ordenadas(n,distancias_bubble, distancias_quick, distancias_seleccion, distancias_insercion)   #Muestra las listas ordenadas si son chicas

input("Presione Enter para continuar a la sección de búsqueda.")    

# =============Búsqueda en la lista de distancias===================
#Búsqueda de lugares en la lista. Se muestra la distancia del lugar
print("""\n=== Búsqueda de lugares ===
Ingrese el lugar que desea buscar (Se mostrará la distancia hasta ese lugar, y la posición que ocupa en el ranking de distancias)\n
""")
lugar = input("Lugar: ")
busqueda.busqueda_lineal(distancias_insercion, lugar)

#Búsqueda lineal y binaria en lista ordenada
objetivo = funciones.obtener_objetivo()
busqueda.binaria_mas_cercano(distancias_insercion, objetivo, destinos)
busqueda.lineal_mas_cercano(distancias_insercion, base, objetivo, destinos)
input("Presione Enter para finalizar el programa.")
print("Gracias por utlizar el gestor de distancias de Florencia Vivas y David Vergara. ¡Hasta pronto!")