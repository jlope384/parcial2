# Examen Parcial #2 - Analisis y Diseno de Algoritmos

Implementacion en Python de tres problemas vistos en el parcial, con enfoque en el paradigma correspondiente a cada uno:

- Problema 1: Coin Change con estrategia greedy.
- Problema 2: Knapsack fraccionado con estrategia greedy.
- Problema 3: Combinaciones en teclado Nokia 3230 con programacion dinamica bottom-up.

## Estructura

- [src/problema1_coin_change.py](src/problema1_coin_change.py)
- [src/problema2_knapsack.py](src/problema2_knapsack.py)
- [src/problema3_nokia.py](src/problema3_nokia.py)
- [docs/demostraciones.md](docs/demostraciones.md)

## Requisitos

- Python 3.10 o superior.
- No se requieren dependencias externas.

## Ejecucion

Desde la raiz del proyecto puedes ejecutar cada problema por separado:

```bash
python src/problema1_coin_change.py
python src/problema2_knapsack.py
python src/problema3_nokia.py
```

Cada script incluye casos de prueba y una salida paso a paso para mostrar el funcionamiento del algoritmo.

## Demostraciones

La justificacion teorica de cada solucion esta en [docs/demostraciones.md](docs/demostraciones.md).

## Contenido de cada script

- `problema1_coin_change.py`: calcula el cambio usando denominaciones canonicas y devuelve cuantas monedas usar.
- `problema2_knapsack.py`: ordena articulos por razon valor/peso y toma fracciones hasta llenar la mochila.
- `problema3_nokia.py`: cuenta combinaciones validas de digitos usando una tabla DP construida de abajo hacia arriba.

# Link al video:
https://drive.google.com/drive/folders/1SSjSM8FV0eBmizx4OPwL6Cly5Q0V8Zcf?usp=sharing 