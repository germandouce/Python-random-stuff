def gs(n: int, b: float, a: int, xKMenosUno: list, precision: int) -> list:
    """Obtiene el vector xK a través de Gauss Seidel.

    Args:
        n (int): cantidad de filas y columnas que tiene la matriz.
        b (float): Constante definida por enunciado.
        a (int): Constante definida por enunciado.
        xKMenosUno (list): x obtenido en la iteración anterior.
        precision (int): precisión con la que se desea trabajar.

    Returns:
        list: x obtenido en la iteración.
    """
    matriz = matrizDeHilbert(n, b, a, precision)
    c = obtenerC(n, b, a, precision)
    xK = []
    for x in range(len(matriz[0])):
        xK.append(0)
    for i in range(len(matriz)):
        aii = matriz[i][i]
        bi = c[i]
        sumatoria1 = 0
        sumatoria2 = 0
        for j in range(i):
            sumatoria1 += (matriz[i][j] * xK[j])
        for k in range(i + 1, len(matriz[i])):
            sumatoria2 += (matriz[i][k] * xKMenosUno[k])
        xKi = round(((bi - sumatoria1 - sumatoria2) / aii), precision)
        xK[i] = xKi
    return xK