"""
Problema 2: Knapsack Fraccionado (Fractional Knapsack)
========================================================
Universidad del Valle de Guatemala - Análisis y Diseño de Algoritmos
Examen Parcial #2

Paradigma: GREEDY
Estrategia: ordenar los artículos por la razón valor/peso (p_i / w_i)
            de mayor a menor, y tomar la mayor fracción posible de cada uno
            hasta llenar la mochila.

Por qué greedy funciona aquí:
- Greedy-choice property: siempre conviene tomar el artículo con mayor p/w
- Subestructura óptima: la solución sin un artículo es óptima para
  el subproblema con menor capacidad
- Matroide ponderada con función de peso w(i, u) = (p_i/w_i) * u
"""


def knapsack_fraccionado(articulos, W, mostrar_pasos=False):
    """
    Resuelve el knapsack fraccionado con algoritmo greedy.

    Args:
        articulos: lista de tuplas (precio, peso_disponible, nombre)
        W: capacidad de la mochila (entero o float)
        mostrar_pasos: si es True, imprime cada decisión del algoritmo

    Returns:
        (valor_total, lista_de_selecciones)
    """
    # Paso 1: calcular razon valor/peso y ordenar
    enriquecidos = [(p, w, n, p / w) for p, w, n in articulos]
    ordenados = sorted(enriquecidos, key=lambda x: x[3], reverse=True)

    if mostrar_pasos:
        print(f"  -> Capacidad de la mochila: W = {W}")
        print(f"  -> Ordenando articulos por razon precio/peso (descendente):")
        for p, w, n, r in ordenados:
            print(f"     {n}: precio={p}, peso={w}, razon={r:.2f}")
        print()

    valor_total = 0.0
    capacidad_restante = W
    seleccion = []

    # Paso 2: tomar greedy del articulo con mayor razon
    for p, w, n, r in ordenados:
        if capacidad_restante <= 0:
            if mostrar_pasos:
                print(f"  -> Mochila llena. {n} no se toma.")
            break

        tomar = min(w, capacidad_restante)
        valor_aporte = tomar * r
        seleccion.append((n, tomar, valor_aporte, r))
        valor_total += valor_aporte
        capacidad_restante -= tomar

        if mostrar_pasos:
            if tomar == w:
                print(f"  -> Tomar TODO {n}: {tomar} u "
                      f"(valor +${valor_aporte:.2f}) "
                      f"-> capacidad restante: {capacidad_restante}")
            else:
                print(f"  -> Tomar fraccion de {n}: {tomar} u de {w} "
                      f"(valor +${valor_aporte:.2f}) "
                      f"-> capacidad restante: {capacidad_restante}")

    return valor_total, seleccion


def mostrar_resultado(W, valor_total, seleccion):
    """Imprime la solución encontrada."""
    print(f"\n  Solucion para W = {W}:")
    print(f"  {'-' * 50}")
    for nombre, cant, val, razon in seleccion:
        print(f"    {nombre}: tomar {cant} u "
              f"(razon {razon:.2f}) -> valor ${val:.2f}")
    print(f"  {'-' * 50}")
    print(f"  VALOR TOTAL: ${valor_total:.2f}\n")


def ejecutar_caso(nombre, articulos, W):
    """Ejecuta un caso de prueba con narración paso a paso."""
    print("=" * 60)
    print(f"  CASO: {nombre}")
    print("=" * 60)
    valor, sel = knapsack_fraccionado(articulos, W, mostrar_pasos=True)
    mostrar_resultado(W, valor, sel)


if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("  PROBLEMA 2: KNAPSACK FRACCIONADO (Greedy)")
    print("#" * 60 + "\n")

    # CASO 1: ejemplo del examen
    articulos1 = [
        (60, 10, "item1"),    # razon = 6.00
        (100, 20, "item2"),   # razon = 5.00
        (120, 30, "item3"),   # razon = 4.00
    ]
    ejecutar_caso("Ejemplo del examen (W=50)", articulos1, 50)

    # CASO 2: razones distintas, capacidad ajustada
    articulos2 = [
        (500, 30, "oro"),       # razon = 16.67
        (300, 20, "plata"),     # razon = 15.00
        (150, 15, "bronce"),    # razon = 10.00
        (80, 10, "cobre"),      # razon = 8.00
    ]
    ejecutar_caso("Joyas robadas (W=40)", articulos2, 40)

    # CASO 3: caso donde caben todos los items completos
    articulos3 = [
        (200, 10, "A"),    # razon = 20.00
        (100, 5, "B"),     # razon = 20.00
        (80, 4, "C"),      # razon = 20.00
    ]
    ejecutar_caso("Razones empatadas (W=19, cabe todo)", articulos3, 19)
