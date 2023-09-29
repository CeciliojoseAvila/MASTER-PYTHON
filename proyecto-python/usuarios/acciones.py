import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema...")
        nombre = input("\n¿Cuál es tu nombre?: ")
        apellidos = input("\n¿Cuales son tus apellidos?: ")
        email = input("\nIngresa tu email: ")
        password = input("\nIngresa tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\nVale!! Identificate en el sistema...")

    try:
        email = input("\nIngresa tu email: ")
        password = input("\nIngresa tu contraseña: ")

        usuario = modelo.Usuario('', '', email, password)
        login = usuario.Identificar()

        if email == login[3]:
            print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
            self.proximasAcciones(login)

    except Exception as e:
        print(type(e))
        print(type(e).__name__)
        print(f"Login incorrecto!! intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
              - Crear nota (crear)
              - Mostrar tus notas (mostrar)
              - Eliminar nota (eliminar)
              - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")

        if accion == "crear":
            print("Vamos a crear")
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            exit()

