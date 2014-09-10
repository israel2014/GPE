from django.db import models
from home.models import Cidade
from home.models import Estado

class Casa(models.Model):
	nick = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	cep = models.IntegerField(max_length='9', blank=False, null=False)
	rua = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	bairro = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	cidade = models.ForeignKey(Cidade)
	estado = models.ForeignKey(Estado)
	numero = models.IntegerField(max_length='6', blank=False, null=False)
	fone = models.IntegerField(max_length='12', blank=False, null=False)
