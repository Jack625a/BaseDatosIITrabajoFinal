import flet as ft
import sqlite3 #Dependencias sqlite

#Configuracion de la base de datos 
#Paso 2. Crear la base de datos o conectar con la base de datos
conexion=sqlite3.connect('datos.db')
#Paso 3. Crear el cursor para las solicitudes sql
cursor=conexion.cursor()
conexion.commit()
conexion.close()

#Funcion para mostrar los datos en la interfaz
def mostrarUsuarios():
    conexion=sqlite3.connect('datos.db')
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios=cursor.fetchall()
    conexion.close()
    return usuarios

#Crear la interface para los datos obtenidos de la base de datos
def mostrarInterfaz():
    usuarios=mostrarUsuarios()

    #crear las tarjetas de los usuarios
    usuariosTarjetas=[
        ft.ResponsiveRow(
            [
                ft.Container(
                    padding=10,
                    expand=True,
                    content=ft.Card(
                        content=ft.Container(
                            padding=10,
                            content=ft.Column(
                                [
                                    ft.Text(value=usuarios[1],size=30,weight=ft.FontWeight.BOLD),
                                    ft.Text(value=usuarios[2])
                                ]
                            ),
                        ),
                        
                    ),
                )
            ],
            col={"xs":6,"md":3,"lg":3}, #organizar 2 columnas para pantallas pequeñas y 4 columnas para pantallas medianas y grandes

        )
        for usuario in usuarios

    ]
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column([
            ft.Text(value="Pantalla Datos obtenidos",size=35),
            ft.ResponsiveRow(usuariosTarjetas,spacing=10)
        ],
        alignment="center",
        spacing=20           
        ),
    )




ft.app(main)
