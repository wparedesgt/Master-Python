import mysql.connector

#Conectar a base de datos

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "", 
    database = "master_python"
)

#print(database)

#Cursor que permite ejecutar las consultas
cursor = database.cursor(buffered=True)

#Crear bases de datos

"""
cursor.execute("Create database if not exists master_python;")
cursor.execute("Show databases;")


for bd in cursor:
    print(bd)

"""
#Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null, 
    marca varchar(40) not null,
    modelo varchar(40) not null, 
    precio float(10,2) not null, 
    CONSTRAINT pk_vehiculo PRIMARY KEY(id) 
)
""")


cursor.execute("SHOW TABLES;")

for tables in cursor:
    print(tables)


#Insertar datos

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Mercedes', 'C500', 65000)")

"""
carros = [
    ('BMW', '328i', 40000),
    ('Ford', 'F150', 65000),
    ('GMC', 'Sierra', 55000),
    ('Ferrary', 'Testa Rosa', 1500000),
    ('Maceraty', 'Tundra', 500000),
    ('Lamborgini', 'Murcielago', 600000),
    ('Lamborgini', 'countach', 1000000)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", carros)

database.commit()

"""

#Sacar los datos de una tabla

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

for carro in result:
    print(carro)



#Actualizar 

cursor.execute("UPDATE vehiculos SET modelo = '328i' where marca = 'BMW' ")
database.commit()

print(cursor.rowcount, "Actualizados !!!!!")