"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from contas.views import listarProfessores, inserirProfessor, deletarProfessor, alterarProfessor
from contas.views import listarAlunos, inserirAluno, alterarAluno, deletarAluno
from contas.views import listarCoordenadores, inserirCoordenador, alterarCoordenador, deletarCoordenador
from contas.views import listarMensagensEntrada, inserirMensagem,listarMensagensSaida, alterarMensagem, deletarMensagem

urlpatterns = [
    path('listarprofessores/', listarProfessores, name ='listarprofessores'),

    path('inserirprofessor/', inserirProfessor, name = 'inserirprofessor'),

    path('deletarprofessor/<int:idprofessor>/', deletarProfessor, name = 'deletarprofessor'),

    path("alterarprofessor/<int:idprofessor>/", alterarProfessor, name = "alterarprofessor"),

    path('listaralunos/', listarAlunos, name='listaralunos'),

    path('inseriraluno/', inserirAluno, name='inseriraluno'),

    path('deletaraluno/<int:idaluno>/', deletarAluno, name='deletaraluno'),

    path("alteraraluno/<int:idaluno>/", alterarAluno, name="alteraraluno"),

    path('listarcoordenadores/', listarCoordenadores, name='listarcoordenadores'),

    path('inserircoordenador/', inserirCoordenador, name='inserircoordenador'),

    path('deletarcoordenador/<int:idcoordenador>/', deletarCoordenador, name='deletarcoordenador'),

    path("alterarcoordenador/<int:idcoordenador>/", alterarCoordenador, name="alterarcoordenador"),

    path("listarmensagensentrada/", listarMensagensEntrada, name="listarmensagensentrada"),

    path("listarmensagenssaida/", listarMensagensSaida, name="listarmensagenssaida"),

    path("inserirmensagem/", inserirMensagem, name="inserirmensagem"),

    path("deletarmensagem/<int:idmensagem>/", deletarMensagem, name="deletarmensagem"),

    path("alterarmensagem/<int:idmensagem>/", alterarMensagem, name="alterarmensagem"),


]
