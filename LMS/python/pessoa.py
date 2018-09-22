from django.db import models


class Pessoa(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)


    class Meta()
        abstract = True

    def retornaSobrenome(self):
        return self.__nome.split(" ")[-1]

    def retornaCargaHoraria(self):
        cargaTotal = 0
        for disciplina in self.__disciplinas:
            cargaTotal += disciplina.getCargaHoraria()
        return cargaTotal / 4