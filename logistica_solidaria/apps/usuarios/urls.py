from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('minha-pagina/', views.pagina_ong_view, name='pagina_ong'),
    path('ongs/', views.paginas_ongs, name='ongs'),
    path('ongs/<int:pk>/', views.pagina_publica_ong, name='pagina_publica_ong'),
]
