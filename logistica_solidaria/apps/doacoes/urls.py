from django.urls import path
from . import views

app_name = 'doacoes'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('nova/', views.nova, name='nova'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
    path('<int:pk>/editar/', views.editar, name='editar'),
    path('<int:pk>/cancelar/', views.cancelar, name='cancelar'),
]
