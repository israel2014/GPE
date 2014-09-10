from django.db import models
from moradores.models import Moradores

class Telefones(models.Model):
	moradores = models.ForeignKey(Moradores)
	codArea = models.IntegerField(max_length='3', blank=False, null=False)
	Telefone = models.IntegerField(max_length='11', blank=False, null=False)

