"""Pruebas del lexer: del texto a los tokens."""

from mini_interprete.lexer import tokenizar
from mini_interprete.tokens import Token, TipoToken


def test_tokeniza_un_numero_solo():
    assert tokenizar("42") == [Token(TipoToken.NUMERO, 42, 0)]

#falta ver num negativos y cuando el numero tenga un espacio, 
# que posicion tendra ese token si tiene el espacio? 


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