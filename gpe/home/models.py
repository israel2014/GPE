from django.db import models

class Dia(models.Model):
	dia = models.IntegerField(max_length='2', blank=False, null=False)

class Mes(models.Model):
	mes = models.IntegerField(max_length='2', blank=False, null=False)
	mesR = models.CharField(db_index=True, max_length='100', blank=False, null=False)

class Ano(models.Model):
	ano = models.IntegerField(max_length='4', blank=False, null=False)

class Cidade(models.Model):
	cidade = models.CharField(db_index=True, max_length='100', blank=False, null=False)

class Estado(models.Model):
	Estado = models.CharField(db_index=True, max_length='2', blank=False, null=False)
		

