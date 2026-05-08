"""
Problema 3: Combinaciones en Teclado Nokia 3230
=================================================
Universidad del Valle de Guatemala - Analisis y Diseno de Algoritmos
Examen Parcial #2

Paradigma: PROGRAMACION DINAMICA (bottom-up)

Estado: dp[d] = numero de secuencias validas de longitud k que comienzan con d
Recurrencia: dp_nuevo[d] = sum(dp[v] para v en vecinos[d])
Caso base: dp[d] = 1 para todo d en {0, 1, ..., 9}
Respuesta: Total(n) = sum(dp[d]) para todo d

Por que NO greedy: es un problema de conteo, no de optimizacion.
Por que NO matroide: no hay funcion de peso ni maximizacion/minimizacion.

Teclado del Nokia 3230 (4 filas x 3 columnas):
    [ 1  2  3 ]
    [ 4  5  6 ]
    [ 7  8  9 ]
    [ *  0  # ]   <- * y # NO se pueden presionar

Movimientos validos: arriba, abajo, izquierda, derecha
ADEMAS, presionar la misma tecla (lo confirma el ejemplo del examen: 00, 11, 22)
"""

# Vecinos validos para cada digito (incluye al propio digito)
VECINOS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [1, 2, 3, 5],
    3: [2, 3, 6],
    4: [1, 4, 5, 7],
    5: [2, 4, 5, 6, 8],
    6: [3, 5, 6, 9],
    7: [4, 7, 8],
    8: [0, 5, 7, 8, 9],
    9: [6, 8, 9]
}


def contar_combinaciones(n, mostrar_tabla=False):
    """
    Cuenta el numero de combinaciones validas de longitud n.

    Args:
        n: longitud de la combinacion (entero positivo)
        mostrar_tabla: si es True, imprime la tabla DP en cada iteracion

    Returns:
        (total, dp_final) donde total es la suma y dp_final el dict por digito
    """
    if n <= 0:
        return 0, {}

    # Caso base: longitud 1, cada digito vale 1 combinacion (el digito solo)
    dp = {d: 1 for d in range(10)}

    if mostrar_tabla:
        print("  Tabla DP:")
        print(f"  {'k=1':>5} | " + " ".join(f"{dp[d]:>4}" for d in range(10)) +
              f"  total={sum(dp.values())}")

    # Construccion bottom-up: longitud k a partir de longitud k-1
    for k in range(2, n + 1):
        dp_nuevo = {d: 0 for d in range(10)}
        for d in range(10):
            for v in VECINOS[d]:
                dp_nuevo[d] += dp[v]
        dp = dp_nuevo

        if mostrar_tabla:
            print(f"  {'k='+str(k):>5} | " +
                  " ".join(f"{dp[d]:>4}" for d in range(10)) +
                  f"  total={sum(dp.values())}")

    total = sum(dp.values())
    return total, dp


def ejecutar_caso(n, mostrar_tabla=True):
    """Ejecuta un caso de prueba con narracion paso a paso."""
    print("=" * 70)
    print(f"  CASO: n = {n}")
    print("=" * 70)
    if mostrar_tabla:
        print(f"  Encabezado: digitos del 0 al 9")
        print(f"          | " +
              " ".join(f"{d:>4}" for d in range(10)))
        print(f"  {'-' * 60}")
    total, dp = contar_combinaciones(n, mostrar_tabla=mostrar_tabla)
    print(f"\n  RESULTADO: para n={n} hay {total} combinaciones validas.\n")


def listar_combinaciones_pequeno(n, max_mostrar=40):
    """Genera la lista completa de combinaciones (solo para n pequeno).
    Sirve para verificacion contra el algoritmo DP."""
    combos = []

    def dfs(actual, restante):
        if restante == 0:
            combos.append("".join(str(d) for d in actual))
            return
        ultimo = actual[-1]
        for v in VECINOS[ultimo]:
            actual.append(v)
            dfs(actual, restante - 1)
            actual.pop()

    for d in range(10):
        dfs([d], n - 1)

    combos.sort()
    return combos


if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("  PROBLEMA 3: COMBINACIONES NOKIA (Programacion Dinamica)")
    print("#" * 70 + "\n")

    # Mostrar la estructura de vecinos
    print("Tabla de vecinos validos por digito:")
    for d in range(10):
        print(f"  {d} -> {VECINOS[d]}")
    print()

    # CASO 1: ejemplo del examen
    ejecutar_caso(2)
    # Verificar contra fuerza bruta
    combos = listar_combinaciones_pequeno(2)
    print(f"  Verificacion con fuerza bruta para n=2: {len(combos)} combos")
    print(f"  Lista completa: {combos}\n")

    # CASO 2: n = 4
    ejecutar_caso(4)

    # CASO 3: n = 10 (no se puede hacer fuerza bruta razonablemente)
    ejecutar_caso(10)
