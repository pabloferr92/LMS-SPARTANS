from django.db import models


class Pessoa(models.Model):
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=11, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        abstract = True

    def retornaCargaHoraria(self):
        return "Metodo nao implementado"


