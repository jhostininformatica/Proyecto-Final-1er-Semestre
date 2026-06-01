usuario_guardado = ""
contraseña_guardada = ""
def registrar_usuario():#registro de usuario
    global usuario_guardado
    global contraseña_guardada
    print(" REGISTRO ")
    usuario_guardado = input("Crear usuario: ").strip()
    contraseña_guardada = input("Crear contraseña: ").strip()
    print(" Usuario registrado correctamente")

def iniciar_sesion():
    print(" INICIAR SESIÓN ")
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    if usuario == usuario_guardado and contraseña == contraseña_guardada:
        print(" Acceso concedido")
        return True
    else:
        print(" Usuario o contraseña incorrectos")
        return False
peliculas_vistas = 0
while True:
    print(""" INICIO 
          
1. Iniciar sesión
2. Registrarse
3. Salir""")
    opcion = input("Seleccione una opción: ").strip()   
    if opcion == "1":# Iniciar sesión
        if iniciar_sesion():
            while True:
                print(""" LETTERBOXD
                       
1. Ver catálogo
2. Ver cantidad de catálogos vistos
3. Cerrar sesion""")
                opcion_menu = input("Seleccione una opción: ").strip()               
                if opcion_menu == "1":# Mostrar catálogo
                    print(" CATÁLOGO ")
                    print("1. Interstellar")
                    print("2. Titanic")
                    print("3. John Wick")
                    print("4. Toy Story")
                    print("5. The Conjuring")
                    peliculas_vistas += 1                
                elif opcion_menu == "2":# Mostrar contador
                    print(f" Catálogos vistos: {peliculas_vistas}")                
                elif opcion_menu == "3":# Cerrar sesión
                    print(" Cerrando sesión...")
                    break
                else:
                    print(" Opción inválida")   
    elif opcion == "2":# Registrarse
        registrar_usuario()
    elif opcion == "3":#salir
        print(" Cerrando sistema...")
        break
    else:
        print(" Opción inválida")