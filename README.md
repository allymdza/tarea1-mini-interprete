# Tarea 1 — Mini intérprete de expresiones

Modelado y Programación (1323) · Grupo 7077 · Semestre 2027-1

| | |
|---|---|
| **Se publica** | lunes 21 de septiembre de 2026 |
| **Se entrega** | **lunes 19 de octubre de 2026** |
| **Equipos** | de 3 personas |

## 1. De qué se trata

Este repositorio contiene un intérprete de expresiones aritméticas **que ya
funciona**. No van a construirlo: van a **entrar a un proyecto existente**,
entenderlo, probarlo, encontrarle lo que le falta y mejorarlo sin romperlo.

Es lo que pasa cuando uno llega a un equipo: el código ya estaba ahí, lo
escribió alguien más, y hay que moverlo sin tirar nada.

El flujo que implementa es el que vimos en clase el 25 de agosto:

```
texto  →  lexer  →  tokens  →  parser  →  AST  →  evaluator  →  número
```

```
"3 + 4 * 2"  →  [NUMERO(3), MAS, NUMERO(4), POR, NUMERO(2)]  →  AST  →  11
```

> El código de este repositorio pasa todas sus pruebas.
> Eso no significa que sea correcto.

## 2. Clonar

Primero hagan **fork** de este repositorio a la cuenta de uno de los
integrantes (botón *Fork*, arriba a la derecha). Después:

```bash
git clone https://github.com/<su-usuario>/tarea1-mini-interprete.git
cd tarea1-mini-interprete
```

Agreguen a los demás integrantes como colaboradores del fork:
*Settings → Collaborators*.

## 3. Ambiente virtual

**Linux y macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
py -m venv venv
venv\Scripts\Activate.ps1
```

Si PowerShell se queja de la política de ejecución:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

Sabrán que funcionó porque el prompt empieza con `(venv)`.

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 5. Ejecutar el intérprete

```bash
python3 interprete.py "3 + 4 * 2"
python3 interprete.py "(3 + 4) * 2"
python3 interprete.py                 # modo interactivo, Ctrl-D para salir
```

### Ver el árbol

```bash
python3 interprete.py --arbol "3 + 4 * 2"
```

```
+
|-- 3
`-- *
    |-- 4
    `-- 2
```

Ese dibujo es el AST: muestra **cómo quedó agrupada** la expresión. Aquí se
lee que la multiplicación quedó adentro, o sea `3 + (4 * 2)`.

Úsenlo cada vez que un resultado no cuadre. Cuando una operación da un número
distinto al que esperaban, casi siempre es porque el árbol no tiene la forma
que ustedes creían — y así lo ven en vez de suponerlo. Es la misma idea del
`imprimirPorNiveles()` de la Práctica 3.

## 6. Ejecutar las pruebas

```bash
pytest                 # todo
pytest -v              # con el nombre de cada prueba
pytest tests/test_lexer.py
pytest -k "suma"       # sólo las que tengan "suma" en el nombre
pytest -x              # detenerse en la primera que falle
```

Las 13 pruebas incluidas pasan. Compruébenlo antes de tocar nada.

### Cómo se escribe una prueba

Una prueba es una función que empieza con `test_` y usa `assert`. Los tres
pasos de clase — **preparar, ejecutar, comprobar**:

```python
def test_la_suma_de_dos_numeros():
    entrada = "3 + 4"              # preparar
    resultado = interpretar(entrada)   # ejecutar
    assert resultado == 7          # comprobar
```

A veces no hay nada que preparar, y está bien: `assert interpretar("3 + 4") == 7`
es una prueba completa.

**Para verificar que algo DEBE fallar** se usa `pytest.raises`. La prueba pasa
si —y sólo si— se lanza ese error:

```python
import pytest

def test_algo_que_debe_fallar():
    with pytest.raises(ZeroDivisionError):
        10 / 0
```

Los errores del intérprete están en `src/mini_interprete/errores.py`:
`ErrorDeSintaxis` y `ErrorDeEvaluacion`. Sean específicos: atrapar
`Exception` a secas no verifica casi nada, porque cualquier falla la cumple.

Los archivos en `tests/` son sus propios ejemplos: ábranlos antes de escribir
la primera.

## 7. Semántica declarada

Estas decisiones **ya están tomadas**. No son opinables, y las pruebas que
escriban deben respetarlas.

| | |
|---|---|
| Números | enteros, sin signo. `007` es `7` |
| División | **real**: `10 / 4` es `2.5`, y `10 / 2` es `5.0` |
| División entre cero | debe reportarse como `ErrorDeEvaluacion` |
| Menos unario | **no se soporta**. `-3` es inválido; escriban `(0 - 3)` |
| Precedencia | `*` y `/` antes que `+` y `-`; los paréntesis mandan |
| Asociatividad | los operadores de la misma precedencia se asocian **a la izquierda** |
| Espacios | se ignoran en cualquier cantidad |
| Entrada inválida | debe rechazarse con `ErrorDeSintaxis`, nunca con un error de Python |
| Mensajes de error | deben indicar la posición dentro del texto |

## 8. Qué tienen que hacer

1. Crear y activar el ambiente virtual, instalar dependencias.
2. Ejecutar el programa y las pruebas iniciales.
3. Explicar brevemente la responsabilidad de `lexer`, `parser`, `ast` y `evaluator`.
4. Clasificar las pruebas iniciales según el componente y el comportamiento que verifican.
5. **Identificar comportamientos importantes que no están probados.**
6. Proponer e implementar:
   - al menos **dos casos normales** adicionales;
   - al menos **tres casos frontera**;
   - al menos **dos entradas inválidas**.
7. Lograr que **al menos una prueba nueva revele un defecto** del código original.
8. Corregir los defectos encontrados **sin romper las pruebas anteriores**.
9. Identificar al menos **dos señales de mal diseño** o de mantenibilidad.
10. **Refactorizar al menos una** de ellas, conservando el comportamiento.
11. Responder si **Factory Method, Adapter o ninguno** es pertinente para alguna
    parte del sistema, y justificarlo.
12. Contestar `ANALISIS.md`.
13. Llenar `DECLARACION_IA.md`. Es obligatorio aunque **no** hayan usado IA:
    en ese caso marcan la casilla, firman, y listo.

> Sobre el punto 11: **"ninguno" es una respuesta válida y puede ser la
> correcta.** No metan un patrón para demostrar que se lo saben. Se evalúa el
> criterio, no la cantidad de clases. Un patrón que no mejora nada, resta.

### Una petición sobre el orden

Usar IA o no es decisión de cada quien. Pero **les pedimos, por favor, que
primero intenten el análisis por su cuenta** y después, si quieren, usen IA
para contrastar: qué encontró que ustedes no vieron, y sobre todo **qué no
encontró que en este curso sí consideramos un problema** — por ejemplo la
duplicación, que una herramienta rara vez señala porque el programa funciona
igual.

Si preguntan primero, se pierden lo segundo: no se puede notar lo que a una
herramienta le faltó sin haberse formado una opinión propia antes. El detalle
está en `ANALISIS.md`, y la declaración se llena en `DECLARACION_IA.md`.

## 9. Flujo de Git

```bash
git switch -c tarea1-pruebas-refactorizacion

# ... trabajan, con commits pequeños ...
git add tests/test_evaluator.py
git commit -m "Agrega prueba de resta encadenada (falla)"
git push -u origin tarea1-pruebas-refactorizacion
```

Después abran un **Pull Request** de su rama hacia `main` **de su propio
fork**, titulado `Tarea 1 — Apellido1, Apellido2, Apellido3`.

Antes de hacer el merge: **revisen el diff completo**. Es parte de la tarea,
y es lo que van a hacer el resto de su vida profesional.

Al terminar, manden el enlace de su fork por el medio acordado en clase.

**Dos reglas:**

- Commits pequeños y descriptivos. `git log --oneline` debe contar el proceso.
  Un solo commit llamado `tarea` vale cero en ese rubro.
- El historial tiene que mostrar commits **de los tres integrantes**
  (`git shortlog -sn`). Si sólo aparece una persona, se califica como si sólo
  una persona hubiera entregado.

## 10. Integración continua

Cada `push` dispara las pruebas automáticamente (pestaña **Actions**).

La primera vez que entren a Actions en su fork, GitHub les va a pedir que
confirmen con un botón que quieren habilitar los workflows. Háganlo el primer
día: es un clic, y a partir de ahí cada push les dice solo si algo se rompió.

**La entrega final debe tener el pipeline en verde.**

## 11. Qué se entrega

A más tardar el **lunes 19 de octubre**:

| | |
|---|---|
| El fork | con la rama fusionada a `main` y el pipeline en verde |
| `ANALISIS.md` | contestado |
| `DECLARACION_IA.md` | llenado, incluso si no usaron IA |
| El historial | commits pequeños, descriptivos, de los tres integrantes |
| El Pull Request | con el diff revisado antes del merge |
