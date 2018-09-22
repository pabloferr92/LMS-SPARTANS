CREATE DATABASE LMS2
GO

USE LMS2

create table administrador (
idAdministrador int primary key identity (1,1)
,logon VARCHAR (20) UNIQUE
,senha VARCHAR (20) NOT NULL
,nome varchar (40) null
,email VARCHAR  (40) UNIQUE NOT NULL
,celular CHAR(9)  UNIQUE
,dtExpiracao DATE DEFAULT GETDATE()
)

GO
CREATE TABLE coordenador (
idCoordenador int primary key identity (1,1)
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR(30) NOT NULL
, email VARCHAR  (40) UNIQUE not null
, celular CHAR(9)  UNIQUE
, dtExpiracao DATE DEFAULT GETDATE()
)
GO
CREATE TABLE aluno (
idAluno INT identity (1,1)  PRIMARY KEY
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR(30) NOT NULL
, email VARCHAR  (40) UNIQUE NOT NULL
, celular CHAR(9)  UNIQUE
, foto nvarchar (max) NULL
, dtExpiracao DATE DEFAULT GETDATE()
, ra VARCHAR (20)
)

go
CREATE TABLE professor (
idProfessor INT identity (1,1) PRIMARY KEY
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR(30) NOT NULL
, email VARCHAR  (40) UNIQUE NOT NULL
, celular CHAR(9)  UNIQUE
, dtExpiracao DATE DEFAULT GETDATE()
, apelido VARCHAR (20)
)
go
CREATE TABLE disciplina (
idDisciplina INT identity (1,1)
, nome VARCHAR (30) UNIQUE
, data DATE DEFAULT GETDATE()
, statusDisc VARCHAR (20) DEFAULT('Aberta')
check (statusDisc ='Aberta' or statusDisc = 'Fechada')
, planoDeEnsino VARCHAR (1000)
, cargaHoraria INT
CHECK(cargaHoraria = 80 or cargaHoraria = 40)
, competencias VARCHAR (1000)
, habilidades VARCHAR (1000)
, ementa VARCHAR (1000)
, conteudoProgramatico VARCHAR (1000)
, bibliografiaBasica VARCHAR (1000)
, bibliografiaComplementar VARCHAR (1000)
, percentualPratico INT
CHECK(percentualPratico >=0 AND percentualPratico <= 100)
, percentualTeorico INT
CHECK(percentualTeorico >=0 AND percentualTeorico <= 100)
, CONSTRAINT pkDisciplina PRIMARY KEY (idDisciplina)
)
GO
CREATE TABLE curso (
idCurso INT identity (1,1) PRIMARY KEY
, nome varchar(30) UNIQUE NOT NULL
,idCoordenador int null
constraint fkIdCoordenadorCurso references coordenador (idCoordenador)
)
CREATE TABLE disciplinaOfertada (
idDisciplinaOfertada INT identity (1,1) PRIMARY KEY
, dtInicioMatricula DATE NULL
, dtFimMatricula DATE NULL
, IdDisciplina INT NOT NULL
, idCurso INT NOT NULL
, ano INT NOT NULL
, semestre INT NOT NULL
, turma VARCHAR(6)
, idProfessor INT NULL
, metodologia VARCHAR(1000) NULL
, recursos VARCHAR(1000) NULL
, criterioAvaliacao VARCHAR(1000) NULL
, planoDeAulas VARCHAR(1000) NULL
, CONSTRAINT fkIdDisciplinaDo FOREIGN KEY (IdDisciplina) REFERENCES disciplina(idDisciplina)
, CONSTRAINT fkIdProfessorDo FOREIGN KEY (IdProfessor) REFERENCES professor(idProfessor)
, CONSTRAINT ckAno CHECK (ano BETWEEN 1900 AND 2100)
, CONSTRAINT ckSemestre CHECK (semestre BETWEEN 1 AND 2)
, CONSTRAINT ckTurma CHECK (turma BETWEEN 'A' AND 'Z')
, CONSTRAINT fkCurso FOREIGN KEY (idCurso) REFERENCES curso (idCurso)
)

GO

CREATE TABLE solicitacaoMatricula
(
idSolicitacaoMatricula INT identity (1,1) PRIMARY KEY
, idAluno INT NOT NULL
, idDisciplinaOfertada INT NOT NULL
, dtSolicitacao DATE DEFAULT GETDATE() NOT NULL
, [status] VARCHAR (100) DEFAULT 'SOLICITADA' CHECK ([status]= 'SOLICITADA' or [status]= 'APROVADA' or [status]= 'REJEITADA' or [status]= 'CANCELADA')
, CONSTRAINT fkIdAluno FOREIGN KEY (idAluno) REFERENCES aluno (idAluno)
, CONSTRAINT fkIdDisciplinaOfertada FOREIGN KEY (idDisciplinaOfertada)
	REFERENCES disciplinaOfertada (idDisciplinaOfertada)
)
GO
CREATE TABLE atividade
(
idAtividade INT NOT NULL PRIMARY KEY identity (1,1)
, titulo VARCHAR (50)
, descricao VARCHAR (1000) NOT NULL
, conteudo VARCHAR (1000) NULL
, tipo VARCHAR (50) CHECK(tipo = 'RESPOSTA ABERTA' or tipo = 'TESTE')
, extra VARCHAR (1000) NULL
, idProfessor INT NOT NULL FOREIGN KEY REFERENCES professor (idProfessor)
)

GO
CREATE TABLE atividadeVinculada (
idAtividadeVinculada INT identity (1,1)NOT NULL PRIMARY KEY
, idProfessor INT NOT NULL
, idAtividade INT NOT NULL
, idDisciplinaOfertada INT NOT NULL
, rotulo VARCHAR (100) NOT NULL UNIQUE (idAtividade, idDisciplinaOfertada)
, CONSTRAINT fkidAtividade FOREIGN KEY (idAtividade) REFERENCES atividade (idAtividade)
, CONSTRAINT fkidProfessor FOREIGN KEY (idProfessor) REFERENCES professor (idProfessor)
, CONSTRAINT fkidDisciplinaOfertadaAv FOREIGN KEY (IdDisciplinaOfertada) REFERENCES disciplinaOfertada (idDisciplinaOfertada)
, estado VARCHAR (100)
check (estado ='Disponibilizada' or estado ='Aberta' or estado = 'Fechada' or estado = 'Encerrada' or estado = 'Prorrogada')
, dtInicioRespostas DATE
, dtFimRespostas DATE
)

GO
CREATE TABLE entrega (
idEntrega INT identity(1,1) PRIMARY KEY
, idAluno INT NOT NULL
, titulo VARCHAR (40)
, resposta VARCHAR(1000)
, idAtividadeVinculada INT NOT NULL
, dtEntrega DATE DEFAULT GETDATE() NOT NULL
, [status] VARCHAR(20) DEFAULT('ENTREGUE') CHECK([status] = 'ENTREGUE' or [status] = 'CORRIGIDO')
, nota DECIMAL(4,2) NULL
, dtAvaliacao DATE NULL
, obs VARCHAR(1000)
, CONSTRAINT fkidAlunoEntrega FOREIGN KEY (idAluno) REFERENCES aluno (idAluno)
, CONSTRAINT ckNota CHECK (nota BETWEEN 0 AND 10)
, CONSTRAINT fkAtividadeVinculada FOREIGN KEY (idAtividadeVinculada)
REFERENCES atividadeVinculada (idAtividadeVinculada)
)

GO
CREATE TABLE mensagem (
idMensagem INT NOT NULL PRIMARY KEY identity (1,1)
, idAluno INT  NULL
, idProfessor INT  NULL
, assunto VARCHAR (1000) NULL
, referencia VARCHAR (1000) NULL
, conteudo VARCHAR (1000) NULL
, [status] VARCHAR (50) CHECK([status] = 'ENVIADO' or [status] = 'LIDO' or [status] = 'RESPONDIDO')
, dtEnvio DATE DEFAULT GETDATE()
, dtResposta DATE  NULL
, resposta VARCHAR (1000) NULL
, origem varchar (1) not null
, CONSTRAINT fkidAlunoMensagem FOREIGN KEY (idAluno) REFERENCES aluno (idAluno)
, CONSTRAINT fkidProfessorMensagem FOREIGN KEY (idProfessor) REFERENCES professor (idProfessor)
)

GO
CREATE TABLE sessao (
id VARCHAR(32) PRIMARY KEY
, idAluno INT NULL
, idProfessor INT NULL
, idCoordenador INT NULL
,idAdministrador int null
, CONSTRAINT fkidAlunoSessao FOREIGN KEY (idAluno) REFERENCES aluno (idAluno)
, CONSTRAINT fkidProfessorSessao FOREIGN KEY (idProfessor) REFERENCES professor (idProfessor)
, CONSTRAINT fkIdCoordenadorSessao FOREIGN KEY (idCoordenador) REFERENCES coordenador (idCoordenador)
,constraint fkIdAdmin foreign key (idAdministrador) references administrador (idAdministrador)
)

GO



-------------------------------------------------------------------------------

----------------------- INICIO AC6 ----------------
------------------------------GUILHERME-------------------------------------------------
/* --Cadastrem: 1 Coordenador, 10 Alunos, ---5 Professores ----- ( INSERT )-- */

insert into coordenador(LOGON,Senha,Nome,Email,Celular)
Values
('Pablo','impacta','coordenador1','coordenador1@gmail.com','999999999'),
('Luiz','impacta','coordenador2','coordenador2@gmail.com','99999998'),
('Douglas','impacta','coordenador3','coordenador3@gmail.com','999999997'),
('Guilherme','impacta','coordenador4','coordenador4@gmail.com','999999996'),
('Matias','impacta','coordenador5','coordenador5@gmail.com','999999995'),
('Silvio','impacta','coordenador6','coordenador6@gmail.com','999999994'),
('Pablo Vitar','impacta','coordenador7','coordenador7@gmail.com','999999993'),
('Thamy Gretchen','impacta','coordenador8','coordenador8@gmail.com','999999992'),
('Sashe Grey','impacta','coordenador9','coordenador9@gmail.com','999999991')

go
insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('PabloImpacta','impacta','Pablo','pabloaluno@gmail.com','999999999','10000')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('LuizImpacta','impacta','Luiz','luizaluno@gmail.com','999999987','10001')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('MarcosImpacta','impacta','Marcos','marcoaluno@gmail.com','99999923','10002')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('GuilhermeImpacta','impacta','Guilherme','guialuno@gmail.com','99999943','10003')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('LucasImpacta','impacta','Lucas','lucasaluno@gmail.com','999999943','10004')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('DouglasImpacta','impacta','Douglas','dougaluno@gmail.com','999999234','10005')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('FraImpacta','impacta','Francoise','franaluno@gmail.com','999999453','10006')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('Juliaimpacta','impacta','Julia','Juliaaluno@gmail.com','999995467','10007')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('Jesusimpacta','impacta','Jesus','jesusaluno@gmail.com','999992314','10008')

insert into aluno(LOGON,Senha,Nome,Email,Celular,RA)
Values('Milaimpacta','impacta','Mila','milaaluno@gmail.com','999362314','10009')

go

insert into professor (logon,senha,nome,email,celular,dtExpiracao,apelido) values
('professor1', 'abc321', 'Renato Seixas The Best', 'professor1@gmail.com', '99999991', '07-01-2018', 'Seixas'),
('professor2', 'abc321', 'Gustavo Maia', 'professor2@gmail.com', '99999992', '07-01-2018', 'Maia'),
('professor3', 'abc321', 'Yuri Dirickson', 'professor3@gmail.com', '99999993', '07-01-2018', 'Dirickson'),
('professor4', 'abc321', 'Fernando Sousa', 'professor4@gmail.com', '99999994', '07-01-2018', 'Sousa'),
('professor5', 'abc321', 'Fabio Campos', 'professor5@gmail.com', '99999995', '07-01-2018', 'Campos')

go

------------------------------GUILHERME-------------------------------------------------
/*�	Cadastrem todos os cursos existentes nesta universidade, se quiserem,
podem utilizar os nomes reduzidos dos mesmos, ADS, SI, etc. ( INSERTT ) */
go

insert into Curso(Nome)
Values('ADS')

insert into Curso(Nome)
Values('ADM')

insert into Curso(Nome)
Values('BD')

insert into Curso(Nome)
Values('GTI')

insert into Curso(Nome)
Values('JD')

insert into Curso(Nome)
Values('PG')

insert into Curso(Nome)
Values('PM')

insert into Curso(Nome)
Values('REDES')

insert into Curso(Nome)
Values('SI')

go
------------------------------GUILHERME-------------------------------------------------

/*	Criem 2 Disciplinas ( planos de ensino ) � Linguagem SQL e Tec Web
( utilizem dados reais para preencher a tabela,
 vejam os planos de ensino apresentados ( INSERT ) */

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('Linguagem SQL', 'Aberta', 'Conceitos basicos, Linguagem SQL, Manipula��o de Dados e etc..' ,80,'Arquitetar um Banco de dados, Garantir a integridade e criar relatorios','Conhecimento aprofundado sobre SQL e sua linguagem',
'Introdu��o a linguagem,Linguagem de Manipula��o de dados, Fun��es e Vis�es','Historia da Linguagem, O modelo fisico, Create, Alter, Drop e Update, Insert, Delete e Join,Revisao e Prova ','DATE, C.J. SQL e Teoria Relacional: Como escrever codigos em SQL precisos - S�o Paulo:Novatec, 2015','ELMASRI, R.E.; NAVATHE, S. B. Sistemas de Banco de Dados. Ed. S�o Paulo: Pearson. 2011',75,25)

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('Tecnologia Web','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)

go

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('BANCO DE DADOS','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('DevOps','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('LINGUAGEM PROGRAMACAO 1','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('REDES','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)

insert into disciplina(Nome,statusDisc, planoDeEnsino,cargaHoraria,competencias,habilidades,ementa,conteudoProgramatico,bibliografiaBasica,bibliografiaComplementar,percentualPratico,percentualTeorico)
Values('IOT','Aberta','Conceitos basicos de HTML5,CSS3,JavaScripts ao avan�ado, Introdu��o e ferramentas ao Django',80,'Desenvolver aplica��o Web','Conhecer e dominar as principais maneiras de  constru��o de publica��o de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts','Introdu��o a HTML5,CSS3 e JavaScripts programa��o avan�ada, revis�o e prova','Use a Cabe�a!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edi��o, 2015','Moraes, Construindo Aplica��es Web. S�o Paulo, NovaTec,2015',50,50)
----------------------------------------------------------MATIAS--------------------------------------------------------------

/* 	Ofertem a Disciplina �Linguagem SQL� em 2018, 1�semestre,
 turma B, para os cursos de SI e ADS. ( INSERT ) */

insert into disciplinaOfertada(DtInicioMatricula,DtFimMatricula,IdDisciplina,IdCurso,Ano,Semestre,Turma,IdProfessor,Metodologia,Recursos,CriterioAvaliacao,PlanoDeAulas)
values
('2018-04-16','2019-04-16',01,01,2018,01,'ADS2B',01,'Aulas utilizando projetor, lousa e computador, cada aula ter� 50 minutos e atividades cont�nuas di�rias.',
'M�quina virtual com servidor Microsoft SQL Server 2014','Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Historia da Linguagem, O modelo fisico, Create, Alter, Drop e Update, Insert, Delete e Join,Revisao e Prova '),

('2018-02-10','2024-04-02',01,09,2018,02,'SI2B',01,'Aulas utilizando projetor, lousa e computador, cada aula ter� 50 minutos e atividades cont�nuas di�rias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts'),

('2018-02-10','2024-04-02',02,09,2018,02,'SI2B',01,'Aulas utilizando projetor, lousa e computador, cada aula ter� 50 minutos e atividades cont�nuas di�rias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts'),

('2018-02-10','2024-04-02',03,09,2018,02,'SI2B',02,'Aulas utilizando projetor, lousa e computador, cada aula ter� 50 minutos e atividades cont�nuas di�rias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts'),

('2018-02-10','2024-04-02',04,09,2018,02,'SI2B',02,'Aulas utilizando projetor, lousa e computador, cada aula ter� 50 minutos e atividades cont�nuas di�rias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Tecnologias para desenvolvimento de aplica��es web com HTML5,CSS3 e JavaScripts')




go
-----------------------------------MATIAS-------------------------------------------------------

/* Atribuam um Professor diferente � cada uma das disciplinas ofertadas
 ( utilizem o UPDATE alterar uma disciplina ofertada j� criada ),
  preenchendo as demais colunas com dados reais ( ver plano de ensino ). ( UPDATE ) */
	update disciplinaOfertada set idProfessor = '02' where idDisciplinaOfertada = '01'
	update disciplinaOfertada set idProfessor = '01' where idDisciplinaOfertada = '02'


----------------------------------- MATIAS-----------------------------------------------------------------------------------------
go
/* Atribuam datas de inicio e fim de matricula �s disciplinas
ofertadas ( utilizem o UPDATE alterar uma disciplina ofertada j� criada ). (UPDATE ) */

	update disciplinaOfertada set dtInicioMatricula = '2019-02-02' where idDisciplinaOfertada = '01'
	update disciplinaOfertada set dtFimMatricula = '2019-07-07' where idDisciplinaOfertada = '01'
	update disciplinaOfertada set dtInicioMatricula = '2018-07-30' where idDisciplinaOfertada = '02'
	update disciplinaOfertada set dtFimMatricula = '2018-12-10' where idDisciplinaOfertada = '02'


-----------------------------------------DOUGLAS------------------------------------------------------------
go
/* 	Preencham a solicita��o de matricula de pelo menos 3 alunos
em cada uma das 2 Disciplinas ofertadas. ( INSERT ) */

insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao)
values (01,01,'2018-04-03')

insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao)
values (01,02,'2018-04-08')

insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao)
values (01,03,'2018-03-05')

insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao)
values (01,03,'2018-06-03')


insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,dtSolicitacao)
values (01,02,'2018-06-12')


insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao,[status])
values (02,1,'2018-05-22','Aprovada')
insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao,[status])
values (02,2,'2018-05-22','Aprovada')
insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao,[status])
values (02,3,'2018-05-22','Aprovada')
insert into solicitacaoMatricula (idAluno,idDisciplinaOfertada,DtSolicitacao,[status])
values (02,4,'2018-05-22','Aprovada')





-----------------------------------------DOUGLAS------------------------------------------------------------
go
/*	Atualize as solicita��es de matricula,
atribuindo status diversos �s mesmas, aprovando algumas, rejeitando outras ( UPDATE ) */
update solicitacaoMatricula set [Status] = 'Aprovada' where idSolicitacaoMatricula = 02

update solicitacaoMatricula set [Status] = 'Rejeitada' where idSolicitacaoMatricula = 03

update solicitacaoMatricula set [Status] = 'Cancelada' where idSolicitacaoMatricula = 06

go
-----------------------------------------DOUGLAS------------------------------------------------------------

/* Criem 2 atividades, e depois vincule uma destas atividades � disciplina ofertada
 �Linguagem SQL�, ano 2018, 1�semestre, turma B, curso SI. ( INSERT ) */

insert into atividade (titulo,descricao,conteudo,idProfessor)
values('ATIVIDADE TIPO 1','Construir um formul�rio que tenha campos login e senha','Verificar os slides da aula anterior',01)

insert into atividade (titulo,descricao,conteudo,idProfessor)
values('ATIVIDADE TIPO 2','Construir o CSS3 do formul�rio de Login','Verificar os slides da aula anterior',01)

go

insert into atividadeVinculada (idProfessor,idAtividade,idDisciplinaOfertada,rotulo,estado, dtInicioRespostas, dtFimRespostas)
	values
	(1,1,1,'AC1','ABERTA','05-16-2018', '05-25-2018'),
	(2,1,2,'AC2','ABERTA','05-16-2018', '05-25-2018'),
	(3,1,3,'AC3','ABERTA','05-16-2018', '05-25-2018'),
	(4,1,4,'AC4','ABERTA','05-16-2018', '05-25-2018'),
	(5,1,5,'AC5','ABERTA','05-16-2018', '05-25-2018'),
	(1,2,1,'AC6','ABERTA','05-16-2018', '05-25-2018'),
	(2,2,2,'AC7','ABERTA','05-16-2018', '05-25-2018'),
	(3,2,3,'AC8','ABERTA','05-16-2018', '05-25-2018'),
	(4,2,4,'AC9','ABERTA','05-16-2018', '05-25-2018'),
	(5,2,5,'AC10','ABERTA','05-16-2018', '05-25-2018')

go
-----------------------------------------------------------------------------------------------------
------------------------- PABLO --------------------

/* Realizem 2 entregas destes trabalhos vinculados, realizados por qualquer aluno. ( INSERT). */

insert into entrega (idAluno,titulo,resposta,idAtividadeVinculada,dtAvaliacao,obs)
values
(1,'Atividade 1', 'segue minha resposta 1', 1,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(2,'Atividade 1', 'segue minha resposta 2', 2,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(3,'Atividade 1', 'segue minha resposta 1', 3,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(4,'Atividade 1', 'segue minha resposta 2', 4,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(1,'Atividade 1', 'segue minha resposta 1', 5,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(2,'Atividade 1', 'segue minha resposta 2', 1,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(3,'Atividade 1', 'segue minha resposta 1', 2,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(4,'Atividade 1', 'segue minha resposta 2', 3,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(1,'Atividade 1', 'segue minha resposta 1', 4,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia'),
(2,'Atividade 1', 'segue minha resposta 2', 5,'01-01-2018','Atividade Referente � AC5 de Linguagem SQL Professor Gustavo Maia')


go
-------------------------PABLO ----------------------

/* Atualizem uma destas entregas, atribuindo uma nota pelo professor vigente
daquela disciplina ofertada. ( UPDATE ). */

update entrega set nota ='10' where idEntrega ='1'

go
-------------------------------------------DOUGLAS ----------------------------
/* �	Cadastrem o envio de 1 d�vida de um aluno qualquer, ao professor da
disciplina de Linguagem SQL com a seguinte mensagem: �qual a data de entrega da AC6 ?� ( INSERT ) */

insert into mensagem(idAluno,idProfessor,assunto,referencia,conteudo,[Status],dtEnvio, dtResposta, resposta, origem)
values(1,1,'Duvida','TecWeb','Qual a data da entrega da AC6?','Enviado','01-01-1992','01-10-1992','recebido', 'P')

go
-----------------------------------DOUGLAS ------------------------------

/* Registrem a resposta do professor � mensagem acima, informando que a
�a data de entrega da AC6 � na pr�xima semana�.(UPDATE) */

update mensagem set DtResposta = '2018-04-17' where idMensagem = 1

update mensagem set Resposta = 'A data da entrega � na proxima semana' where idMensagem = 1


-------------------- Criação de usuario admin ------------------

insert into administrador(logon,Senha,Nome,Email,Celular)
Values('spartansadmin','spartans','SPARTANS','spartans@spartans.com','999942131')

insert into administrador(logon,Senha,Nome,Email,Celular)
Values('teste','teste','teste','teste@teste.com','999942128')
