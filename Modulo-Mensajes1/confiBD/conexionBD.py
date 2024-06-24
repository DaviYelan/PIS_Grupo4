# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
from mysql.connector.errors import Error

def connectionBD():
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="shifusql",
            database="sala_chat"
        )
        if connection.is_connected():
            # print("Conexión exitosa a la BD")
            return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a la BD: {e}")
