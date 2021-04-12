import mysql.connector

#Conectar a base de datos

def conectar():


    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "W1ll1@m2021",
        database = "master_python", 
        port = 3306
    )

    cursor = database.cursor(buffered = True)

    return [database, cursor]


