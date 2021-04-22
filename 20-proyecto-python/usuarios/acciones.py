import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\n Ok!! Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu Nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu emaiil: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("n\ No te ha registrado correctamente!!!")

    def login(self):
        print("Identificate en el sistema...")
        
        try:

            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"n/ Bienvenido {login[1]}, te has registrado en el sistema el: {login[5]} ")
                self.proximasAcciones(login)


        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login Incorrecto !!!!")

    def proximasAcciones(self, usuario):  #(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input("Que quieres hacer?: ")
        hasEl = notas.acciones.Acciones()

        if accion == "crear":
            hasEl.crear(usuario)
            
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hasEl.mostrar(usuario)
                        
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a Eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto")
            exit()

  
    
