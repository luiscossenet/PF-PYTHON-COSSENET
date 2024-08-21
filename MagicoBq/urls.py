"""
URL configuration for MagicoBq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from AppMagico.views.general_views import custom_404_view, custom_403_view, custom_500_view, custom_400_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("AppMagico.urls")),
    path(
        "users/", include("users.urls")
    ),  # Se diferencia de la ruta de la app principal
    path("blog/", include("blog.urls")),
]

handler404 = 'AppMagico.views.custom_404_view'  # Asegúrate de usar la ruta correcta a tu vista
handler403 = 'AppMagico.views.custom_403_view'
handler500 = 'AppMagico.views.custom_500_view'
handler400 = 'AppMagico.views.custom_400_view'
    
# Añadir rutas para archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
