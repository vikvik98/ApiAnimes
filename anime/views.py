from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.response import Response

from anime.models import Anime
from anime.serializer import AnimeListSerializer, AnimeCreateSerializer, AnimeUpdadeSerializer


class AnimeView(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Anime.objects.get(pk=pk)
        except:
            raise Http404

    def list(self, request, cd_usuario, *args, **kwargs):
        instances = Anime.objects.filter(cd_usuario=cd_usuario)

        if "ie_assistido" in request.GET:
            instances = Anime.objects.filter(cd_usuario=cd_usuario, ie_assistido=True)

        if "ie_favorito" in request.GET:
            instances = Anime.objects.filter(cd_usuario=cd_usuario, ie_favorito=True)

        serializer = AnimeListSerializer(instances, many=True)
        return Response(serializer.data)

    def retrive(self, request, cd_anime, *args, **kwargs):
        instance = self.get_object(cd_anime)
        serializer = AnimeListSerializer(instance)
        return Response(serializer.data)

    def create(self, request, cd_usuario, *args, **kwargs):
        request.data["cd_usuario"] = cd_usuario
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, cd_anime, *args, **kwargs):
        instance = self.get_object(cd_anime)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_updade(self, request, cd_anime, *args, **kwargs):
        instance = self.get_object(cd_anime)
        serializer = AnimeUpdadeSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
