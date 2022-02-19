from os import close
import sqlite3

miconexion = sqlite3.connect('Usuarios')
micursor = miconexion.cursor()
micursor.execute('''CREATE TABLE DATOS(
         NOMBRE_ARTICULOS VARCHAR(50),
         PRECIO INTEGER,
         SECCION VARCHAR(50))'''
                 )

miconexion.close()
