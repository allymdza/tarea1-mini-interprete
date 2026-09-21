"""Del texto a los tokens.

    "3 + 4 * 2"  ->  [NUMERO(3), MAS, NUMERO(4), POR, NUMERO(2)]
"""

from .tokens import Token, TipoToken

SIMBOLOS = {
    "+": TipoToken.MAS,
    "-": TipoToken.MENOS,
    "*": TipoToken.POR,
    "/": TipoToken.ENTRE,
    "(": TipoToken.PAR_IZQ,
    ")": TipoToken.PAR_DER,
}


def tokenizar(texto: str) -> list:
    """Parte el texto en tokens."""
    tokens = []
    i = 0
    while i < len(texto):
        caracter = texto[i]

        if caracter.isspace():
            i += 1

        elif caracter.isdigit():
            inicio = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            tokens.append(Token(TipoToken.NUMERO, int(texto[inicio:i]), inicio))

        elif caracter in SIMBOLOS:
            tokens.append(Token(SIMBOLOS[caracter], caracter, i))
            i += 1

        else:
            i += 1

    return tokens
