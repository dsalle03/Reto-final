from __future__ import annotations

def busqueda(
    posible_tablero: list[int], 
    derecha: list[int], 
    izquierda: list[int], 
    tableros: list[list[str]], n:int,
) -> None:
    
    filas = len(posible_tablero)
    if filas == n:
        tableros.append([". " * i + "Q " + ". " * (n - 1 - i) for i in posible_tablero])
        return
    
    for columnas in range(n):
        if (
            columnas in posible_tablero 
            or filas-columnas in derecha 
            or filas + columnas in izquierda
        ):
                continue

        busqueda(
            posible_tablero+[columnas], 
            derecha +[filas-columnas], 
            izquierda + [filas+columnas], 
            tableros,
            n,
        )

def solucion(n:int) -> None:
    tableros: list[list[str]] = []
    busqueda([],[],[], tableros, n)

    for tablero in tableros:
        for columnas in tablero:
            print(columnas)
        print("")
    
    print("El número de posibles soluciones es", len(tableros))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    solucion(15)