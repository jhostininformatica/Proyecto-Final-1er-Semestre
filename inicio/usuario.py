USUARIO = "jhostin"
CONTRASEÑA = "cine1234"

def iniciar_sesion():

    print("\n===== INICIAR SESIÓN =====")

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == USUARIO and contraseña == CONTRASEÑA:

        print("\n Inicio de sesión exitoso")
        return True

    else:

        print("\n Usuario o contraseña incorrectos")
        return False
def menu():

    while True:

        print("""
=====================================
             INICIO
=====================================

1. Iniciar sesión
2. Salir

=====================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            acceso = iniciar_sesion()

            if acceso:

                print("""
=====================================
    BIENVENIDO 
=====================================
""")

                break

        elif opcion == "2":

            print("\n Hasta luego")
            break

        else:

            print("\n Opción inválida")
menu()