from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.usuarios.urls')),
    path('doacoes/', include('apps.doacoes.urls')),
    path('pedidos/', include('apps.pedidos.urls')),
    path('rastreamento/', include('apps.rastreamento.urls')),
    path('avaliacoes/', include('apps.avaliacoes.urls')),
    path('notificacoes/', include('apps.notificacoes.urls')),
    path('relatorios/', include('apps.relatorios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
