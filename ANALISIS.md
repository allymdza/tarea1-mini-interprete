# Análisis — Tarea 1

**Integrantes:**
1. Campos Mendoza Alondra
2. Guadalupe Balanzar Ruth Sarai

**Fork:**

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Recibe el texto, que en este caso, es la expresión numérica. | Devuelve la tokenización de la expresión en una lista, indicando si es un número o si es un operador | Se encarga justo, de la tokenización, es decir, es nuestro analizador léxico, les da significado a los caracteres para el lenguaje. |
| `parser` | Recibe la lista de tokens que el analizador léxico ya hizo. | Construye un ast de la lista de tokens y lo devuelve. | Se encarga de crear una representación con sentido basándose en las reglas gramáticales que se le den, es el analizador sintáctico. |
| `ast` | Recibe término a término lo de una operación binaria o un número en forma de nodo, nodo que creó el parser. | Devuelve una representación en forma de árbol de la expresión | De darle "forma" al ast, y representar a nuestra expresión en este mismo ast, dándole la jerarquía necesaria. |
| `evaluator` |  Recibe el nodo raíz del ast | Devuelve el resultado de una operación, o bien, el resultado de evaluar todo el ast | Se encarga de verificar que las operaciones tienen sentido, por ejemplo, cacha el caso de cuando intentamos dividir algo entre cero, y sabemos que eso no es posible, entonces lanza un error, y de devolver el resultado al evaluar el ast |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

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
    <td><code>["Token(PAR_IZQ, "(", 0), Token(NUMERO, 3, 1), Token(MAS, "+", 3 ), Token(NUMERO, 4, 5), Token(PAR_DER, ")", 6), Token(POR, "*", 8), Token(NUMERO, 2, 10)"]</code></td>
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

### 2.2 ¿Qué comportamientos **no** estaban probados?
Analizando y viendo las pruebas, hay algunos casos que no están contemplados, los enlistaré enseguida:

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

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| test_evaluator: test_error_division_cero() | "10 / 0" | ErrorDeEvaluacion | Inválida | Se espera que el programa falle y notifique ese error con una excepción |
| test_evaluator: test_error_menos_unario() | "-10 + 2" | ErrorDeSintaxis | Inválida | De acuerdo a las reglas de gramática del programa, no se soportan números negativos. Lo correcto sería escribir "(0 - 10) + 2" |
| test_evaluator: test_resta_numero_consigo_mismo()| "5 - 5" | 0 | Normal | Es una operación básica que el programa debe lograr evaluar |
| test_evaluator: test_division_numero_consigo_mismo() | "100 / 100" | 1 | Normal | Es una operación básica que el programa debe lograr evaluar |
| test_evaluator: test_resta_precedencia_sin_parentesis() | "3 - 3 - 3" | -3 | Frontera | Se espera que el programa realice la operación asociando por la izquierda y no por la derecha, es decir que realice "(3 - 3) - 3" y no "3 - (3 - 3)" |
|test evaluator: test_precedencia_sin_parentesis() | "3 - 3 + 3" | Frontera | Se espera que evalue de izquierda a derecha, dando como resultado 3 |
| test_evaluator: test_multiples_operaciones_y_parentesis_anidados() | "(10 - 5 * 1) + (6 / 2 * (2 + 1 * (10 / 10)))" | 14 | Frontera | Tenemos varios paréntesis anidados y varias operaciones combinadas. Aqui observariamos si la jerarquía de operaciones se respeta correctamente |
| test_evaluator: test_division_resultado_con_decimal() | "5 / 2" | 2.5 | Frontera | Una división real con decimales debe poder ser evaluada correctamente, pues no quisieramos que el programa recorte esos datos adicionales de la división | 
| test_ evaluator: test_numeros() | "007" | 7 | Frontera | Pues se espera que se considere como solo 7, es decir, que los 0's se ignoren.
| test_ evaluator: test_menos_unario() | "(0 - 10) + 2" | -8 | Normal | De acuerdo con las reglas establecidas, no soporta los negativos como los conocemos, como se menciona en la prueba de `test_error_menos_unario`, entonces hicimos la prueba de como se debería de escribir el negativo, dandonos el resultado esperado.
| test_lexer: test_tokeniza_numero_negativo() | "-1" | [Token(TipoToken.MENOS, "-", 0), Token(TipoToken.NUMERO, 1, 1)] | Normal | El lexer debería ser capaz de leer el texto y separarlo en tokens sin ningún problema |
| test_lexer: test_tokeniza_operaciones_basicas_combinadas() | "(4 - 2) / (2 * 1)" | [Token(TipoToken.PAR_IZQ, "(", 0), Token(TipoToken.NUMERO, 4, 1), Token(TipoToken.MENOS, "-", 3), Token(TipoToken.NUMERO, 2, 5), Token(TipoToken.PAR_DER, ")",6), Token(TipoToken.ENTRE, "/", 8), Token(TipoToken.PAR_IZQ, "(",10), Token(TipoToken.NUMERO, 2, 11), Token(TipoToken.POR, "*", 13), Token(TipoToken.NUMERO, 1, 15), Token(TipoToken.PAR_DER, ")", 16] | Normal | Son operaciones básicas con símbolos válidos y su lectura no debería presentar ningún problema |
| test_lexer: test_tokeniza_simbolo_extranio() | " 3 + @" | [Token(TipoToken.NUMERO, 3, 0), Token(TipoToken.MAS, '+', 2)] | Normal | De acuerdo a como está implementado el lexer, este debería ignorar los símbolos extraños y no romperse |
| test_lexer: test_tokeniza_numero_con_espacio_al_inicio() | " 42" | [Token(TipoToken.NUMERO, 42, 1)] | Frontera | El número debería considerarse con una posición distinta si hay un espacio inicial, es decir, "42" y " 42" no deben tener la misma posición |
| test_lexer: test_tokeniza_cadena_vacia() | "" | [] | Frontera | Queremos que el lexer pueda procesar correctamente una cadena vacía sin llegar a ciclarse o considerarlo como un error |
| test_parser: test_construye_arbol_de_una_resta() | "5 - 2" | OperacionBinaria("-", Numero(5), Numero(2)) | Normal | Verificamos la construcción de una operación básica |
| test_parser: test_construye_arbol_de_una_multiplicacion() | "4 * 3" | OperacionBinaria("*", Numero(4), Numero(3)) | Normal | Verificamos la construcción de una operación básica |
| test_parser: test_construye_arbol_de_una_division() | " 8 / 2 | OperacionBinaria("/", Numero(8), Numero(2)) | Normal | Verificamos la construcción de una operación básica |
| test_parser: test_error_construye_arbol_de_cadena_vacia() | "" | ErrorDeSintaxis | Inválida | El parser no debería poder construir la raíz del árbol de sintaxis al no recibir ningún token |
| test_parser: test_error_falta_parentesis_de_cierre() | "(3 + 4" | ErrorDeSintaxis |  Inválida | Se incumple la regla de tener un token de tipo PAR_DER de cierre para un token de tipo PAR_IZQ |
| test_parser: test_error_operadores_consecutivos() | "3 ++ 4" | ErrorDeSintaxis | Inválida | El parser tiene que esperar un token de tipo NUMERO o PAR_IZQ después de un operador unario, pues es lo que exige la gramática | 

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?
  * No manejaba como interpretar una expresión vacía.
  * Asocia mal cuando tenemos la misma operación en la expresíon.
  * Arrojaba IndexError cuando faltaba el paréntesis de cierre en una expresión que terminaba sin ese parentésis, cuando debía de lanzar un ErrorDeSintaxis.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?
  * Porque en el archivo `parser.py`, en la función `parsear()` no se manejaba el error en dónde tenemos una expresión vacía, pues si está vacía, no hay árbol. Va contra la regla 8 de la semántica, "entrada inválida".
  * Debe de evaluar las operaciones de izquierda a derecha, y las evalua al revés, es decir, de derecha a izquierda. Va contra la regla 6 de la semántica, "asociatividad".
  * Porque una expresión que termina sin cerrar el paréntesis está mal, pues nos quedamos esperando como algo más, o que el paréntesis se cierre, y como tal, debe de ser un error de sintaxis, pues está mal escrito, no un error de índice, pues no estamos tocandolos en esta parte. Va contra la regla 8 de la semántica, "entrada inválida".

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| No valida una expresión vacia | "" | Saltaba un error de tipo IndexError, aqui el parser no sabía manejarlo | Debería de dar ErrorDeSintaxis| 635e14c | bed184e |
| Asocia mal | "3 - 3 - 3" y "3 - 3 + 3"| Para el primer caso, daba 3, y para el segundo caso, daba -3 | Debería de dar, para el primer caso -3, y para el segundo caso, 3 | da380fa | 082ed9d |
| Lanza un IndexError cuando no está el parentesis de cierre | "(3 + 4" | Saltaba un error de IndexError | Debería de saltar un error de ErrorDeSintaxis | 635e14c | bed184e | 

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?
Porque las correcciones se hicieron para casos generales, no solo para esos casos particulares, pues se modificó el código, es decir, desde "raíz" y por eso, por ejemplo, se añadió la prueba de "3 - 3 + 3", pues ambos operadores tienen la misma precedencia, entonces lo que hicimos en el código, no fue únicamente para un caso particular.

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

- Lo primero que encontramos fue **rigidez estructural** en la implementación del parser. Esto porque el diseño tenía un comportamiento que iba contra la regla de asociar a la izquierda operadores de la misma precedencia. Lo que ocurría era que el parser estaba diseñado de tal forma que utilizaba llamadas recursivas que rompían esta regla básica y al querer corregir este error se volvía más tedioso buscar la falla dentro de llamadas a las funciones que se hacían. Por lo que corregir la función no bastaba con cambiar una variable o parámetro o condición, se necesitó rediseñar el algoritmo que implementaba el parser (Para corregir la asociatividad utilizamos un while en lugar de utilizar la recursividad original).


- Otro mal diseño que encontramos fue también en el parser. Además de la **rigidez** ya mencionada, encontramos nuevamente esta situación en el método _avanzar(), que a su vez propiciaba a una **amplificación del cambio** pues el error que se encontró es que este método no verificaba correctamente si aún había algún token por leer y como consecuencia se rompía ante entradas vacías o paréntesis que no fueron cerrados; al no verificarse correctamente esta situación, saltaba un IndexError de Python que se propagaba a las demás funciones: _expresion(), _termino(), _factor(), y no nos permitía dar un error controlado (en este caso ErrorDeSintaxis).


### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

- Para arreglar la parte de la asociatividad a la izquierda se hizo lo siguiente:
Reemplazamos la recursividad rígida por un bloque `while` en la función `_expresion()` y `_termino()`. Al implementar este bucle pudimos acumular los operandos de izquierda a derecha (esto se ve representado en el código como `izquierda = OperacionBinaria(operador.valor, izquierda, derecha)`). Con ese arreglo el parser ya respeta la regla gramatical de asociatividad a la izquierda con operadores de la misma precedencia y además no se alteró al resto del programa.


- La segunda parte que fue arreglar la validación para la función `_avanzar()`: 
Rediseñamos esta función agregando las validaciones para los datos de entrada y consumo. La condicional`if not self.tokens` en la función `_parsear()` revisa si la lista de tokens está vacía (en este caso, si es vacía frena la ejecución y lanza el error), y la condicional `if self.pos >= len(self.tokens)` en la función `_avanzar()` vigila que en cada consumo o avance de posición no se rebase el tamaño total de la lista (nos ayudaría a detectar si una expresión está incompleta como en el caso de que un paréntesis no se cierre). Ambas correcciones ahora nos permiten ahora lanzar un `ErrorDeSintaxis` controlado para los casos en que necesitamos ver el error.


Estas refactorizaciones conservan el comportamiento. En primer lugar, el cambio realizado con el bucle `while` sigue construyendo los nodos para el AST con la función OperaciónBinaria, pero con la correción de la asociatividad que se exigen en las reglas de gramática y no altera el resultado de las operaciones. 
Lo segundo, el agregar las validaciones para los límites al momento de que se consumen los tokens solo verifica y controla los casos de errores evitando que ocurran desbordamientos que respondan con un error de Python. Esto no altera el flujo de ejecución del programa, se queda igual que antes pero ahora hacemos que el programa pueda lanzar un error de tipo `ErrorDeSintaxis` que se exige como un comportamiento más.


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
