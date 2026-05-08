# Demostraciones — Examen Parcial #2

---

## Problema 1 — Hacer Sencillo

### Subestructura óptima

Las decisiones posibles en este problema son las denominaciones que podemos escoger, es decir, $c \in \{1, 5, 10, 25\}$ con $c \le m$. Cada una de esas decisiones genera el subproblema de hacer sencillo para $m - c$.

Suponga que $S^*$ es la solución óptima para $m$ y que dentro de ella se usó una moneda de denominación $c$. Si removemos esa moneda de $S^*$, lo que queda debe ser solución óptima para $m - c$. Si no lo fuera, existiría alguna solución $S'$ para $m - c$ con menos monedas, y entonces $S' \cup \{c\}$ sería una solución para $m$ con menos monedas que $S^*$, lo cual contradice que $S^*$ era óptima.

Concluimos que la solución óptima del problema completo contiene en su interior la solución óptima de los subproblemas que genera, por lo tanto el problema posee subestructura óptima.

### Subproblemas traslapados

Para resolver el problema en $m$ hace falta resolverlo en $m-1$, $m-5$, $m-10$ y $m-25$. Pero a su vez, varios de esos subproblemas requieren los mismos sub-subproblemas. Por ejemplo, $m-6$ aparece tanto al resolver $m-1$ (restándole 5) como al resolver $m-5$ (restándole 1). Lo mismo pasa con $m-11$, $m-26$, etc.

Esto significa que un árbol de recursión sin memoización terminaría calculando los mismos subproblemas múltiples veces. Como hay solapamiento entre los subproblemas, el problema posee la propiedad de subproblemas traslapados.

### Greedy-choice property

El criterio de decisión es: en cada paso, escoger la moneda de mayor denominación $c^*$ tal que $c^* \le m$.

Para probar que ese óptimo local lleva al óptimo global, suponga lo contrario: que existe una solución óptima $S^*$ para $m$ que **no** usa $c^*$. Entonces $S^*$ solo usa monedas de denominaciones menores que $c^*$. Analizando cada caso:

- Si $c^* = 25$, la única manera de armar 25 sin usar monedas de 25 es con 2 de 10 más una de 5, o con combinaciones más largas de 10s, 5s y 1s. En cualquier caso, una de 25 reemplaza al menos 3 monedas.
- Si $c^* = 10$, la única manera es con 2 de 5 (2 monedas) o combinaciones con 1s. Una de 10 reemplaza 2 o más monedas.
- Si $c^* = 5$, sólo se puede formar con 5 monedas de 1. Una de 5 las reemplaza con ventaja.

En todos los casos, podemos intercambiar monedas de denominaciones menores por una de $c^*$ sin aumentar el total de monedas (en la mayoría de los casos lo reduce). Esto contradice que $S^*$ era óptima si no usaba $c^*$. Por lo tanto siempre existe una solución óptima que incluye la elección greedy.

Como además ya demostramos subestructura óptima, el problema se puede resolver con un acercamiento greedy.

### Matroide ponderada

Definimos la matroide $(S, I)$ así:

- $S = \{(c, k) : c \in \{1, 5, 10, 25\}, \; k \ge 1\}$, donde cada elemento representa una instancia indexada de una moneda. Es decir, podemos tener $(25, 1), (25, 2), (25, 3), \dots$ porque hay infinitas monedas disponibles de cada denominación.
- $I = \{A \subseteq S : \sum_{(c,k) \in A} c \le m\}$, los subconjuntos de monedas cuya suma no excede el monto.
- $w(c, k) = c$ es la función de peso (la denominación de la moneda).

**Herencia.** Si $A \in I$ y $B \subseteq A$, entonces la suma de denominaciones en $B$ es menor o igual que la suma en $A$, que a su vez no excede $m$. Por lo tanto $B \in I$.

**Intercambio.** Si $A, B \in I$ con $|A| < |B|$, entonces queremos mostrar que existe $x \in B \setminus A$ tal que $A \cup \{x\} \in I$. Como $|A| < |B|$ y todas las monedas tienen denominación al menos 1, no puede ser que añadir cualquier moneda de $B$ a $A$ exceda $m$ (si $A$ tiene capacidad sobrante para al menos una moneda más). Si $\text{sum}(A) + 1 \le m$ entonces siempre se puede añadir al menos una moneda de denominación 1 que esté en $B \setminus A$, y por construcción siempre existen monedas de 1 disponibles.

Por lo tanto $(S, I)$ es matroide ponderada.

---

## Problema 2 — Knapsack Fraccionado

### Subestructura óptima

Las decisiones posibles para cada artículo $i$ consisten en elegir una cantidad $x_i$ con $0 \le x_i \le w_i$. Cada elección genera el subproblema de llenar una mochila de capacidad $W - x_i$ con los artículos restantes.

Suponga que $\text{OPT}$ es óptima para capacidad $W$ y artículos $\{1, \dots, n\}$, y que en ella se tomó $x_i$ del artículo $i$. Si removemos esas $x_i$ unidades, lo que queda debe ser óptimo para el subproblema de capacidad $W - x_i$ con los artículos $\{1, \dots, n\} \setminus \{i\}$.

Si no lo fuera, existiría una solución mejor para ese subproblema con valor $V'$ mayor que el de la porción correspondiente en $\text{OPT}$. Combinándola con las $x_i$ unidades ya tomadas obtendríamos una solución para el problema original con valor mayor que $\text{OPT}$, lo cual es una contradicción.

Por lo tanto el problema tiene subestructura óptima.

### Greedy-choice property

El criterio de decisión es: ordenar los artículos por la razón $p_i / w_i$ de mayor a menor, y tomar la mayor cantidad posible del primero (hasta llenar la mochila o agotar el artículo).

Para probar que esto lleva al óptimo, sea el artículo $1$ el de mayor razón $p_1 / w_1$, y suponga que la solución óptima $\text{OPT}$ no toma la cantidad máxima posible de él, es decir, $x_1 < \min(w_1, W)$.

Como queda capacidad disponible y artículo 1 disponible, debe existir alguna fracción $x > 0$ de otro artículo $j$ en $\text{OPT}$ con $p_j / w_j \le p_1 / w_1$. Reemplazamos esas $x$ unidades de $j$ por $x$ unidades de artículo 1. El peso total no cambia. El valor cambia en:

$$\Delta V = x \cdot \frac{p_1}{w_1} - x \cdot \frac{p_j}{w_j} \ge 0$$

porque $p_1/w_1 \ge p_j/w_j$. Es decir, el reemplazo no empeora la solución, lo cual significa que existe una solución óptima que sí incluye la elección greedy.

Como además el problema tiene subestructura óptima, podemos resolverlo greedy.

### Matroide ponderada

Definimos:

- $S = \{(i, u) : i \in \{1, \dots, n\}, \; 0 < u \le w_i\}$ es el conjunto de porciones disponibles de cada artículo.
- $I = \{A \subseteq S : \text{peso total de } A \le W\}$ son las colecciones de porciones que caben en la mochila.
- $w(i, u) = (p_i / w_i) \cdot u$ es la función de peso (el valor que aporta esa porción).

**Herencia.** Si $A \in I$ y $B \subseteq A$, entonces el peso de $B$ no supera el peso de $A$, que a su vez no supera $W$. Por lo tanto $B \in I$.

**Intercambio.** Si $A, B \in I$ con $|A| < |B|$, como $|A| < |B|$ y ambos respetan la capacidad, debe haber elementos en $B \setminus A$ que aún quepan en $A$. Específicamente, como $\text{peso}(A) < \text{peso}(B) \le W$, queda capacidad en $A$ para incorporar al menos un elemento más, y dado que $|B \setminus A| \ge 1$, existe $x \in B \setminus A$ tal que $A \cup \{x\} \in I$.

Por lo tanto $(S, I)$ es una matroide ponderada.

### Por qué NO tiene subproblemas traslapados

A diferencia del problema 1, aquí cada decisión consume capacidad de forma continua y no genera subproblemas idénticos repetidos. Una vez ordenados los artículos por razón valor/peso, el algoritmo procesa cada uno una sola vez sin volver atrás. No hay árbol de recursión con ramas que coincidan.

---

## Problema 3 — Combinaciones en Teclado Nokia

### Modelado

El teclado se modela como una grilla 4×3 donde cada dígito tiene una posición. Los movimientos válidos son arriba, abajo, izquierda y derecha **del teclazo más reciente**, lo que también permite presionar la misma tecla dos veces seguidas (lo confirma el ejemplo del examen, que incluye combinaciones como 00, 11, 22, 33).

Las teclas $*$ y $\#$ están prohibidas, así que los vecinos del 0 son solo el 0 mismo y el 8; los vecinos del 7 son 4, 7 y 8; etc.

### Subestructura óptima

Como el problema no es de optimización sino de **conteo**, la "subestructura óptima" aquí se refiere a que el conteo correcto del problema completo depende del conteo correcto de los subproblemas.

Sea $f(d, k)$ el número de secuencias válidas de longitud $k$ que comienzan con el dígito $d$. Las decisiones posibles para construir tal secuencia son: elegir el siguiente teclazo $v$ entre los vecinos válidos de $d$. Cada una de esas decisiones genera el subproblema $f(v, k-1)$.

La cantidad de secuencias de longitud $k$ que empiezan con $d$ es exactamente la suma de las secuencias de longitud $k-1$ que empiezan en cada uno de los vecinos. Si alguno de los $f(v, k-1)$ se contara incorrectamente, $f(d, k)$ también sería incorrecto. La solución del problema completo está construida sobre las soluciones de los subproblemas, por lo que hay subestructura óptima.

### Subproblemas traslapados

Al calcular $f(d, k)$ para los 10 dígitos simultáneamente, todos requieren $f(v, k-1)$ para sus respectivos vecinos. Pero el grafo de adyacencia tiene muchos vecinos compartidos. Por ejemplo, $f(5, k-1)$ es necesario para calcular $f(2, k)$, $f(4, k)$, $f(5, k)$, $f(6, k)$ y $f(8, k)$, porque el dígito 5 es vecino de cinco dígitos distintos.

Si resolviéramos esto recursivamente sin memoización, $f(5, k-1)$ se recalcularía cinco veces solo en una iteración, y el costo se vuelve exponencial. Con programación dinámica bottom-up calculamos cada $f(d, k)$ una sola vez. Hay solapamiento masivo, por lo tanto subproblemas traslapados.

### Caracterización de la solución óptima y recurrencia

Caracterización: $f(d, k)$ es el número de secuencias válidas de longitud $k$ cuyo primer dígito es $d$.

Caso base: $f(d, 1) = 1$ para todo $d \in \{0, 1, \dots, 9\}$, porque una secuencia de longitud 1 es solamente el dígito en sí.

Recurrencia: $f(d, k) = \displaystyle\sum_{v \in \text{vecinos}(d)} f(v, k-1)$ para $k > 1$.

Solución final: $\text{Total}(n) = \displaystyle\sum_{d=0}^{9} f(d, n)$.

### Por qué NO greedy ni matroide

Como es un problema de conteo, no hay nada que optimizar. No existe una "mejor combinación" que el algoritmo deba escoger localmente, simplemente las cuenta a todas. Por lo tanto greedy-choice property no aplica.

Por la misma razón, no hay función de peso que tenga sentido aquí, y los subconjuntos independientes no se pueden definir naturalmente porque queremos contar todas las secuencias, no escoger una. La estructura no es matroide.
