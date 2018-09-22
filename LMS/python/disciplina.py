class Disciplina:

    def __init__(self, nome, data, status, planoDeEnsino, cargaHoraria, competencias, habilidades, ementa, conteudoProgramatico, bibliografiaBasica, bibliografiaComplementar, percentualPratico, percentualTeorico, mensalidade, coordenador):
        self.__nome = nome
        self.__data = data
        self.__status = status
        self.__planoDeEnsino = planoDeEnsino
        self.__cargaHoraria = cargaHoraria
        self.__competencias = competencias
        self.__habilidades = habilidades
        self.__ementa = ementa
        self.__conteudoProgramatico = conteudoProgramatico
        self.__bibliografiaBasica = bibliografiaBasica
        self.__bibliografiaComplementar = bibliografiaComplementar
        self.__percentualPratico = percentualPratico
        self.__percentualTeorico = percentualTeorico
        self.__mensalidade = mensalidade
        self.__coordenador = coordenador

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getData(self):
        return self.__data

    def setData(self, novaData):
        self.__data = novaData

    def getStatus(self):
        return self.__status

    def setStatus(self, novoStatus):
        self.__status = novoStatus

    def getPlanoDeEnsino(self):
        return self.__planoDeEnsino

    def setPlanoDeEnsino(self, novoPlanoDeEnsino):
        self.__planoDeEnsino = novoPlanoDeEnsino

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def setCargaHoraria(self, novaCargaHoraria):
        self.__cargaHoraria = novaCargaHoraria

    def getCompetencias(self):
        return self.__competencias

    def setCompetencias(self, novasCompetencias):
        self.__competencias = novasCompetencias

    def getHabilidades(self):
        return self.__habilidades

    def setHabilidades(self, novasCompetencias):
        self.__competencias = novasCompetencias

    def getEmenta(self):
        return self.__ementa

    def setEmenta(self, novaEmenta):
        self.__ementa = novaEmenta

    def getConteudoProgramatico(self):
        return self.__conteudoProgramatico

    def setConteudoProgramatico(self, novoConteudoProgramatico):
        self.__conteudoProgramatico = novoConteudoProgramatico

    def getBibliografiaBasica(self):
        return self.__bibliografiaBasica

    def setBibliografiaBasica(self, novaBibliografiaBasica):
        self.__bibliografiaBasica = novaBibliografiaBasica

    def getBibliografiaComplementar(self):
        return self.__bibliografiaComplementar

    def setBibliografiaComplementar(self, novaBibliografiaComplementar):
        self.__bibliografiaComplementar = novaBibliografiaComplementar

    def getPercentualPratico(self):
        return self.__percentualPratico

    def setPercentualPratico(self, novoPercentualPratico):
        self.__percentualPratico = novoPercentualPratico

    def getPercentualTeorico(self):
        return self.__percentualTeorico

    def setPercentualTeorico(self, novoPercentualTeorico):
        self.__percentualTeorico = novoPercentualTeorico

    def getMensalidade(self):
        return self.__mensalidade

    def setMensalidade(self, novoMensalidade):
        self.__mensalidade = novoMensalidade

    def getCoordenador(self):
        return self.__coordenador

    def setCoordenador(self, novoCoordenador):
        self.__coordenador = novoCoordenador

    def retornaValorHora(self):
        valor = self.mensalidade*6 / self.__cargaHoraria
        return valor
