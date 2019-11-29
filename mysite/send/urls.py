from django.urls import path,include
from . import views

urlpatterns = [
    path('ss', views.index, name='hola'),
    path('', views.ClientCreate, name='client_new'),
]