from .pessoa import pessoa
from django.utils import timezone


class Professor(pessoa):
    idprofessor = pessoa.AutoField(db_column='idProfessor', primary_key=True)  # Field name made lowercase.
    logon = pessoa.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = pessoa.CharField(max_length=20)
    nome = pessoa.CharField(max_length=30)
    email = pessoa.CharField(unique=True, max_length=40)
    celular = pessoa.CharField(unique=True, max_length=9, blank=True, null=True)
    dtexpiracao = pessoa.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    apelido = pessoa.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'
