from django.shortcuts import render, redirect
from .models.atividade import Atividade
from curriculo.models.disciplina import Disciplina
from curriculo.models.disciplinaOfertada import Disciplinaofertada
from .models.atividadeVinculada import Atividadevinculada
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from restrito.models.solicitacaoMatricula import Solicitacaomatricula
from .models.entrega import Entrega
import time

def listarAtividades(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaAtividades.html', {"atividades": Atividade.objects.all()})

def inserirAtividade(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.sessao.usuario.id)

        Atividade.objects.create (
            titulo=request.POST.get("titulo"),
            descricao = request.POST.get("descricao"),
            conteudo = request.POST.get("conteudo"),
            tipo = request.POST.get("tipo"),
            extra = request.POST.get("extra"),
            idprofessor = professor
        )
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividade.html")

def alterarAtividade(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        atividade = Atividade.objects.get(idatividade=idatividade)
        atividade.titulo=request.POST.get("titulo")
        atividade.descricao = request.POST.get("descricao")
        atividade.conteudo = request.POST.get("conteudo")
        atividade.tipo = request.POST.get("tipo")
        atividade.extra = request.POST.get("extra")
        atividade.save()
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividade.html", {'atividade': Atividade.objects.get(idatividade=idatividade)})

def deletarAtividade(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividade = Atividade.objects.get(idatividade=idatividade)
    atividade.delete()
    return redirect ('listaratividades')

def listarAtividadeVinculada(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaAtividadesVinculadas.html', {"atividades": Atividadevinculada.objects.all()})

def inserirAtividadeVinculada(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    contexto = {
        'atividade': Atividade.objects.get(idatividade=idatividade),
        'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y"))),
    }

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.sessao.usuario.id)
        atividade = Atividade.objects.get(idatividade=idatividade)
        disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplinaofertada"))
        Atividadevinculada.objects.create(
            idprofessor=professor,
            idatividade=atividade,
            iddisciplinaofertada=disciplinaofertada,
            rotulo=request.POST.get("rotulo"),
            estado=request.POST.get("estado"),
            dtiniciorespostas=request.POST.get("dtiniciorespostas"),
            dtfimrespostas=request.POST.get("dtfimrespostas")
        )
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividadeVinculada.html", contexto)

def alterarAtividadeVinculada(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        atividadevindulada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplinaofertada"))
        atividadevindulada.iddisciplinaofertada = disciplinaofertada
        atividadevindulada.rotulo = request.POST.get("rotulo")
        atividadevindulada.estado = request.POST.get("estado")
        atividadevindulada.dtiniciorespostas = request.POST.get("dtiniciorespostas")
        atividadevindulada.dtfimrespostas = request.POST.get("dtfimrespostas")
        atividadevindulada.save()
        return redirect('listaratividadevinculada')
    else:
        atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        contexto ={
            'atividade': atividadevinculada.idatividade,
            'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y"))),
            'atividadevinculada': atividadevinculada
        }
        return render(request, "formNovaAtividadeVinculada.html", contexto)

def deletarAtividadeVinculada(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')

def listarEntregasAlunos(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno



    return render(request, 'listaEntregasAlunos.html', {"entregas": Entrega.objects.filter(idaluno=request.sessao.usuario.id, status="ENTREGUE")})

def listarEntregasPendentes(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasPendentes.html', {"avs": Entrega().retornaAtividadesNaoEnviadasAluno(request.sessao.usuario.id)})

def listarEntregasProfessores(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasProfessores.html', {"entregas": Entrega.objects.filter(idatividadevinculada__idprofessor=request.sessao.usuario.id, status="ENTREGUE")})

def listarMediaAlunos(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    minhasMaterias = Disciplinaofertada.objects.filter(idprofessor=request.sessao.usuario.id, ano=time.strftime("%Y"))
    listaMaterias = [];
    for mm in minhasMaterias:
        print("procurando entrega da disciplina", mm.iddisciplinaofertada)
        atividadesviculadas = Atividadevinculada.objects.filter(iddisciplinaofertada=mm.iddisciplinaofertada)
        for av in atividadesviculadas:
            idAlunoAux = 0
            arrAlunos = []
            dicAluno = {}
            print("encontrei uma av pra disciplina", av.idatividadevinculada)
            entregas = Entrega.objects.filter(idatividadevinculada=av.idatividadevinculada, status="CORRIGIDO").order_by('idaluno')
            
            for e in entregas:
                print("encontrei um entrega do aluno", e.idaluno.nome, " para a entrega ", av.rotulo)
                if idAlunoAux != e.idaluno.idaluno:
                    if idAlunoAux != 0:
                        arrAlunos.append(dicAluno)
                    idAlunoAux = e.idaluno.idaluno
                    dicAluno = {}
                    dicAluno['notas'] = []

                dicAluno["id"] = e.idaluno.idaluno
                dicAluno["nome"] = e.idaluno.nome
                dicAluno['notas'].append(float(e.nota))
            
            if idAlunoAux != 0:
                arrAlunos.append(dicAluno)

            print("arrAlunos:", arrAlunos)
            for aluno in arrAlunos:
                if len(aluno['notas']) > 1:
                    aluno['notas'].remove(max(aluno['notas']))
                if len(aluno['notas']) > 1:
                    aluno['notas'].remove(max(aluno['notas']))
                if len(aluno['notas']) > 1:
                    aluno['notas'].remove(max(aluno['notas']))
                soma = 0
                for nota in aluno['notas']:
                    soma += nota
                aluno['media'] = soma / len(aluno['notas'])

            alunosMatriculados = Solicitacaomatricula.objects.filter(iddisciplinaofertada=mm.iddisciplinaofertada, status="APROVADA")
            for am in alunosMatriculados:
                alunoPresente = False
                for aluno in arrAlunos:
                    if am.idaluno.idaluno == aluno['id']:
                        alunoPresente = True
                if not alunoPresente:
                    dicAluno = {
                        "id": am.idaluno.idaluno,
                        "nome": am.idaluno.nome,
                        "notas": [],
                        "media": 0
                    }
                    arrAlunos.append(dicAluno)
        dicDisciplina = {
            "nome": mm.iddisciplina.nome,
            "alunos": arrAlunos
        }

        listaMaterias.append(dicDisciplina)
    print("listaMaterias:", listaMaterias)
    return render(request, 'listaMediasAluno.html', {"materias": listaMaterias})

def listarCorrigidasProfessores(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasProfessores.html', {"entregas": Entrega.objects.filter(idatividadevinculada__idprofessor=request.sessao.usuario.id, status="CORRIGIDO")})

def inserirEntrega(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        idatividade = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id)
        Entrega.objects.create(
            idaluno=idaluno,
            titulo=request.POST.get("titulo"),
            resposta=request.POST.get("resposta"),
            idatividadevinculada=idatividade,
            dtentrega=time.strftime("%Y-%m-%d"),
            obs="",
            nota=0,
            status="ENTREGUE"
        )
        return redirect('listarentregaspendentes')
    else:
        return render(request, "formNovaEntrega.html")

def alterarEntrega(request, identrega):
    try:
        if request.sessao.usuario.profile != "A" and request.sessao.usuario.profile != 'P':
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        entrega = Entrega.objects.get(identrega=identrega)
        entrega.titulo=request.POST.get("titulo")
        entrega.resposta=request.POST.get("resposta")
        entrega.dtentrega=time.strftime("%Y-%m-%d")
        dtentrega = time.strftime(str(entrega.dtentrega))
        dtlimite = time.strftime(str(entrega.idatividadevinculada.dtfimrespostas))
        nota = float(request.POST.get("nota"))
        if dtentrega > dtlimite:
            nota = nota * 0.7
        if request.sessao.usuario.profile == 'P':
            entrega.nota = nota
            entrega.obs = request.POST.get("obs")
            entrega.dtavaliacao=time.strftime("%Y-%m-%d")
            entrega.status="CORRIGIDO"
            entrega.save()
            return redirect('listarentregasprofessores')
        entrega.save()
        return redirect('listarentregasalunos')

    else:
        entrega = Entrega.objects.get(identrega=identrega)
        return render(request, "formNovaEntrega.html", {'entrega': entrega})

def deletarEntrega(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')

def listarSolicitacaoMatricula(request):
    try:
        if request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    return render(request, 'listaSolicitacaoMatricula.html', {"solicitacoes": Solicitacaomatricula.objects.filter(status="SOLICITADA")})

def inserirSolicitacaoMatricula(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        for matricula in request.POST.getlist("matricula"):
            Solicitacaomatricula.objects.create (
                idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id),
                iddisciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=matricula),
                dtsolicitacao=time.strftime("%Y-%m-%d"),
                status = "SOLICITADA",
            )
        return redirect('aluno')
    else:
        try:
            solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
            return redirect('alterarsolicitacao')
        except:
            return render(request, 'formNovaSolicitacaoMatricula.html', {'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y")))})

def alterarSolicitacao(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
        arrantigo = []
        for sm in solicitacaomatricula:
            arrantigo.append(sm.iddisciplinaofertada.iddisciplinaofertada)

        arrnovo = []
        for matricula in request.POST.getlist("matricula"):
            arrnovo.append(matricula)

        if not (arrantigo==arrnovo):
            for sm in solicitacaomatricula:
                sm.delete()

            for matricula in request.POST.getlist("matricula"):
                Solicitacaomatricula.objects.create (
                    idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id),
                    iddisciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=matricula),
                    dtsolicitacao=time.strftime("%Y-%m-%d"),
                    status = "SOLICITADA",
                )

        return redirect('alterarsolicitacao')
    else:
        solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
        disciplinasofertadas = Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y")));
        for disciplinaofertada in disciplinasofertadas:
            if any(sm.iddisciplinaofertada.iddisciplinaofertada == disciplinaofertada.iddisciplinaofertada for sm in solicitacaomatricula):
                disciplinaofertada.selected = True
            else:
                disciplinaofertada.selected = False

        return render(request, "formNovaSolicitacaoMatricula.html", {'disciplinasofertadas': disciplinasofertadas})

def deletarSolicitacao(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
    solicitacaomatricula.delete()
    return redirect ('inserirsolicitacao')

def aprovarSolicitacao(request, idsolicitacaomatricula):
    try:
        if request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    if request.method == 'POST':
        solicitacao = Solicitacaomatricula.objects.get(idsolicitacaomatricula=idsolicitacaomatricula)
        solicitacao.status=request.POST.get("status")
        solicitacao.save()
        return redirect('listarsolicitacao')
    else:
        return render(request, 'formAprovarSolicitacao.html', {"solicitacao": Solicitacaomatricula.objects.get(idsolicitacaomatricula=idsolicitacaomatricula)})
