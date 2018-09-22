from django.db import models
from .disciplina import Disciplina
from .curso import Curso
from contas.models.professor import Professor


class Disciplinaofertada(models.Model):
    iddisciplinaofertada = models.AutoField(db_column='idDisciplinaOfertada', primary_key=True)  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='dtInicioMatricula', blank=True, null=True)  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='dtFimMatricula', blank=True, null=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='idCurso')  # Field name made lowercase.
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=6, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor', blank=True, null=True)  # Field name made lowercase.
    metodologia = models.CharField(max_length=1000, blank=True, null=True)
    recursos = models.CharField(max_length=1000, blank=True, null=True)
    criterioavaliacao = models.CharField(db_column='criterioAvaliacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='planoDeAulas', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplinaOfertada'

    def __str__(self):
        return self.iddisciplina
