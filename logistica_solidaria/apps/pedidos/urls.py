from django.urls import path
from . import views
 
app_name = 'pedidos'
 
urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
    path('novo/<int:doacao_pk>/', views.novo, name='novo'),
    path('<int:pk>/status/', views.atualizar_status, name='atualizar_status'),
    # Rotas do voluntário
    path('<int:pk>/aceitar/', views.aceitar_entrega, name='aceitar_entrega'),
    path('<int:pk>/concluir/', views.concluir_entrega, name='concluir_entrega'),
]
 
