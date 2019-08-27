from django.urls import path
from .views import login, home, logout, agregar, regis, borrar, editar, modific, logs, show_account,add_account, forbidden

urlpatterns = [
    path('', login),
    path('home/', home),
    path(r'logout/', logout),
    path('Agregar/', agregar),
    path('Registro/', regis),
    path('show_account/', show_account),
    path('add_account/', add_account),
    path('borrar/<int:registro_id>', borrar),
    path('editar/<int:registro_id>', editar),
    path('modificar_cuenta/', modific),
    path('logs/', logs),
    path('forbidden/', forbidden)
]