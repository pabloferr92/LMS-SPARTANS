
from django.db import models
from contas.models.coordenador import Coordenador
from contas.models.aluno import Aluno
from curriculo.models.disciplinaOfertada import Disciplinaofertada


class Solicitacaomatricula(models.Model):
    idsolicitacaomatricula = models.AutoField(db_column='idSolicitacaoMatricula', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada')  # Field name made lowercase.
    dtsolicitacao = models.DateField(db_column='dtSolicitacao')  # Field name made lowercase.
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitacaoMatricula'

    def __str__(self):
        return self.idsolicitacaomatricula
