from django.shortcuts import render, redirect
from .models.curso import Curso
from .models.disciplina import Disciplina
from .models.disciplinaOfertada import Disciplinaofertada
from contas.models.coordenador import Coordenador
from contas.models.professor import Professor
from restrito.models.atividade import Atividade

def listarCursos(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    return render(request, 'listaCursos.html', {'cursos':  Curso.objects.all()})

def inserirCurso(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        Curso.objects.create(
            nome=request.POST.get("curso"),
            idcoordenador=Coordenador.objects.get(idcoordenador=request.POST.get("coordenador"))
        )
        return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", {"coordenadores": Coordenador.objects.all()})

def alterarCurso(request, idcurso):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        curso = Curso.objects.get(idcurso=idcurso)
        curso.nome = request.POST.get('curso')
        curso.idcoordenador = Coordenador.objects.get(idcoordenador=request.POST.get("coordenador"))
        curso.save()
        return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", {'curso': Curso.objects.get(idcurso=idcurso), "coordenadores": Coordenador.objects.all()})

def deletarCurso(request, idcurso):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    curso = Curso.objects.get(idcurso=idcurso)
    curso.delete()
    return redirect('listarcursos')

def listarDisciplinas(request):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    return render(request, 'listaDisciplinas.html', {"disciplinas": Disciplina.objects.all()})

def inserirDisciplina(request):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        Disciplina.objects.create(
            nome=request.POST.get("nome"),
            data=request.POST.get("data"),
            statusdisc=request.POST.get("statusdisc"),
            planodeensino=request.POST.get("plano"),
            cargahoraria=request.POST.get("cargahoraria"),
            competencias=request.POST.get("competencias"),
            habilidades=request.POST.get("habilidades"),
            ementa=request.POST.get("ementa"),
            conteudoprogramatico=request.POST.get("conteudoprogramatico"),
            bibliografiabasica=request.POST.get("bibliografiabasica"),
            bibliografiacomplementar=request.POST.get("bibliografiacomplementar"),
            percentualpratico=request.POST.get("percentualpratico"),
            percentualteorico=request.POST.get("percentualteorico")
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplina.html")

def alterarDisciplina(request, iddisciplina):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        disciplina = Disciplina.objects.get(iddisciplina=iddisciplina)
        disciplina.nome = request.POST.get("nome")
        disciplina.data = request.POST.get("data")
        disciplina.statusdisc = request.POST.get("statusdisc")
        disciplina.planodeensino = request.POST.get("plano")
        disciplina.cargahoraria = request.POST.get("cargahoraria")
        disciplina.competencias = request.POST.get("competencias")
        disciplina.habilidades = request.POST.get("habilidades")
        disciplina.ementa = request.POST.get("ementa")
        disciplina.conteudoprogramatico = request.POST.get("conteudoprogramatico")
        disciplina.bibliografiabasica = request.POST.get("bibliografiabasica")
        disciplina.bibliografiacomplementar = request.POST.get("bibliografiacomplementar")
        disciplina.percentualpratico = request.POST.get("percentualpratico")
        disciplina.percentualteorico = request.POST.get("percentualteorico")
        disciplina.save()
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplina.html", {'disciplina': Disciplina.objects.get(iddisciplina=iddisciplina)})

def deletarDisciplina(request, iddisciplina):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    disciplina = Disciplina.objects.get(iddisciplina=iddisciplina)
    disciplina.delete()
    return redirect('listardisciplinas')

def listarDisciplinasOfertadas(request):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    return render(request, 'listarDisciplinasOfertadas.html', {"disciplinasofertadas":Disciplinaofertada.objects.all()})

def inserirDisciplinaOfertada(request, iddisciplina):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    contexto ={
        'professores': Professor.objects.all(),
        'disciplina': Disciplina.objects.get(iddisciplina=iddisciplina),
        'cursos': Curso.objects.all(),
    }

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        curso = Curso.objects.get(idcurso=request.POST.get("curso"))
        disciplina = Disciplina.objects.get(iddisciplina = iddisciplina)
        Disciplinaofertada.objects.create(
            dtiniciomatricula = request.POST.get("dtiniciomatricula"),
            dtfimmatricula = request.POST.get("dtfimmatricula"),
            iddisciplina=disciplina,
            idcurso=curso,
            ano=request.POST.get("ano"),
            semestre=request.POST.get("semestre"),
            turma=request.POST.get("turma"),
            idprofessor=professor,
            metodologia=request.POST.get("metodologia"),
            recursos = request.POST.get("recursos"),
            criterioavaliacao = request.POST.get("criterios"),
            planodeaulas = request.POST.get("planodeaulas")
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplinaOfertada.html", contexto)

def alterarDisciplinaOfertada(request, iddisciplinaofertada):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        curso = Curso.objects.get(idcurso=request.POST.get("curso"))
        do = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
        do.dtiniciomatricula = request.POST.get("dtiniciomatricula")
        do.dtfimmatricula = request.POST.get("dtfimmatricula")
        do.idcurso=curso
        do.ano=request.POST.get("ano")
        do.semestre=request.POST.get("semestre")
        do.turma=request.POST.get("turma")
        do.idprofessor=professor
        do.metodologia=request.POST.get("metodologia")
        do.recursos = request.POST.get("recursos")
        do.criterioavaliacao = request.POST.get("criterios")
        do.planodeaulas = request.POST.get("planodeaulas")
        do.save()
        return redirect('listardisciplinasofertadas')
    else:
        do = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
        contexto ={
            'professores':Professor.objects.all(),
            'atividades': Atividade.objects.all(),
            'disciplinaofertada': Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada),
            'cursos': Curso.objects.all(),
            'disciplina': do.iddisciplina
        }
        return render(request, "formNovaDisciplinaOfertada.html", contexto)


def deletarDisciplinaOfertada(request, iddisciplinaofertada):
    try:
        if request.sessao.usuario.profile != "S" and request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
    disciplinaofertada.delete()
    return redirect ('listardisciplinasofertadas')
