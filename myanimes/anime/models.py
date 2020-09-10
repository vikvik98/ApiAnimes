from django.db import models

# Create your models here.
class Anime(models.Model):
    nm_anime = models.CharField("Nome do anime", max_length=400, null=False)
    ie_assistido = models.BooleanField(default=False)
    ie_favorito = models.BooleanField(default=False)
    cd_usuario = models.ForeignKey(related_name="animes", on_delete=models.CASCADE)