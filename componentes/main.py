import flet as ft
#Importar las pantallas de cada opcion
from pantallaInicio import mostrarInterfaz
from pantallaProductos import mostrarPantallaProductos
from pantallaServicios import mostrarPantallaServicios
from pantallaPerfil import mostrarPantallaPerfil
from pantallaNotificaciones import mostrarPantallaNotificaciones
from pantallaUbicacion import mostrarPantallaUbicacion



def main(page: ft.Page):
     #Variables
    page.title="Trabajo Final "
    
    navegacion=ft.Tabs(
        selected_index=0,
        animation_duration=500,
    
        tabs=[
            ft.Tab(text="Inicio",icon=ft.icons.HOME,content=mostrarInterfaz()),
            ft.Tab(text="Productos",icon=ft.icons.SHOPPING_BASKET,content=mostrarPantallaProductos()),
            ft.Tab(text="Servicios",icon=ft.icons.HOME_REPAIR_SERVICE,content=mostrarPantallaServicios()),
            ft.Tab(text="Perfil",icon=ft.icons.PERSON_4, content=mostrarPantallaPerfil()),
            ft.Tab(text="Notificaciones", icon=ft.icons.NOTIFICATIONS_ACTIVE_SHARP,content=mostrarPantallaNotificaciones()),
            ft.Tab(text="Ubicacion", icon=ft.icons.LOCATION_PIN,content=mostrarPantallaUbicacion())

        ],expand=1
        )

    page.add(navegacion)

ft.app(main)
