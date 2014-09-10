from django.db import models
from usuario.models import Usuario

class Login(models.Model):
	senha = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	nick = models.CharField(db_index=True, max_length='100', blank=False, null=False)
	usuario = models.ForeignKey(Usuario)
