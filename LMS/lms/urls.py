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
from core.views import templateBase, cursos, detalheCurso
from core.views import detalheDisciplinaBd, detalheDisciplinaDevops, detalheDisciplinaTecweb
from core.views import index, painelAdmin
from curriculo import urls as curriculo_urls
from contas import urls as contas_urls
from restrito import urls as restrito_urls
from core import urls as core_urls


urlpatterns = [
    path('', index, name=""),
    path('base/', templateBase, name="base"),
    path('cursos/', cursos, name="cursos"),
    url(r'^detalheCurso/([a-z]+)$', detalheCurso, name="detalheCurso"),
    path('detalhe-disciplina-tecweb/', detalheDisciplinaTecweb, name="detalhe-disciplina-tecweb"),
    path('detalhe-disciplina-bd/', detalheDisciplinaBd, name="detalhe-disciplina-bd"),
    path('detalhe-disciplina-devops/', detalheDisciplinaDevops, name="detalhe-disciplina-devops"),
    path('index/', index, name="index"),
    path('painel-admin/', painelAdmin, name='painel-admin'),
    path('curriculo/', include(curriculo_urls)),
    path('contas/', include(contas_urls)),
    path('restrito/', include(restrito_urls)),
    path('core/', include(core_urls)),

]
