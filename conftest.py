"""Deja que las pruebas importen el paquete sin instalar nada.

Gracias a esto pueden escribir  from mini_interprete.lexer import tokenizar
en cualquier prueba. No necesitan modificar este archivo.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))
