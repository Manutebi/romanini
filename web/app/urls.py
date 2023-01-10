from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('checklist/', checklist, name="checklist"),
    path('otmecanicos/', otmecanicos, name="otmecanicos"),
    path('alertas/', alertas, name="alertas"),
    path('solicitud/', solicitud, name="solicitud"),
    path('crear_check/', crear_check, name="crear_check"),
    path('listar_check/', listar_check, name="listar_check"),
    path('crear_alerta/', crear_alerta, name="crear_alerta"),
    path('listar_alerta/', listar_alerta, name="listar_alerta"),
    path('crear_solicitud/', crear_solicitud, name="crear_solicitud"),
    path('listar_solicitud/', listar_solicitud, name="listar_solicitud"),
    path('crear_ot/', crear_ot, name="crear_ot"),
    path('listar_ot/', listar_ot, name="listar_ot"),
    path('login/', login, name="login")
]