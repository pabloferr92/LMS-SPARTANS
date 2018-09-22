# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    ra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'


class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=1000)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=1000, blank=True, null=True)
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'


class Atividadevinculada(models.Model):
    idatividadevinculada = models.AutoField(db_column='idAtividadeVinculada', primary_key=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='idAtividade')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='idDisciplinaOfertada')  # Field name made lowercase.
    rotulo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, blank=True, null=True)
    dtiniciorespostas = models.DateField(db_column='dtInicioRespostas', blank=True, null=True)  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='dtFimRespostas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadeVinculada'
        unique_together = (('idatividade', 'iddisciplinaofertada'),)


class Coordenador(models.Model):
    idcoordenador = models.AutoField(db_column='idCoordenador', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador'


class Curso(models.Model):
    idcurso = models.AutoField(db_column='idCurso', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'curso'


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
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplina'


class Disciplinaofertada(models.Model):
    iddisciplinaofertada = models.AutoField(db_column='idDisciplinaOfertada', primary_key=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='dtInicioMatricula', blank=True, null=True)  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='dtFimMatricula', blank=True, null=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='idCurso')  # Field name made lowercase.
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=6, blank=True, null=True)
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor', blank=True, null=True)  # Field name made lowercase.
    metodologia = models.CharField(max_length=1000, blank=True, null=True)
    recursos = models.CharField(max_length=1000, blank=True, null=True)
    criterioavaliacao = models.CharField(db_column='criterioAvaliacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='planoDeAulas', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplinaOfertada'


class Entrega(models.Model):
    identrega = models.AutoField(db_column='idEntrega', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    titulo = models.CharField(max_length=40, blank=True, null=True)
    resposta = models.CharField(max_length=1000, blank=True, null=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='idAtividadeVinculada')  # Field name made lowercase.
    dtentrega = models.DateField(db_column='dtEntrega')  # Field name made lowercase.
    status = models.CharField(max_length=20, blank=True, null=True)
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtavaliacao = models.DateField(db_column='dtAvaliacao')  # Field name made lowercase.
    obs = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega'


class Mensagem(models.Model):
    idmensagem = models.AutoField(db_column='idMensagem', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    assunto = models.CharField(max_length=1000, blank=True, null=True)
    referencia = models.CharField(max_length=1000, blank=True, null=True)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    dtenvio = models.DateField(db_column='dtEnvio', blank=True, null=True)  # Field name made lowercase.
    dtresposta = models.DateField(db_column='dtResposta')  # Field name made lowercase.
    resposta = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagem'


class Professor(models.Model):
    idprofessor = models.AutoField(db_column='idProfessor', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    apelido = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class Solicitacaomatricula(models.Model):
    idsolicitacaomatricula = models.AutoField(db_column='idSolicitacaoMatricula', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada')  # Field name made lowercase.
    dtsolicitacao = models.DateField(db_column='dtSolicitacao')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitacaoMatricula'
