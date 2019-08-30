from django.urls import path
from .views import login, home, logout, agregar, regis, borrar, editar, modific, logs, show_account,add_account,\
    forbidden , add_staff , remove_staff , add_active , remove_active, OrderListJson

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
    path('forbidden/', forbidden),
    path('add_staff/<int:pk>', add_staff),
    path('remove_staff/<int:pk>', remove_staff),
    path('add_active/<int:pk>', add_active),
    path('remove_active/<int:pk>', remove_active),
    path('my/datatable/data/', OrderListJson.as_view(), name='order_list_json'),
]