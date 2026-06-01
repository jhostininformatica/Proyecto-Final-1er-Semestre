usuario_guardado = ""
contraseña_guardada = ""
def registrar_usuario():#registro de usuario
    global usuario_guardado#usuario guardado
    global contraseña_guardada#contraseña guardada
    print(" REGISTRO ")
    usuario_guardado = input("Crear usuario: ").strip()#guardar nuevo usuario
    contraseña_guardada = input("Crear contraseña: ").strip()#guardar nueva contraseña
    print(" Usuario registrado correctamente")

def iniciar_sesion():
    print(" INICIAR SESIÓN ")
    usuario = input("Usuario: ").strip()#pedir usuario
    contraseña = input("Contraseña: ").strip()#pedir contraseña
    if usuario == usuario_guardado and contraseña == contraseña_guardada:#mostrar si ambos se cumplen
        print(" Acceso concedido")
        return True
    else:
        print(" Usuario o contraseña incorrectos")
        return False
peliculas_vistas = 0
while True:
    print("""  INICIO 
          
1. Iniciar sesión
2. Registrarse
3. Salir""")
    opcion = input("Seleccione una opción: ").strip()#seleccion de opciones   
    if opcion == "1":#iniciar sesión
        if iniciar_sesion():
            while True:
                print("""   LETTERBOXD
                       
1. Ver catálogo
2. Ver cantidad de catálogos vistos
3. Cerrar sesion""")
                opcion_menu = input("Seleccione una opción: ").strip()#seleccion de opciones del segundo panel               
                if opcion_menu == "1":#mostrar catálogo de las peliculas
                    print(" CATÁLOGO ")
                    print("1. Eternal Sunshine of the Spotless Mind")
                    print("2. All the Bright Places")
                    print("3. Ruby Sparks")
                    print("4. Scott Pilgrim vs. the World")
                    print("5. The Girl Next Door")
                    peliculas_vistas += 1                
                elif opcion_menu == "2":#mostrar contador de peliculas vistas
                    print(f" Catálogos vistos: {peliculas_vistas}")                
                elif opcion_menu == "3":#cerrar sesión
                    print(" Cerrando sesión...")
                    break
                else:
                    print(" Opción inválida")   
    elif opcion == "2":#registrarse
        registrar_usuario()
    elif opcion == "3" or opcion == "SALIR": #sale del sistema
            print("Calabaza calabaza 🎃 cada quien para su casa ")
            break
    else:
        print(" Opción inválida")