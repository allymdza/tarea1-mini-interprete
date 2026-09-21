"""De los tokens al AST.

La gramatica que reconoce este parser es:

    expresion := termino  (('+' | '-') termino)*
    termino   := factor   (('*' | '/') factor)*
    factor    := NUMERO | '(' expresion ')'

Los tres niveles son lo que hace que  3 + 4 * 2  se agrupe como  3 + (4 * 2)
y no como  (3 + 4) * 2 : la multiplicacion vive un nivel mas abajo, asi que
se arma primero.
"""

from .ast import Numero, OperacionBinaria
from .errores import ErrorDeSintaxis
from .tokens import TipoToken

OPERADORES_SUMA = (TipoToken.MAS, TipoToken.MENOS)
OPERADORES_PRODUCTO = (TipoToken.POR, TipoToken.ENTRE)


class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def parsear(self):
        """Construye el AST de la lista de tokens."""
        return self._expresion()

    def _actual(self):
        """El token en la posicion actual, o None si ya no quedan."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _avanzar(self):
        """Consume el token actual y lo regresa."""
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def _expresion(self):
        izquierda = self._termino()
        actual = self._actual()
        if actual is not None and actual.tipo in OPERADORES_SUMA:
            operador = self._avanzar()
            derecha = self._expresion()
            return OperacionBinaria(operador.valor, izquierda, derecha)
        return izquierda

    def _termino(self):
        izquierda = self._factor()
        actual = self._actual()
        if actual is not None and actual.tipo in OPERADORES_PRODUCTO:
            operador = self._avanzar()
            derecha = self._termino()
            return OperacionBinaria(operador.valor, izquierda, derecha)
        return izquierda

    def _factor(self):
        token = self._avanzar()

        if token.tipo == TipoToken.NUMERO:
            return Numero(token.valor)

        if token.tipo == TipoToken.PAR_IZQ:
            nodo = self._expresion()
            cierre = self._avanzar()
            if cierre.tipo != TipoToken.PAR_DER:
                raise ErrorDeSintaxis("se esperaba ')'", cierre.posicion)
            return nodo

        raise ErrorDeSintaxis(f"token inesperado {token.valor!r}", token.posicion)
