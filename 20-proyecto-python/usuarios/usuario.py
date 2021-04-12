
import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
                 
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        
        fecha = datetime.datetime.now()
        #Cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('UTF8'))


        sql = "INSERT INTO usuarios VALUES(null,%s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

                    
        return result

    def identificar(self):
        #Consulta de comprobacion de usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        #Cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('UTF8'))
        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result



        
    