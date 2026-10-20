# Declaración de uso de Inteligencia Artificial

**Actividad: Tarea 1**

**Integrantes:**
**1. Campos Mendoza Alondra**
**2. Guadalupe Balanzar Ruth Saraí**

**Fecha: 19 de octubre del 2026**

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [✔] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| Gemini | |


---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
|Para acomodar bien una tabla que se desfazaba del formato | En el archivo README, para la primera tabla |
| Para analizar porqué una prueba fallaba | En el archivo de test_parser.py |

---

## 3. Prompts principales


```
(prompt 1)
y si ahora quiero que esto se vea de que lindo, y no asi? (y le adjunte una captura de como se veía la tabla)
```

```
(prompt 2)
Realicé una prueba unitaria para que ver que el parser soporte cadenas vacías, mi prueba falló pero no logró entender bien por qué. Explicame el flujo que se hace cuando doy una cadena vacía como entrada. [Aquí le subí el código de parser.py y también le pasé una screenshot de la prueba que hice] 
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
|Produjo el código de la tabla 1.2 (no lo coloqué porque está muy extenso)|Aceptado y modificado|Aceptado porque se ve bien, modificado porque tuve que rellenar todo el apartado de tokens, pues no lo colocó la IA.|ANALISIS.md/|
| Me explicó cual era el flujo de ejecución de por qué fallaba la prueba, un pequeño resumen: "Cuando le pasas una cadena vacía "", el lexer regresa correctamente una lista vacía de tokens []. El parser recibe esa lista vacía e intenta parsearla llamando a _expresion() -> _termino() -> _factor() -> _avanzar(). Dentro de _avanzar(), el código intenta leer el token actual haciendo self.tokens[self.pos] sin verificar si la posición ya rebasó el tamaño de la lista. Como la lista está vacía ([]), salta un IndexError: list index out of range de Python en lugar de lanzar el controlado ErrorDeSintaxis que tú estabas esperando con pytest.raises(ErrorDeSintaxis)."| Aceptado pero no modifqué nada ya que solo buscaba razonar el fallo de dicha prueba. | Luego de la explicación que obtuve, pude ver con mayor claridad donde debía manejarse de forma diferente la implementación del parser. Y la prueba la marqué con .xfail para que se supiera que fallaba. | ninguno |


### 4.1 Si la usaron para el análisis: el contraste

No aplica.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?
Prompt 1. Porque hay un comando en VSCode (ctrl k + v) para ver como luce el .md mientras trabajas en él, y vi que la tabla ya parecía tabla, entonces está correcto.

Prompt 2. Al volver a analizar el código que tenía que no me era tan intuitivo de analizar para el caso que quería entender, pude seguir mejor el flujo de ejecución y me di cuenta que efectivamente si era eso el problema/fallo que había en la implementación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?
En cuánto al uso de IA, ninguna de las integrantes tuvo problemas para la ayuda o retroalimentación que se pidió.
### 5.2 ¿Qué harían distinto la próxima vez?

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
|Campos Mendoza Alondra|323143363|
| Guadalupe Balanzar Ruth Sarai | 426008031
