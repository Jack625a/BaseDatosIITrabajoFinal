#Paso 1. IMPORTAR SQLITE
import sqlite3
#Paso 2. Crear la base de datos o conectar con la base de datos
conexion=sqlite3.connect('datos.db')
#Paso 3. Crear el cursor para las solicitudes sql
cursor=conexion.cursor()
#Paso 4. Ejecutar la consulta SQL - Crear la tabla (Usuarios (idUsuario, nombre, ci))
cursor.execute('''CREATE TABLE productos (idProducto INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, precio INTEGER NOT NULL) ''')
#Paso 5. Guardar los cambios de la consulta SQÑ
conexion.commit()
#Paso 6. Cerrar la conexion
conexion.close()
