from django.db import models
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from contas.models.professor import Professor
from contas.models.administrador import Administrador
import uuid

class Sessao(models.Model):

        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')
        idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')
        idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')
        idadministrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='idAdministrador')

        class Meta:
            managed = False
            db_table = 'sessao'

        def __str__(self):
            return self.id
