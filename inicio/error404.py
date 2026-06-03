usuario_guardado = ""#variables globales
contraseña_guardada = ""
peliculas_vistas = 0#variable de peliculas
peliculas = {
    "Interstellar": "Ciencia ficción",
    "Entre Navajas y Cuchillos": "Ciencia ficción",
    "Guardianes de la Galaxia": "Acción",
    "Son Como Niños 2 ": "Comedia",
    "Ruby Sparks": "Romance",
    "La Chica de al Lado": "Romance",
    "500 dias con Summer": "Romance",
    "Maze Runner": "Acción",
    "Ponyo": "Animación",
    "Cadaver de la novia": "Animación",
    "Inmaculada": "Terror",
    "It ": "Terror",
    "Blade Runner 2049 ": "Ciencia ficiión",
    "Lightyear ": "Animación",
    "El Show de Truman ": "Drama",
    "Eterno Resplandor de una Mente Sin Recuerdos ": "Romance",
    "El Abismo ": "Romance",
    "Flow ": "Animación",
    "Cherry ": "Drama",
    "¿Dónde estan las rubias? ": "Comedia",
    "Tren Bala ": "Acción",
    "Son Como Niños ": "Comedia",
    "Weapons ": "Terror",
    "Un Hombre Llamado Otto ": "Drama",
    "La Sustancia ": "Terror",
    "La Hermanastra Fea ": "Drama",
    "En Busca de la Felicidad ": "Drama",
    "El Hogar de Miss Peregrine  ": "Ciencia ficción",
    "A Dos Metros de Ti ": "Romance",
    "Mr. Smith & Mrs. Smith ": "Drama",
    "Violeta y Finch ": "Romance",
}
calificaciones = {}
def registrar_usuario():#registro de usuario
    global usuario_guardado#usuario guardado
    global contraseña_guardada#contraseña guardada
    print(" REGISTRO ")
    usuario_guardado = input("Crear usuario: ").strip()#guardar nuevo usuario
    contraseña_guardada = input("Crear contraseña: ").strip()#guardar nueva contraseña
    print(" Usuario registrado correctamente ")
def iniciar_sesion():
    print(" INICIAR SESIÓN ")
    usuario = input("Usuario: ").strip()#pedir usuario
    contraseña = input("Contraseña: ").strip()#pedir contraseña
    if usuario == usuario_guardado and contraseña == contraseña_guardada:#mostrar si ambos se cumplen
        print(" Acceso concedido ")
        return True
    else:
        print(" Usuario o contraseña incorrectos ")#mostrar si no se cumple
        return False
while True:
    print("""  INICIO 
          
1. Iniciar sesión
2. Registrarse
3. Salir """)
    opcion = input("Seleccione una opción: ").strip()#seleccion de opciones del primer plano  
    if opcion == "1":#iniciar sesión
        if iniciar_sesion():
            while True:
                print("""   LETTERBOXD
                       
1. Ver catálogo
2. Calificar película
3. Ver mis calificaciones
4. Agregar película
5. Ver cantidad de catálogos vistos
6. Ver recomendaciones
7. Cerrar sesión """)           
                opcion_menu = input("Seleccione una opción: ").strip()#selección de opciones del segundo plano
                if opcion_menu == "1":#mostrar catálogo
                    print("CATÁLOGO ")
                    for pelicula, categoria in peliculas.items():
                        print(f" {pelicula} - {categoria}")#mostrar la pelicula con su género correspondiente 
                    peliculas_vistas += 1 #sumar al agregar como pelicula vista
                elif opcion_menu == "2":#sección para calificar la película
                    pelicula = input("Nombre de la película: ").strip()#ingresa el nombre de la pelicula recien vista
                    nota = int( input("Calificación (1-5): "))#calificar de 1 a 5 estrellas
                    if nota >= 1 and nota <= 5: #definir cual es su calificación
                        calificaciones[pelicula] = nota
                        print( "Calificación guardada")#mostrar despues de calificar
                    else:
                        print(" La nota debe estar entre 1 y 5")#mostrar si se ingresa otra calificacion que no sea <5
                elif opcion_menu == "3":#mostrar las calificaciones ya guardadas
                    print(" MIS CALIFICACIONES ")
                    if len(calificaciones) == 0:#mostra las calificaciones ya guardadas 
                        print("No hay películas calificadas")#mostrar si no calificaste ninguna 
                    else:
                        for pelicula, nota in calificaciones.items():#mostrar la película y su calificación
                            print( f"{pelicula} -> {nota}⭐")
                elif opcion_menu == "4":#sección para agregar alguna pélicula nueva
                    nueva_pelicula = input("Ingrese la película: ")#pedir la película
                    nueva_pelicula = (nueva_pelicula.replace("_", " "))
                    categoria = input(" Categoría: ").strip()#pedir su categoria
                    peliculas[nueva_pelicula] = categoria#mostar lo agregado
                    print("Película agregada correctamente")
                elif opcion_menu == "5":#ver la cantidad de vistos
                    print( f" Catálogos vistos: "
                        f"{peliculas_vistas}")#sumar al agregar otra película vista
                elif opcion_menu == "6":#mostrar las recomendaciones segun la categoria agregada
                    if len(calificaciones) == 0:
                        print(" Primero debes " "calificar películas ")#mostar si no se cumple
                    else:
                        gustos = {}#enlazar dependiendo la calificación de cada pelicula
                        for pelicula, nota in calificaciones.items():
                            if pelicula in peliculas:
                                categoria = peliculas[pelicula]#recomendar dependiendo las calificaciones mas altas
                                if categoria not in gustos:
                                    gustos[categoria] = 0
                                gustos[categoria] += nota#mostrar la catagoria deoendiendo las calificaciones anteriores
                        categoria_favorita = max(gustos, key=gustos.get )#categoria mas alta
                        print(" RECOMENDACIONES ")
                        print(f" Género favorito: " f"{categoria_favorita}")#mostrar el género favorita depende el rank mas alto
                        for pelicula, categoria in peliculas.items():#guardar la categoria agregada
                            if categoria == categoria_favorita:
                                if pelicula not in calificaciones:
                                    print(" película ") 
                elif opcion_menu == "7": #cerrar sesión
                    print(" Cerrando sesión...")
                    break
                else:
                    print(" Opción inválida" )#mostrar al no cumplir con ninguno
    elif opcion == "2":#registrarse
        registrar_usuario()#mandar a la variable de registro
    elif opcion == "3" or opcion == "SALIR": #sale del sistema
            print(" Calabaza, calabaza 🎃 cada quien para su casa ")#mensaje de salida
            break#romper todo el codigo
    else:
        print(" Opción inválida. ")#mostrar al no cumplir con ninguno