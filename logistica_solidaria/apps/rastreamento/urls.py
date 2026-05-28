from django.urls import path
from . import views

app_name = 'rastreamento'

urlpatterns = [
    path('', views.consulta, name='consulta'),
    path('<str:codigo>/', views.detalhe, name='detalhe'),
]
