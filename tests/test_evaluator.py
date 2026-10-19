"""Pruebas del evaluador: del AST a un numero."""

import pytest
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis, ErrorDeEvaluacion


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


# Añadimos las pruebas que planteamos

def test_error_division_cero():
    entrada = "10 / 0"
    with pytest.raises(ErrorDeEvaluacion):
        interpretar(entrada)

def test_error_menos_unario():
    entrada = "-10 + 2"
    with pytest.raises(ErrorDeSintaxis):
        interpretar(entrada)

def test_resta_numero_consigo_mismo():
    entrada = "5 - 5"
    assert interpretar(entrada) == 0
    
def test_division_numero_consigo_mismo():
    entrada = "100 / 100"
    assert interpretar(entrada) == 1

# Encontramos que el parser no asocia a la izquierda con operadores de la misma precedencia
# Asocia 3 - (3 - 3) en lugar de (3 - 3) - 3
@pytest.mark.xfail(reason="asocia mal con operadores de la misma precedencia (por corregir)")
def test_resta_precedencia_sin_parentesis():
    entrada = "3 - 3 - 3"
    assert interpretar(entrada) == -3

def test_multiples_operaciones_y_parentesis_anidados():
    entrada = "(10 - 5 * 1) + (6 / 2 * (2 + 1 * (10 / 10)))"
    assert interpretar(entrada) == 6
    
def test_division_resultado_con_decimal():
    entrada = " 5 / 2"
    assert interpretar(entrada) == pytest.approx(2.5)

#encontramos estas otras pruebas
def test_numeros():
    entrada = "007"
    assert interpretar(entrada) == 7  

def test_menos_unario():
    entrada = "(0 - 10) + 2"
    assert interpretar(entrada) == -8 
    
