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
from restrito.views import listarAtividades, inserirAtividade, alterarAtividade, deletarAtividade
from restrito.views import listarAtividadeVinculada, inserirAtividadeVinculada, alterarAtividadeVinculada, deletarAtividadeVinculada
from restrito.views import listarEntregasAlunos, inserirEntrega, alterarEntrega, deletarEntrega, listarEntregasProfessores, listarEntregasPendentes, listarCorrigidasProfessores, listarMediaAlunos
from restrito.views import listarSolicitacaoMatricula, inserirSolicitacaoMatricula, alterarSolicitacao, deletarSolicitacao, aprovarSolicitacao

urlpatterns = [
    path('listaratividades/', listarAtividades, name='listaratividades'),

    path('inseriratividade/', inserirAtividade, name='inseriratividade'),

    path("alteraratividade/<int:idatividade>/", alterarAtividade, name="alteraratividade"),

    path('deletaratividade/<int:idatividade>/', deletarAtividade, name='deletaratividade'),

    path('listaratividadevinculada/', listarAtividadeVinculada, name='listaratividadevinculada'),

    path('inseriratividadevinculada/<int:idatividade>/', inserirAtividadeVinculada, name='inseriratividadevinculada'),

    path("alteraratividadevinculada/<int:idatividadevinculada>/", alterarAtividadeVinculada, name="alteraratividadevinculada"),

    path('deletaratividadevinculada/<int:idatividadevinculada>/', deletarAtividadeVinculada, name='deletaratividadevinculada'),
    path('listarentregasalunos/', listarEntregasAlunos, name='listarentregasalunos'),
    path('listarmediaalunos/', listarMediaAlunos, name='listarmediaalunos'),
    path('listarentregaspendentes/', listarEntregasPendentes, name='listarentregaspendentes'),
    path('listarentregasprofessores/', listarEntregasProfessores, name='listarentregasprofessores'),
    path('listarcorrigidasprofessores/', listarCorrigidasProfessores, name='listarcorrigidasprofessores'),
    path('inserirentrega/<int:idatividadevinculada>/', inserirEntrega, name='inserirentrega'),
    path("alterarentrega/<int:identrega>/", alterarEntrega, name="alterarentrega"),
    path('deletarentrega/<int:identrega>/', deletarEntrega, name='deletarentrega'),
    path('listarsolicitacao/', listarSolicitacaoMatricula, name='listarsolicitacao'),
    path('inserirsolicitacao/', inserirSolicitacaoMatricula, name='inserirsolicitacao'),
    path("alterarsolicitacao/", alterarSolicitacao, name="alterarsolicitacao"),
    path("aprovarsolicitacao/<int:idsolicitacaomatricula>/", aprovarSolicitacao, name="aprovarsolicitacao"),
    path("deletarsolicitacao/", deletarSolicitacao, name="deletarsolicitacao"),

    #path('admin/', admin.site.urls),
]
