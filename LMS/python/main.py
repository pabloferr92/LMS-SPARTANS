from professor import Professor
from disciplina import Disciplina
from aluno import Aluno


p1= Professor(nome='pablo', email='pablo',ra=12,celular=9999)
d1=Disciplina(nome='lp2', cargaHoraria=80,mensalidade=100, professor=p1)

a= Aluno(nome='pablo', email='pablo', ra='123', celular='0999999', desconto=50)

a.adicionaDisciplina(d1)
a.diminuirDesconto(25)
print(a.retornaValorMensalidade())
print (a.retornaCargaHoraria())