from django.urls import path
from . import views

app_name = 'avaliacoes'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('novo/<int:pedido_pk>/', views.nova, name='nova'),
]
