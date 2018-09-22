class Aluno:

    def __init__(self, logon, nome, email, celular, foto, dataExpiracao, ra, desconto):
        self.__logon = logon
        self.__nome = nome
        self.__email = email
        self.__celular = celular
        self.__foto = foto
        self.__dataExpiracao = dataExpiracao
        self.__ra = ra
        self.__desconto = desconto
        self.__disciplinas = []

    def getLogon(self):
        return self.__logon

    def setLogon(self, novoLogon):
        self.__logon = novoLogon

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getEmail(self):
        return self.__email

    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def getFoto(self):
        return self.__foto

    def setFoto(self, novaFoto):
        self.__foto = novaFoto

    def getDataExpiracao(self):
        return self.__dataExpiracao

    def setDataExpiracao(self, novaDataExpiracao):
        self.__dataExpiracao = novaDataExpiracao

    def getRa(self):
        return self.__ra

    def setRa(self, novoRa):
        self.__ra=novoRa

    def setCelular(self, novoCelular):
        self.__celular = novoCelular

    def getCelular(self):
        return self.__celular

    def getDesconto(self):
        return self.__desconto

    def setDesconto(self, novoDesconto):
        self.__desconto = novoDesconto

    def getDisciplina(self):
        return self.__disciplina

    def adicionaDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def aumentarDesconto(self, aumento):
        self.__desconto + = aumento

    def diminuirDesconto(self, diminui):
        self.__desconto - = diminui

    def retornaSobrenome(self):
        return self.__nome.split()[-1]

    def retornaValorMensalidade(self):
        mensalidadetotal = 0
        for disciplina in self.__disciplinas:
            mensalidadetotal + = disciplina.getMensalidade()*(100-self.__desconto)/100
        return mensalidadetotal

    def retornaCargaHoraria(self):
        cargahorariatotal = 0
        for disciplina in self.__disciplinas:
            cargahorariatotal + = disciplina.getCargaHoraria()
        return cargahorariatotal
