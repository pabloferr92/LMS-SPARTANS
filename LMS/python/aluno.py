class Aluno:

    def __init__(self, nome, email, ra, celular, desconto):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = []

    def setnome(self, novoNome):
        self.__nome = novoNome

    def getNome(self):
        return self.__nome

    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def getEmail(self):
        return self.__email

    def setRa(self, novoRa):
        self.__ra=novoRa
    
    def getRa(self):
        return self.__ra
    
    def setCelular(self, novoCelular):
        self.__celular = novoCelular
    
    def getCelular(self):
        return self.__celular
    
    def setDesconto(self, novoDesconto):
        self.__desconto = novoDesconto
    
    def getDesconto(self):
        return self.__desconto
    
       
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