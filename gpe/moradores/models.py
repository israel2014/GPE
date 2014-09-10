from django.db import models
from usuario.models import Usuario
from casa.models import Casa

class Moradores(models.Model):
	casa = models.ForeignKey(Casa)
	usuario = models.ForeignKey(Usuario)