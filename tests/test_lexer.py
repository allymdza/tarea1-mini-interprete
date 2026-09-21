"""Pruebas del lexer: del texto a los tokens."""

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


def test_los_espacios_no_producen_tokens():
    assert len(tokenizar("  3   +   4  ")) == 3


def test_tokeniza_parentesis():
    tipos = [token.tipo for token in tokenizar("(3)")]
    assert tipos == [TipoToken.PAR_IZQ, TipoToken.NUMERO, TipoToken.PAR_DER]
