from django.db import models
from contas.models.aluno import Aluno
from contas.models.professor import Professor
from restrito.models.atividadeVinculada import Atividadevinculada
from datetime import date, datetime, timedelta
import time

class Entrega(models.Model):
    identrega = models.AutoField(db_column='idEntrega', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    titulo = models.CharField(max_length=40, blank=True, null=True)
    resposta = models.CharField(max_length=1000, blank=True, null=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='idAtividadeVinculada')  # Field name made lowercase.
    dtentrega = models.DateField(db_column='dtEntrega')  # Field name made lowercase.
    status = models.CharField(max_length=20, blank=True, null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtavaliacao = models.DateField(db_column='dtAvaliacao')  # Field name made lowercase.
    obs = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega'

    def __str__(self):
        return self.titulo

    #métodos para o aluno ver as atividades enviadas, não enviadas e pendentes de envio

    def retornaAtividadesEnviadasAluno(disciplinaOfertada, idAluno):
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada, idaluno = idAluno)
        atividadesEntregues = []
        if(len(entregas) == 0):
            return atividadesEntregues
        for entrega in entregas:
            atividadesEntregues.append(entrega.idAtividadevinculada)

        return atividadesEntregues

    def retornaAtividadesNaoEnviadasAluno(self, idAluno):
        from restrito.models.atividadeVinculada import Atividadevinculada
        from restrito.models.solicitacaoMatricula import Solicitacaomatricula
        matriculas = Solicitacaomatricula.objects.filter(status="APROVADA", idaluno=idAluno)
        atividadesNaoEntregues = []

        for m in matriculas:
            print(m.iddisciplinaofertada.iddisciplinaofertada)
            limit = datetime.now() + timedelta(days=-3)
            atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = m.iddisciplinaofertada.iddisciplinaofertada, dtiniciorespostas__lte=time.strftime("%Y-%m-%d"), dtfimrespostas__gte=limit.strftime('%Y-%m-%d'))
            entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = m.iddisciplinaofertada.iddisciplinaofertada, idaluno = idAluno)
            if(len(entregas) == 0):
                return atividades
            for atividade in atividades:
                if(not bool(len(entregas.filter(idatividadevinculada=atividade.idatividadevinculada)))):
                    atividadesNaoEntregues.append(atividade)

        return atividadesNaoEntregues

    def retornaAtividadesPendentesAluno(disciplinaOfertada, idAluno):
        from restrito.models.atividadeVinculada import Atividadevinculada
        atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = disciplinaOfertada, dtiniciorespostas__lte=date.today(), dtfimrespostas__gte=date.today())
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada, idaluno = idAluno)
        if(len(entregas) == 0):
            return atividades
        atividadesNaoEntregues = []
        for atividade in atividades:
            if(not bool(len(entregas.filter(idatividadevinculada=atividade.idatividadevinculada)))):
                atividadesNaoEntregues.append(atividade)

        return atividadesNaoEntregues

    #métodos para o professor ver as atividades enviadas pelos alunos

    def retornaAtividadesEnviadasProfessor(disciplinaOfertada):
        from restrito.models.atividadeVinculada import Atividadevinculada
        atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = disciplinaOfertada)
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada)
        atividadesEntregues = []
        if(len(entregas) == 0):
            return atividadesEntregues
        for atividade in atividades:
            atividadesEntregues.append(
                {
                    "atividade": atividade,
                    "entregas": entregas.filter(idatividadevinculada=atividade.idatividadevinculada)
                }
            )

        return atividadesEntregues

    def descontaNota(nota, porcentagem):
        desconto = nota - (nota * porcentagem/100)
        return desconto
