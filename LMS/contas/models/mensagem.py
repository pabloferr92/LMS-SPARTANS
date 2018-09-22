from django.db import models
from .aluno import Aluno
from .professor import Professor

class Mensagem(models.Model):
    idmensagem = models.AutoField(db_column='idMensagem', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    assunto = models.CharField(max_length=1000, blank=True, null=True)
    referencia = models.CharField(max_length=1000, blank=True, null=True)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    origem = models.CharField(max_length=1, blank=True, null=True)
    dtenvio = models.DateField(db_column='dtEnvio', blank=True, null=True)  # Field name made lowercase.
    dtresposta = models.DateField(db_column='dtResposta')  # Field name made lowercase.
    resposta = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagem'

    def __str__(self):
        pass
