"""Pruebas del lexer: del texto a los tokens."""

import pytest
from mini_interprete.lexer import tokenizar
from mini_interprete.tokens import Token, TipoToken


def test_tokeniza_un_numero_solo():
    assert tokenizar("42") == [Token(TipoToken.NUMERO, 42, 0)]

def test_tokeniza_una_suma():
    assert tokenizar("3+4") == [
        Token(TipoToken.NUMERO, 3, 0),
        Token(TipoToken.MAS, "+", 1),
        Token(TipoToken.NUMERO, 4, 2),
    ]

#falta ver la multi, la division, la resta y los parentesis en op
#y si le pongo espacios?


def test_los_espacios_no_producen_tokens():
    assert len(tokenizar("  3   +   4  ")) == 3

#y si es una cadena vacia o un numero negativo    


def test_tokeniza_parentesis():
    tipos = [token.tipo for token in tokenizar("(3)")]
    assert tipos == [TipoToken.PAR_IZQ, TipoToken.NUMERO, TipoToken.PAR_DER]

#y si no hay nada dentro de los paréntesis

# Añadimos las pruebas que planteamos
def test_tokeniza_numero_negativo():
    entrada = "-1"
    assert tokenizar(entrada) == [
        Token(TipoToken.MENOS, "-", 0), 
        Token(TipoToken.NUMERO, 1, 1),
        ]

def test_tokeniza_operaciones_basicas_combinadas():
    entrada = "(4 - 2) / (2 * 1)"
    assert tokenizar(entrada) == [
        Token(TipoToken.PAR_IZQ, "(", 0),
        Token(TipoToken.NUMERO, 4, 1), 
        Token(TipoToken.MENOS, "-", 3), 
        Token(TipoToken.NUMERO, 2, 5), 
        Token(TipoToken.PAR_DER, ")",6), 
        Token(TipoToken.ENTRE, "/", 8), 
        Token(TipoToken.PAR_IZQ, "(",10), 
        Token(TipoToken.NUMERO, 2, 11), 
        Token(TipoToken.POR, "*", 13), 
        Token(TipoToken.NUMERO, 1, 15), 
        Token(TipoToken.PAR_DER, ")", 16),
        ]

def test_tokeniza_simbolo_extranio():
    entrada = "3 + @"
    assert tokenizar(entrada) == [
        Token(TipoToken.NUMERO, 3, 0), 
        Token(TipoToken.MAS, "+", 2)
        ]

def test_tokeniza_numero_con_espacio_al_inicio():
    entrada = " 42"
    assert tokenizar(entrada) == [Token(TipoToken.NUMERO, 42, 1)]

def test_tokeniza_cadena_vacia():
    entrada = ""
    assert tokenizar(entrada) == []
