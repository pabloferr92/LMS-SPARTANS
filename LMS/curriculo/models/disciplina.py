from django.db import models

class Disciplina(models.Model):
    iddisciplina = models.AutoField(db_column='idDisciplina', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(unique=True, max_length=30, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    statusdisc = models.CharField(db_column='statusDisc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    planodeensino = models.CharField(db_column='planoDeEnsino', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='cargaHoraria', blank=True, null=True)  # Field name made lowercase.
    competencias = models.CharField(max_length=1000, blank=True, null=True)
    habilidades = models.CharField(max_length=1000, blank=True, null=True)
    ementa = models.CharField(max_length=1000, blank=True, null=True)
    conteudoprogramatico = models.CharField(db_column='conteudoProgramatico', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='bibliografiaBasica', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='bibliografiaComplementar', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='percentualPratico', blank=True, null=True)  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='percentualTeorico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplina'

    def __str__(self):
        return self.nome
