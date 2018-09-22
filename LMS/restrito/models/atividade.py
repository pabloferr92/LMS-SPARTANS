from django.db import models
from contas.models.professor import Professor



class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=1000)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=1000, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'

    def __str__(self):
        return self.titulo