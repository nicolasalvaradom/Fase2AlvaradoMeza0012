from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('quienessomos', views.quienessomos, name="quienessomos"),
    path('store', views.store, name="store"),
    path('formulario', views.formulario, name="formulario"),
    path('confirmacion', views.confirmacion, name="confirmacion"),
]