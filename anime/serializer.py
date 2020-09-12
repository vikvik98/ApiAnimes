from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from anime.models import Anime
from user.serializer import UsuarioListSerializer


class AnimeListSerializer(serializers.ModelSerializer):
    cd_usuario = UsuarioListSerializer()

    class Meta:
        model = Anime
        fields = (
            'id',
            'nm_anime',
            'ds_anime',
            'ie_assistido',
            'ie_favorito',
            'cd_usuario'
        )


class AnimeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = (
            'nm_anime',
            'ds_anime',
            'ie_assistido',
            'ie_favorito',
            'cd_usuario'
        )

class AnimeUpdadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = (
            'nm_anime',
            'ds_anime',
            'ie_assistido',
            'ie_favorito',
        )