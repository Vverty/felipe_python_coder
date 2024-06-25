import re  #Se importa el módulo de expresiones regulares para validar la contraseña.

def registrar_usuario(usuarios):
    #Funcion para reistrar nuevo usuario.
    def validar_contrasena(password):
        #Funcion para validar si una contraseña cumple con los requisitos minimos.
        errores = []  #Lista para acumular los mensajes de error.

        #Requisitos mínimos:
        min_longitud = 12  #Longitud mínima de la contraseña.
        if len(password) < min_longitud:
            errores.append(f"La contraseña debe tener al menos {min_longitud} caracteres.")

        if not re.search("[A-Z]", password):
            errores.append("La contraseña debe contener al menos una letra mayúscula.")

        if not re.search("[a-z]", password):
            errores.append("La contraseña debe contener al menos una letra minúscula.")

        if not re.search("[0-9]", password):
            errores.append("La contraseña debe contener al menos un número.")

        if not re.search("[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+", password):
            errores.append("La contraseña debe contener al menos un símbolo especial.")

        if errores:
            return False, errores
        else:
            return True, ["Contraseña válida."]

    #Sirve para registrar un nuevo usuario en el diccionario con username y contraseña.
    while True:
        username = input("Ingrese el nombre de usuario: ")

        if username in usuarios:
            print("El usuario ya existe. Intente con otro nombre de usuario.")
        else:
            break

    while True:
        password = input("Ingrese la contraseña: ")

        es_valida, mensajes = validar_contrasena(password)
        if es_valida:
            break
        else:
            print("La contraseña no cumple con los siguientes requisitos:")
            for mensaje in mensajes:
                print(f"- {mensaje}")

    usuarios[username] = password

    print(f"Usuario {username} registrado exitosamente.")

def mostrar_usuarios(usuarios):
    #Muestra todos los username registrados.
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("Usuarios registrados:")
    for username in usuarios.keys():
        print(f"- {username}")

def login_usuario(usuarios):
    #Permite iniciar sesión con usuarios y contraseña.
    while True:
        username = input("Ingrese su nombre de usuario: ")

        if username not in usuarios:
            print("El usuario no está registrado.")
        else:
            break

    while True:
        password = input("Ingrese su contraseña: ")

        if usuarios[username] == password:
            print("Login exitoso.")
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente.")

def menu():
    #Permite generar un menu de opciones para que el usuarios final vaya interactuando con las diferentes funciones.
    usuarios = {}

    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Login de usuario")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            mostrar_usuarios(usuarios)
        elif opcion == '3':
            login_usuario(usuarios)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
