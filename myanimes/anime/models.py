from django.db import models


# Create your models here.
from user.models import Usuario


class Anime(models.Model):
    nm_anime = models.CharField("Nome do anime", max_length=400, null=False)
    ds_anime = models.CharField("Descrição do anime", max_length=600, null=True)
    ie_assistido = models.BooleanField(default=False)
    ie_favorito = models.BooleanField(default=False)
    cd_usuario = models.ForeignKey(Usuario, related_name="animes", on_delete=models.CASCADE, null=False)
