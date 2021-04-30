
import psycopg2

conn = psycopg2.connect(
    host="10.0.0.17",
    database="postgres",
    user="postgres",
    password="Mingob2021")

try:


    #Crea el Cursor

    cur = conn.cursor()

    # Ejecuta prueba de Conexion

    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    #Imprime la version de postgres

    db_version = cur.fetchone()
    print(db_version)
        
    # Cierra la comunicacion
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Conexion terminada')
