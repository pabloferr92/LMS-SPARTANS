from .pessoa import pessoa
from django.utils import timezone


class Aluno(pessoa):
    foto = pessoa.CharField(max_length=255, blank=True, null=True)
    ra = pessoa.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'
