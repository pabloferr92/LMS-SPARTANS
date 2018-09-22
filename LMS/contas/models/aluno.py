from .pessoa import Pessoa
from django.db import models
import time

class Aluno(Pessoa):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    foto = models.CharField(max_length=11, blank=True, null=True)
    ra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'
    
    
    def __str__(self):

        return self.nome
     
    def retornaCargaHoraria(self,idaluno):
        from restrito.models.solicitacaoMatricula import Solicitacaomatricula
        aluno = Aluno.objects.get(idaluno=self.idaluno)
        solicitacoes = Solicitacaomatricula.objects.filter(idaluno=self.idaluno)
        cargaHoraria = 0
        for i in solicitacoes:
            cargaHoraria+= i.iddisciplinaofertada.iddisciplina.cargahoraria
        return cargaHoraria
            

    def geraNumeroRA(ultimoRA):
        ano = time.strftime("%y")
        if(str(ultimoRA)[:2] == ano):
            return ultimoRA+1
        return int(''.join([str(ano), '00001']))        
