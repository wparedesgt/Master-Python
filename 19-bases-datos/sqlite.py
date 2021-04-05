import sqlite3

#Conexión

conexion = sqlite3.connect('19-bases-datos/pruebas.db')

#Crear cursor

cursor = conexion.cursor()

#Crear tabla

cursor.execute("CREATE TABLE IF NOT EXISTS  productos(" +
"id INTEGER PRIMARY KEY autoincrement, " +
"titulo VARCHAR(255), "  +
"descripcion TEXT, "  +
"precio int(255)" + ")")

#Guardar Cambios

conexion.commit()

"""

#Insertar datos

cursor.execute("insert into productos values(null, 'Primer Producto', 'Descripcion de mi Producto', 550)")
conexion.commit()

"""

##Borrar Registros

cursor.execute("Delete from productos;")
conexion.commit()




#Lectura de datos

cursor.execute("select * from productos;")

productos = cursor.fetchall()

for producto in productos:
    print("Titulo: ",  producto[1])
    print("Descripcion: ",   producto[2])
    print("Precio: ", producto[3])




cursor.execute("select titulo from productos;")
producto = cursor.fetchone()
print(producto)


#Cerrar conexion
conexion.close()



