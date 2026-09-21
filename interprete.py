"""Punto de entrada desde la raiz del repositorio.

    python3 interprete.py "3 + 4 * 2"
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))

from mini_interprete.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
