"""Pruebas del evaluador: del AST a un numero."""

from mini_interprete.cli import interpretar


def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14
