"""Errores propios del interprete.

Tener errores propios (y no dejar escapar los de Python) es lo que permite
que una prueba diga "esta entrada DEBE ser rechazada" en vez de "esta entrada
truena de alguna manera".
"""


class ErrorDelInterprete(Exception):
    """Error base. Todo lo que el interprete reporta hereda de aqui."""


class ErrorDeSintaxis(ErrorDelInterprete):
    """La entrada no forma una expresion valida."""

    def __init__(self, mensaje: str, posicion: int):
        self.mensaje = mensaje
        self.posicion = posicion
        super().__init__(f"{mensaje} (posicion {posicion})")


class ErrorDeEvaluacion(ErrorDelInterprete):
    """La expresion es valida pero no se puede evaluar."""
