from tema_curs14 import Dreptunghi

dr = Dreptunghi(2, 2, 'rosu')


def test_descriere(): #unsure
    assert dr.descriere() == 'Dreptunghiul nostru are o lungime de 2, o latime de 2 si este rosu'


def test_aria():
    assert dr.aria() == 4


def test_perimetrul():
    assert dr.perimetrul() == 8


def test_schimba_culoare(): #very unsure
    new_color = dr.schimba_culoarea('roz')
    assert dr.culoare == 'roz'
    print(dr.culoare)






