"""myanimes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from anime.views import AnimeView
from user.views import UsuarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', UsuarioView.as_view({'get': 'get', 'post': 'create'}), name='usuarios/'),
    path('animes/<int:cd_usuario>/', AnimeView.as_view({'get': 'list', 'post': 'create'}), name='animes/cd_usuario/'),
    path('animes/anime/<int:cd_anime>/', AnimeView.as_view({'get': 'retrive', 'delete': 'destroy', 'patch': 'partial_updade'}), name='animes/anime/cd_anime/'),
]
