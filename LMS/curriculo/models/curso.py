from django.db import models
from contas.models.coordenador import Coordenador

class Curso(models.Model):
    idcurso = models.AutoField(db_column='idCurso', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(unique=True, max_length=30)
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return self.nome
