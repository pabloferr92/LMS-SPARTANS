from django.urls import path, include
from django.conf.urls import url, include
from .views import login, logout, visaoAluno, visaoProfessor, visaoCoordenador, visaoAdministrador
urlpatterns = [
     path('login/', login, name="login"),
     path('logout/', logout, name="logout"),
     path('aluno/', visaoAluno, name="aluno"),
     path('professor/', visaoProfessor, name="professor"),
     path('coordenador/', visaoCoordenador, name="coordenador"),
     path('administrador/', visaoAdministrador, name="administrador"),
     ]
