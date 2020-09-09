from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    cd_usuario_django = models.OneToOneField(User, related_name="usuario", on_delete=models.PROTECT, unique=True)
    nm_usuario = models.CharField("Nome completo", max_length=190)
    ds_email = models.CharField("Email", max_length=200)
