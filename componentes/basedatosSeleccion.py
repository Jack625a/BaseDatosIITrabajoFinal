#Paso 1. Importar sqlite3
import sqlite3
#Paso 2. Conectar con la base de datos
conexion=sqlite3.connect('datos.db')
#Paso 3. Crear el cursor
cursor=conexion.cursor()
#Paso 4. Ejecutar la consulta SQL
cursor.execute('''SELECT * FROM usuarios ''')
#Paso 5. Obtencion de los registros (todos)
usuarios=cursor.fetchall()
#Paso 6. Mostrar los datos de la tabla
for usuario in usuarios:
    print(f"ID: {usuario[0]} -  Nombre: {usuario[1]} - Ci: {usuario[2]}")

#Paso 7. Cerrar la conexion
conexion.close()

