#Paso 1. IMPORTAR SQLITE
import sqlite3
#Paso 2. Crear la base de datos o conectar con la base de datos
conexion=sqlite3.connect('datos.db')
#Paso 3. Crear el cursor para las solicitudes sql
cursor=conexion.cursor()
#Paso 4. Ejecutar la consulta SQL

nombre=input("Ingrese un nombre: ")
ci=int(input("Ingrese un ci: "))

cursor.execute('''INSERT INTO usuarios (nombre,ci) VALUES (?, ?) ''',(nombre,ci))
#Paso 5. Guardar los cambios de la consulta SQL
conexion.commit()
#Paso 6. Cerrar la conexion
conexion.close()
