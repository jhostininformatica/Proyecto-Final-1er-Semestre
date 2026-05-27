usuario_guardado = ""
contraseña_guardada = ""
def registrar_usuario(): #registro de usuario
    global usuario_guardado, contraseña_guardada
    print(" REGISTRO ")
    usuario_guardado = input("Crear usuario: ").strip()#usuario nuevo
    contraseña_guardada = input("Crear contraseña: ").strip()#contraseña nueva
    print("Usuario registrado correctamente.")
def iniciar_sesion():#número de intentos
    intentos_maximos = 3
    intentos = 0  
    while intentos < intentos_maximos:
        print(f" INICIAR SESIÓN (Intento {intentos + 1}/{intentos_maximos}) ")
        usuario = input("Usuario: ").strip()#pedir usuario
        contraseña = input("Contraseña: ").strip()#pedir contraseña      
        if usuario == usuario_guardado and contraseña == contraseña_guardada:#continuar si ambas opciones se cumplen
            print("Acceso concedido.")#cerrar el maximo de intentos
            return True
        else:
            intentos += 1 #restar un intento al fallar 
            intentos_restantes = intentos_maximos - intentos
            print("Usuario o contraseña incorrectos.")
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intentos.") #mostrar el número de intentos restantes          
    print("Acceso bloqueado. Has superado el límite de intentos.") #mostrar cuando ya no queden intentos
    return False
def menu(): #pantalla del menú
     while True:
        print("""    INICIO 
        1. Iniciar sesión
        2. Salir """)
        
        opcion = input("Seleccione una opción: ").strip().upper()#seleccion de opcion
        
        if opcion == "1":     
            if iniciar_sesion():
                print(" BIENVENIDO ")
                break 
        elif opcion == "2" or opcion == "SALIR": #sale del sistema
            print("Calabaza calabaza 🎃 cada quien para su casa ")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
registrar_usuario()
menu()

