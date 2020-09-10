from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response

from anime.models import Anime
from anime.serializer import AnimeListSerializer, AnimeCreateSerializer


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

    def detail(self, request, cd_anime, *args, **kwargs):
        instance = self.get_object(cd_anime)
        serializer = AnimeListSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

