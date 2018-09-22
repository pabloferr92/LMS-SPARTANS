from core.utils.utils import calculaMediaFinal

def test_calculaMediaFinal():
    assert calculaMediaFinal(10, 10) == 10.0

from core.utils.utils import geraNumeroRA
from core.utils.utils import calculaMedia
from core.utils.utils import descontaNota



def test_calculaMediaFinal1():
    assert calculaMediaFinal(5,5) == 5


def test_calculaMediaFinal2():
    assert calculaMediaFinal(7,7) == 7


def test_calculaMediaFinal3():
    assert calculaMediaFinal(6,7) == 6.4


def test_calculaMediaFinal4():
    assert calculaMediaFinal(3,8) ==5


def test_calculaMediaFinal5():
    assert calculaMediaFinal(9,6) == 7.8


def test_calculaMediaFinal6():
    assert calculaMediaFinal(-1,10) == None


def test_calculaMediaFinal7():
    assert calculaMediaFinal(10,11) == None


def test_geraNumeroRA1():
    assert geraNumeroRA(1800020) == 1800021


def test_geraNumeroRA2():
    assert geraNumeroRA(1701234) == 1800001


def test_geraNumeroRA3():
    assert geraNumeroRA('') == 1800001


def test_geraNumeroRA4():
    assert geraNumeroRA(1800999) == 1801000


def test_geraNumeroRA5():
    assert geraNumeroRA(1801234) == 1801235

def test_calculaMedia1():
    assert calculaMedia([8.0]) == 8.0


def test_calculaMedia2():
    assert calculaMedia([10.0,6.0,8.0]) == 8.0


def test_calculaMedia3():
    assert calculaMedia([9.0, 6.0, 6.0,  7.0]) == 7.0


def test_calculaMedia4():
    assert calculaMedia([6.0, 6.0, 9.0, 6.0, 6.0, 7.0, 8.0, 8.0]) == 7.0


def test_calculaMedia5():
    assert calculaMedia([10.0, 10.0, 9.0, 9.0, 8.0, 8.0, 7.0, 7.0, 6.0, 6.0]) == 8.0


def test_descontaNota1():
    assert descontaNota (8,30) == 5.6


def test_descontaNota2():
    assert descontaNota (10,20) == 8.0


def test_descontaNota3():
    assert descontaNota (7,25) == 5.25


def test_descontaNota4():
    assert descontaNota (8.5,30) == 5.95


def test_descontaNota5():
    assert descontaNota (6,20) == 4.8
