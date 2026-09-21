"""Del AST a un numero.

Recorre el arbol de abajo hacia arriba: para evaluar una operacion hay que
evaluar primero sus dos lados.
"""

from .ast import Numero, OperacionBinaria
from .errores import ErrorDeEvaluacion


def evaluar(nodo):
    """Evalua un nodo del AST y regresa su valor."""
    if isinstance(nodo, Numero):
        return nodo.valor

    if isinstance(nodo, OperacionBinaria):
        izquierda = evaluar(nodo.izquierda)
        derecha = evaluar(nodo.derecha)

        if nodo.operador == "+":
            return izquierda + derecha
        if nodo.operador == "-":
            return izquierda - derecha
        if nodo.operador == "*":
            return izquierda * derecha
        if nodo.operador == "/":
            if derecha == 0:
                raise ErrorDeEvaluacion("division entre cero")
            return izquierda / derecha

        raise ErrorDeEvaluacion(f"operador desconocido: {nodo.operador!r}")

    raise ErrorDeEvaluacion(f"nodo desconocido: {nodo!r}")
