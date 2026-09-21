"""Las piezas en las que el lexer parte el texto."""

from enum import Enum


class TipoToken(Enum):
    NUMERO = "NUMERO"
    MAS = "MAS"
    MENOS = "MENOS"
    POR = "POR"
    ENTRE = "ENTRE"
    PAR_IZQ = "PAR_IZQ"
    PAR_DER = "PAR_DER"


class Token:
    """Un token sabe que es, que valor tiene y en que posicion del texto estaba.

    La posicion sirve para que los mensajes de error puedan senalar el lugar
    exacto donde algo salio mal.
    """

    def __init__(self, tipo: TipoToken, valor, posicion: int):
        self.tipo = tipo
        self.valor = valor
        self.posicion = posicion

    def __repr__(self):
        return f"Token({self.tipo.name}, {self.valor!r}, {self.posicion})"

    def __eq__(self, otro):
        if not isinstance(otro, Token):
            return NotImplemented
        return (self.tipo == otro.tipo
                and self.valor == otro.valor
                and self.posicion == otro.posicion)
