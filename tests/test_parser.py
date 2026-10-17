"""Pruebas del parser: de los tokens al AST."""

import pytest
from mini_interprete.ast import Numero, OperacionBinaria
from mini_interprete.lexer import tokenizar
from mini_interprete.parser import Parser
from mini_interprete.errores import ErrorDeSintaxis


def arbol_de(texto):
    return Parser(tokenizar(texto)).parsear()


def test_construye_el_arbol_de_una_suma():
    assert arbol_de("3 + 4") == OperacionBinaria("+", Numero(3), Numero(4))

#de las demas op

def test_la_multiplicacion_se_agrupa_antes_que_la_suma():
    # 3 + 4 * 2  debe agruparse como  3 + (4 * 2)
    assert arbol_de("3 + 4 * 2") == OperacionBinaria(
        "+", Numero(3), OperacionBinaria("*", Numero(4), Numero(2))
    )


def test_los_parentesis_cambian_la_agrupacion():
    # (3 + 4) * 2  debe agruparse al reves
    assert arbol_de("(3 + 4) * 2") == OperacionBinaria(
        "*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2)
    )


#Añadimos las pruebas que planteamos

def test_construye_arbol_de_una_resta():
    assert arbol_de("5 - 2") == OperacionBinaria("-", Numero(5), Numero(2))
    
def test_construye_arbol_de_una_multiplicacion():
    assert arbol_de("4 * 3") == OperacionBinaria("*", Numero(4), Numero(3))

def test_construye_arbol_de_una_division():
    assert arbol_de("8 / 2") == OperacionBinaria("/", Numero(8), Numero(2))

@pytest.mark.xfail(reason="salta un error de tipo IndexError en lugar de ErrorDeSintaxis, aqui el parser no sabe manejarlo")
def test_error_construye_arbol_de_cadena_vacia():
    with pytest.raises(ErrorDeSintaxis):
        arbol_de("")
    
@pytest.mark.xfail(reason = "salta un error de tipo IndexError en lugar de ErrorDeSintaxis, aqui el parser no sabe manejarlo bien")
def test_error_falta_parentesis_de_cierre():
    with pytest.raises(ErrorDeSintaxis):
        arbol_de("(3 + 4")

def test_error_operadores_consecutivos():
    with pytest.raises(ErrorDeSintaxis):
        arbol_de("3 ++ 4")