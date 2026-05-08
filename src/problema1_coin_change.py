"""
Problema 1: Hacer Sencillo (Coin Change)
==========================================
Universidad del Valle de Guatemala - Análisis y Diseño de Algoritmos
Examen Parcial #2

Paradigma: GREEDY
Estrategia: en cada paso, tomar la moneda de mayor denominación
            que no exceda el monto restante.

Por qué greedy funciona aquí:
- El conjunto de denominaciones {1, 5, 10, 25} es CANÓNICO
- Tiene greedy-choice property + subestructura óptima
- También se puede modelar como matroide ponderada
"""

DENOMINACIONES = [25, 10, 5, 1]  # ordenadas de mayor a menor


def hacer_sencillo(monto_centavos, mostrar_pasos=False):
    """
    Resuelve el problema de cambio de monedas con algoritmo greedy.

    Args:
        monto_centavos: monto a alcanzar, en centavos (entero)
        mostrar_pasos: si es True, imprime cada decisión del algoritmo

    Returns:
        Diccionario {denominacion: cantidad}
    """
    resultado = {}
    restante = monto_centavos

    if mostrar_pasos:
        print(f"  -> Monto inicial: {monto_centavos} centavos")

    for c in DENOMINACIONES:
        cantidad = restante // c  # cuántas monedas de c caben
        if cantidad > 0:
            resultado[c] = cantidad
            restante -= cantidad * c
            if mostrar_pasos:
                print(f"  -> Tomar {cantidad} moneda(s) de {c}c "
                      f"-> restante: {restante}c")
        else:
            if mostrar_pasos:
                print(f"  -> No caben monedas de {c}c (restante: {restante}c)")

    return resultado


def formatear_resultado(monto_centavos, resultado):
    """Imprime el resultado de forma legible."""
    print(f"\n  Monto: Q{monto_centavos/100:.2f} ({monto_centavos} centavos)")
    print(f"  {'-' * 40}")
    total_monedas = 0
    for den in sorted(resultado.keys(), reverse=True):
        cant = resultado[den]
        print(f"    {cant:>3} moneda(s) de Q{den/100:.2f}")
        total_monedas += cant
    print(f"  {'-' * 40}")
    print(f"  TOTAL: {total_monedas} monedas\n")


def ejecutar_caso(nombre, monto):
    """Ejecuta un caso de prueba con narración paso a paso."""
    print("=" * 60)
    print(f"  CASO: {nombre}")
    print("=" * 60)
    resultado = hacer_sencillo(monto, mostrar_pasos=True)
    formatear_resultado(monto, resultado)


if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("  PROBLEMA 1: HACER SENCILLO (Greedy)")
    print("#" * 60 + "\n")

    # CASO 1: ejemplo del examen
    ejecutar_caso("Ejemplo del examen - Q2.93", 293)

    # CASO 2: monto que requiere combinar varias denominaciones
    ejecutar_caso("Monto mediano - Q0.99", 99)

    # CASO 3: monto grande
    ejecutar_caso("Monto grande - Q15.67", 1567)
