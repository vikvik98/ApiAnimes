from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from user.models import Usuario


class UsuarioListSerializer(serializers.Serializer):

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nm_usuario',
            'ds_email'
        )


class UsuarioCreateSerializer(serializers.Serializer):

    class Meta:
        model = Usuario
        fields = (
            'ds_email',
            'nm_usuario',
            'ds_senha'
        )

    def validate(self, data):
        if Usuario.objects.filter(ds_email=data['ds_email']) > 0:
            raise serializers.ValidationError({"ds_email": "Esse e-mail já está cadastrado em nossa base de dados."})

    @transaction.atomic
    def create(self, validated_data):
        usuario = Usuario(ds_email=validated_data['ds_email'], nm_usuario=validated_data['nm_usuario'])
        user = User(
            email=validated_data['ds_email'],
            username=validated_data['ds_email']
        )
        user.set_password(validated_data['ds_senha'])
        user.save()
        usuario.cd_usuario_django = user
        usuario.save()
        return usuario