from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
## herdando classes e sobescrevendo forms do django
class Users(AbstractUser):
    choices_cargo = (('R', 'Recpecao'),
                     ('A', 'Administrativo'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)