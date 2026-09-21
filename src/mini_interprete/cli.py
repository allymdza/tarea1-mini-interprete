"""Linea de comandos del interprete.

    python3 interprete.py "3 + 4 * 2"
    python3 interprete.py --arbol "3 + 4 * 2"
    python3 interprete.py                     (interactivo, Ctrl-D para salir)
"""

import sys

from .ast import Numero
from .errores import ErrorDelInterprete
from .evaluator import evaluar
from .lexer import tokenizar
from .parser import Parser


def interpretar(texto: str):
    """texto -> tokens -> AST -> valor. El recorrido completo, en una linea."""
    return evaluar(Parser(tokenizar(texto)).parsear())


def formatear_arbol(nodo, prefijo: str = "", rama: str = "") -> list:
    """Dibuja el AST como un arbol de texto.

    Sirve para VER como quedo agrupada una expresion, en vez de suponerlo.
    Es la misma idea que el imprimirPorNiveles() de la Practica 3: cuando algo
    no cuadra, lo primero es mirar la estructura.
    """
    if isinstance(nodo, Numero):
        return [prefijo + rama + str(nodo.valor)]

    lineas = [prefijo + rama + nodo.operador]
    if rama == "":
        prefijo_hijos = prefijo
    elif rama.startswith("`"):
        prefijo_hijos = prefijo + "    "
    else:
        prefijo_hijos = prefijo + "|   "

    lineas += formatear_arbol(nodo.izquierda, prefijo_hijos, "|-- ")
    lineas += formatear_arbol(nodo.derecha, prefijo_hijos, "`-- ")
    return lineas


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    mostrar_arbol = "--arbol" in argv
    argv = [a for a in argv if a != "--arbol"]

    if argv:
        return _una_expresion(" ".join(argv), mostrar_arbol)

    for linea in sys.stdin:
        linea = linea.strip()
        if linea:
            _una_expresion(linea, mostrar_arbol)
    return 0


def _una_expresion(texto: str, mostrar_arbol: bool = False) -> int:
    try:
        if mostrar_arbol:
            arbol = Parser(tokenizar(texto)).parsear()
            print("\n".join(formatear_arbol(arbol)))
            return 0
        print(interpretar(texto))
        return 0
    except ErrorDelInterprete as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
