from django.db import models

class Usuario(models.Model):
	nome = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	sobrenome = models.CharField(max_length='100', blank=False, null=False)
	cpf = models.IntegerField(max_length='12', blank=False, null=False)
	email = models.CharField(max_length='100', blank=False, null=False)
	status = models.IntegerField(max_length='1', blank=False, null=False)
	diaN = models.IntegerField(max_length='2', blank=False, null=False)
	mesN = models.IntegerField(max_length='2', blank=False, null=False)
	anoN = models.IntegerField(max_length='4', blank=False, null=False)
	sexo = models.CharField(max_length='100', blank=False, null=False)

