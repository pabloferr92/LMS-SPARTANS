from django.db import models
from django.utils import timezone


class pessoa(models.Model):
    logon = models.CharField(unique=True, max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=40)
    celular = models.IntegerField(unique=True, null=True)
    dtExpiracao = models.DateField(default=timezone.now) 

    def retorna_sobrenome(self):
        return self.nome.split(' ')[-1]

    def retornaCargaHoraria(self):
        return 'Metodo nao implementado'
    
    class Meta:
        abstract = True
