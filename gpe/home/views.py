# This Python file uses the following encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from home.models import Dia
from home.models import Mes
from home.models import Ano


def index(request):
	dias = Dia.objects.all()
	meses = Mes.objects.all()
	anos = Ano.objects.all()
	return render(request, 'index.html', {'dias':dias, 'meses':meses, 'anos':anos})
