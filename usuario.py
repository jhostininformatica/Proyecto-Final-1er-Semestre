#Registro de usuario
USUARIO = "jhostin"
CONTRASEÑA = "cine1234"

def iniciar_sesion():

    print("\n INICIAR SESIÓN ")

    usuario = input("Usuario: ") #ingreso del usuario
    contraseña = input("Contraseña: ") #ingreso de la contraseña

    if usuario == USUARIO and contraseña == CONTRASEÑA: 

        print("\n Inicio de sesión exitoso") #continuar si todo esta correcto
        return True

    else:

        print("\n Usuario o contraseña incorrectos") #seguir insistiendo si uno esta incorrecto
        return False
def menu():

    while True:

        print(""" INICIO
1. Iniciar sesión
2. Salir """)
        
        opcion = input("Seleccione una opción: ") #sección de opciones

        if opcion == "1":
            
            acceso = iniciar_sesion()

            if acceso:

                print(""" BIENVENIDO """) #mensaje al ingresar todo correcto
                break

        elif opcion == "SALIR":

            print("\n CHAO PESCAO") #mensaje al salir
            break

        else:

            print("\n Opción inválida") #mensaje al poner otra cosa no ingresable
menu()