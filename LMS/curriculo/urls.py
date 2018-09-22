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
from curriculo.views import listarCursos, inserirCurso, alterarCurso, deletarCurso
from curriculo.views import listarDisciplinas, inserirDisciplina, alterarDisciplina, deletarDisciplina
from curriculo.views import listarDisciplinasOfertadas,inserirDisciplinaOfertada,alterarDisciplinaOfertada,deletarDisciplinaOfertada


urlpatterns = [
    path('listarcursos/', listarCursos, name ='listarcursos'),

    path('inserircurso/', inserirCurso, name = 'inserircurso'),

    path('deletarcurso/<int:idcurso>/', deletarCurso, name = 'deletarcurso'),

    path("alterarcurso/<int:idcurso>/", alterarCurso, name = "alterarcurso"),

    path('listardisciplinas/', listarDisciplinas, name ='listardisciplinas'),

    path('inserirdisciplina/', inserirDisciplina, name = 'inserirdisciplina'),

    path('deletardisciplina/<int:iddisciplina>/', deletarDisciplina, name = 'deletardisciplina'),

    path("alterardisciplina/<int:iddisciplina>/", alterarDisciplina, name = "alterardisciplina"),

    path('listardisciplinasofertadas/',listarDisciplinasOfertadas, name ='listardisciplinasofertadas'),

    path('inserirdisciplinaofertada/<int:iddisciplina>/', inserirDisciplinaOfertada, name = 'inserirdisciplinaofertada'), ## SOMENTE VIA OFERTADA DA TELA DISCIPLINAS

    path('deletardisciplinaofertada/<int:iddisciplinaofertada>/', deletarDisciplinaOfertada, name = 'deletardisciplinaofertada'),

    path("alterardisciplinaofertada/<int:iddisciplinaofertada>/", alterarDisciplinaOfertada, name = "alterardisciplinaofertada"),
]
