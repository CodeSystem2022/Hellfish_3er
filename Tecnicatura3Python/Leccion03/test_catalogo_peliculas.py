from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar Película")
        print("2. Listar las Películas")
        print("3. Eliminar catálogo de Películas")
        print("4. Salir ")

        opcion = int(input("Introduzca una opción de menú (1-4): "))

        if opcion == 1:
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f"Ocurrió un error de tipo: {e}")
        opcion = None

    else:
        print("Salimos del programa")
