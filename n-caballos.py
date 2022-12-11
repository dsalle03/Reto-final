from __future__ import annotations


def funcion_1(posicion: tuple[int, int], n: int) -> list[tuple[int, int]]:
    y, x = posicion
    posiciones = [
        (y +1, x+2),
        (y +1, x-2),
        (y -1, x+2),
        (y -1, x-2),
        (y +2, x+1),
        (y +2, x-1),
        (y -2, x+1),
        (y -2, x-1),
    ]
    posibles_soluciones = []
    for posicion in posiciones:
        y_test, x_test = posicion
        if 0<= y_test < n and 0<= x_test < n:
            posibles_soluciones.append(posicion)

    return posibles_soluciones

def funcion_2 (tablero: list[list[int]]) -> bool:
    return not any(elementos == 0 for filas in tablero for elementos in filas)

def funcion_3(
    tablero: list[list[int]], posicion_2: tuple[int,int], curr: KeyboardInterrupt
) -> bool:

    if funcion_2(tablero):
        return True

    for posicion in funcion_1(posicion_2, len(tablero)):
        y, x = posicion
        if tablero[y][x] == 0:
            tablero[y][x] = curr + 1
            if funcion_3(tablero, posicion, curr+1):
                return True
            tablero[y][x] = 0
    
    return False

def funcion_4(n:int) -> list[list[int]]:
    tablero = [[0 for i in range(n)] for j in range (n)]

    for i in range(n):
        for j in range(n):
            tablero[i][j] = 1
            if funcion_3(tablero, (i, j), 1):
                return tablero
            tablero[i][j] = 0
    
    raise ValueError(f"No se puede realizar en un tablero de tamaño {n}")

if __name__ == "__name__":
    import doctest
    doctest.testmod()


