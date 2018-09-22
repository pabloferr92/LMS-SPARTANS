from difflib import SequenceMatcher
import time

def calculaMediaFinal(ac, prova):
    if ac < 0 or ac > 10 or prova < 0 or prova > 10:
        return None
    else:
        media = (ac * 0.6) + (prova * 0.4)
        return media
    

def geraNumeroRA(ultimoRA):
    ano = time.strftime("%y")
    if(str(ultimoRA)[:2] == ano):
        return ultimoRA+1
    return int(''.join([str(ano), '00001']))

def calculaMedia(listaNotas):
    nota = 0
    for i in listaNotas:
        nota += i
    media = nota / len(listaNotas)
    return media


def descontaNota(nota, porcentagem):
    desconto = nota - (nota * porcentagem/100)
    return desconto


def verificaCopia(texto1, texto2):
    s = SequenceMatcher(None, texto1, texto2)
    if s.ratio() > 0.8:
        return True
    else:
        return False