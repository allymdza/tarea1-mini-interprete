# Análisis — Tarea 1

**Integrantes:**
1. Campos Mendoza Alondra
2.
3.

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Recibe el texto, que en este caso, es la expresión numérica. | Devuelve la tokenización de la expresión en una lista, indicando si es un número o si es un operador | Se encarga justo, de la tokenización, es decir, es nuestro analizador léxico, les da significado a los caracteres para el lenguaje. |
| `parser` | Recibe la lista de tokens que el analizador léxico ya hizo. | Construye un ast de la lista de tokens y lo devuelve. | Se encarga de crear una representación con sentido basándose en las reglas gramáticales que se le den, es el analizador sintáctico. |
| `ast` | Recibe término a término lo de una operación binaria o un número en forma de nodo, nodo que creó el parser. | Devuelve una representación en forma de árbol de la expresión | De darle "forma" al ast, y representar a nuestra expresión en este mismo ast, dándole la jerarquía necesaria. |
| `evaluator` |  Recibe el nodo raíz del ast | Devuelve el resultado de una operación, o bien, el resultado de evaluar todo el ast | Se encarga de veriicar que las operaciones tienen sentido, por ejemplo, cacha el caso de cuando intentamos dividir algo entre cero, y sabemos que eso no es posible, entonces lanza un error, y de devolver el resultado al evaluar el ast |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

<table>
  <tr>
    <th>Etapa</th>
    <th>Cómo se ve <code>(3 + 4) * 2</code> aquí</th>
  </tr>
  <tr>
    <td>texto</td>
    <td><code>"(3 + 4) * 2"</code></td>
  </tr>
  <tr>
    <td>tokens</td>
    <td><code>["Token(PAR_IZQ, (, 0), Token(NUMERO, 3, 1), Token(MAS, +, 3 ), Token(NUMERO, 4, 5), Token(PAR_DER, ), 6), Token(POR, *, 8), Token(NUMERO, 2, 10)"]</code></td>
  </tr>
  <tr>
    <td>AST</td>
    <td>
      <pre>        *
       / \
      +   2
     / \
    3   4</pre>
    </td>
  </tr>
  <tr>
    <td>resultado</td>
    <td><code>14</code></td>
  </tr>
</table>

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
|`test_suma`|evaluator|sume correctamente|uno, +|normal|
|`test_resta`|evaluator|reste correctamente|uno, -|normal|
|`test_multiplicacion`|evaluator|multiplique correctamente|uno, *|normal|
|`test_division`|evaluator|divida correctamente|uno, /|normal|
|`test_precendencia_sin_parentesis`|evaluator|que tome en cuenta un orden jerarquico, es decir, que ejecute las operaciones como toda la vida lo hemos hecho, y como no tiene parentésis, entonces se sigue el orden convencional|dos: +,*|normal|
|`test_precedencia_con_parentesis`|evaluator|que primero realice las operaciones que se muestran dentro de los paréntesis y después realice las demás|tres, (), +, *|normal|
|`test_tokeniza_un_numero_solo`|lexer|que tokenice los números como se supone que debe de hacerlo: tipo de token, que token es, que posición tiene|ninguno, pero si tomamos como operador a las funciones que llama, entonces una, que sería `tokenizar`|normal|
|`test_tokeniza_una_suma`|lexer|que convierta la suma correctamente a tokens|el de la suma, pero también llama a la función tokenizar|normal|
|`test_los_espacios_no_producen_tokens`|lexer|que el tamaño de la expresion sea el que ocupan los operadores y numeros, y esto se hace calculando el tamaño de la expresión, si coincide con el número de operadores  y operandos, entonces lo tokeniza los espacios|uno, la suma, pero nuevamente, llama la funcion `tokenizar`|normal|
|`test_tokeniza_parentesis`|lexer|que tokenice debidamente los paréntesis con un número dentro de ellos|ninguno, pero llama a `tokenizar`|normal|
|`test_construye_el_arbol_de_una_suma`|parser|que la suma esté bien hecha dentro de un arbol binario|uno, la suma, pero manda a llamar a operacion binaria de ast|normal|
|`test_la_multiplicacion_se_agrupa_antes_que_la_suma`|parser|que exista la jerarquía en el arbol, es decir que si no hay parentésis, aplicamos la jerarquia que ya sabemos|dos, + y *, y llama a a funcion operacion binaria|normal|
|`test_los_parentesis_cambian_la_agrupacion`|parser|qu primero se muestren las operaciones que están dentro del paréntesis y aparezca esa agrupacion en el arbol|tres, (),+,* y manda a llamar a operacion binaria|normal|

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?
Analizando y viendo las pruebas, hay algunos casos que no están contemplados, los enlisaré enseguida:

- En el archivo `test_evaluator` encontré algunos casos, como estos:
  1. Falta ver qué sucede cuando queremos dividir entre 0.
  2. ¿Qué sucede cuando tenemos algo del estilo `-10 + 2`?
  3. ¿Qué pasa cuando resto un número consigo mismo?
  4. ¿Qué pasa si divido un número entre sí mismo?
  5. ¿Y si tengo algo como num - num - num? ¿Cómo lo evaluo?

- En el archivo `test_lexer` encontré otros, como estos:
  1. ¿Cómo se tokeniza un número negativo?
  2. ¿Qué posición debe tener si hay espacios? Por ejemplo:
     - El número `" 42"`.
     - El número `"42  "`.
  3. Falta ver la tokenización de la multiplicación, la división, la resta y los paréntesis con una operación dentro.
  4. ¿Qué pasa si tokenizo una operación con espacios en blanco?
  5. Si los espacios no generan tokens, ¿qué sucede si introduzco una cadena vacía o solo un número negativo?
  6. ¿Qué pasa si tengo algún símbolo como @?

- En el archivo `test_parser` encontré estos casos:
  1. Falta ver el árbol de las demás operaciones.
  2. Falta ver el árbol de una expresión vacía.
  3. ¿Que pasa si no cierro un paréntesis?
  4. ¿Qué pasa si tengo algo como ++?


> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| | | | | |

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| | | | | | |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
