from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.response import Response

from user.models import *
from user.serializer import *


class UsuarioView(viewsets.ViewSet):


    def get_object(self, request):
        try:
            return Usuario.objects.get(ds_email=request.GET.get("ds_email"))
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):

        if "ds_email" not in request.GET:
            return Response({"detail": "O campo ds_email é obrigatorio"}, status=status.HTTP_404_NOT_FOUND)

        if "ds_senha" not in request.GET:
            return Response({"detail": "O campo ds_senha é obrigatorio"}, status=status.HTTP_404_NOT_FOUND)

        instance = self.get_object(request)

        if instance.cd_usuario_django.check_password(request.GET.get("ds_senha")) is False:
            return Response({"detail": "Email e/ou senha invalido"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioListSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = UsuarioCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

