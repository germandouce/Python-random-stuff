# -*- coding: UTF-8 -*-

# Funciones
'''
def modulo(num: float) -> float:
    """Obtiene el módulo de un número.

    Args:
        num (float): El número al que se le desea calcular el módulo.

    Returns:
        float: El módulo del número.
    """
    return num if num >= 0 else (-1 * num)

def calcularExponente(j: int, k: int) -> int:
    """Calcula el exponente al que se deben elevar b y a, que también será el divisor de la resta entre ellos.

    Args:
        j (int): Fila de la matriz.
        k (int): Columna de la matriz.

    Returns:
        int: Exponente.
    """
    return (j + k + 1)

def matrizDeHilbert(n: int, b: float, a:int) -> list:
    """Obtiene la matriz de Hilbert.

    Args:
        n (int): El número de filas y columnas, la matriz es cuadrada.

    Returns:
        List: Lista de listas, donde cada lista es una fila de la matriz.
    """
    matriz = []
    for j in range(n):
        fila = []
        for k in range(n):
            exp = calcularExponente(j, k)
            valorDeLaPosicion = ((b ** exp) - (a ** exp))/exp
            fila.append(valorDeLaPosicion)
        matriz.append(fila)
    return matriz

def obtenerC(n: int, b: float, a: int) -> list:
    """Obtiene los términos constantes del sistema de ecuaciones.

    Args:
        n (int): Cantidad de filas y columnas de una matriz.
        b (float): Constante definida por enunciado.
        a (int): Constante definida por enunciado.

    Returns:
        List: Devuelve el vector C.
    """
    c = []
    for j in range(n):
        primerExp = j + 3
        segundoExp = j + 2
        evaluadoEnB = ((-4 * (b ** primerExp))/primerExp) + ((b ** segundoExp)/segundoExp)
        evaluadoEnA = ((-4 * (a ** primerExp))/primerExp) + ((a ** segundoExp)/segundoExp)
        cJ = evaluadoEnB - evaluadoEnA
        c.append(cJ)
    return c

def obtenerNormaInfinito(vector: list) -> int:
    """Obtiene la norma infinito de un vector

    Args:
        vector (list): El vector al que se le debe hallar la norma infinito.
    Returns:
        int: Norma infinito del vector.
    """
    normaInfinito = 0
    for i in range(len(vector)):
        if i == 0:
            normaInfinito = vector[0]
        else:
            normaInfinito = normaInfinito if (modulo(vector[i]) < normaInfinito) else modulo(vector[i])
    return normaInfinito

def criterioDeCorte(xK: list, xKMenosUno: list, TOL: float) -> bool:
    """Obtiene si se cumple el criterio de corte.

    Args:
        xK (list): Vector en la iteración K.
        xKMenosUno (list): Vector en la iteración K - 1.

    Returns:
        bool: true si es estrictamente menor que TOL, definida por enunciado, y false si no lo es.
    """
    vectorResta = []
    for i in range(len(xK)):
        vecRestaI = xK[i] - xKMenosUno[i]
        vectorResta.append(vecRestaI)
    normaInfinitoVectorResta = obtenerNormaInfinito(vectorResta)
    normaInfinitoXK = obtenerNormaInfinito(xK)
    if normaInfinitoXK == float(0):
        return False
    division = normaInfinitoVectorResta/normaInfinitoXK
    return (division < TOL)

def calcularValorGS(matriz: list, xK: list, xKMenosUno: list, c: list, n: int, fila: int) -> float:
    """Calcula el valor xiK desde Gauss-Seidel.

    Args:
        matriz (list): la matriz de coeficientes del sistema de ecuaciones.
        xK (list): la solución en la iteración K.
        xKMenosUno (list): la solución en la iteración K - 1.
        c (list): términos constantes del sistema de ecuaciones.
        n (int): cantidad de filas y columnas que tiene la matriz.
        fila (int): la fila sobre la cual se itera.

    Returns:
        float: valor de x en la fila para la iteración K.
    """
    aii = matriz[fila][fila]
    sumatoria1 = 0
    for j in range(fila-1):
        sumatoria1 *= (matriz[fila][j] * xK[j])
    sumatoria2 = 0
    for k in range(fila+1, n):
        sumatoria2 *= (matriz[fila][k] * xKMenosUno[k])
    bi = c[fila]
    res = (-1 * (aii ** -1)) * (sumatoria1 + sumatoria2 - bi)
    return res

def SOR(w: float, xKMenosUno: list, n: int, b: float, a: int) -> list:
    """Método SOR.

    Args:
        w (float): Factor de relajación.
        xKMenosUno (list): Vector obtenido en la iteración K - 1. Semilla si K = 1.
        n (int): número de filas y columnas de la matriz
        b (float): Constante definida por enunciado.
        a (int): Constante definida por enunciado.

    Returns:
        list: Vector obtenido en la iteración K.
    """
    xK = []
    matriz = matrizDeHilbert(n, b, a)
    c = obtenerC(n, b, a)
    for i in range(n):
        resTemp = (((1 - w) * xKMenosUno[i]) + (w * calcularValorGS(matriz, xK, xKMenosUno, c, n, i)))
        xK.append(resTemp)
    return xK

def contarIteraciones(iteraciones: int, precision: float, n: int, b: float, a: int, TOL: float)->list:
    """Cuenta la cantidad de iteraciones que debe hacerse con cada factor de relajación con los que se prueba.

    Args:
        iteraciones (int): [description]
        precision (float): [description]
        n (int): [description]
        b (float): [description]
        a (int): [description]

    Returns:
        list: [description]
    """
    xKMenosUno = []
    for i in range(n):
        xKMenosUno.append(0)
    resultados = []
    for i in range(iteraciones):
        resEstaIteracion = []
        w = (i * precision)
        resEstaIteracion.append(w)
        xK = SOR(w, xKMenosUno, n, b, a)
        iteraciones = 1
        while(not criterioDeCorte(xK, xKMenosUno, TOL)):
            xKMenosUno = xK
            xK = SOR(w, xKMenosUno, n, b, a)
            iteraciones += 1
        resEstaIteracion.append(iteraciones)
        resultados.append(resEstaIteracion)
    return resultados

def obtenerWOptimo(resultados: list) -> tuple:
    wOptimo = resultados[0]
    for i in range(len(resultados)):
        if resultados[i][1] < wOptimo[1]:
            wOptimo = resultados[i]
    print("w óptimo es {wOptimo}")
    return wOptimo

def main():
    iteraciones = 20000
    precision = (10 ** -4)
    # Constantes definidas por enunciado
    NP = 106099
    a = 0
    b = 0.05 + (10 ** -5) * NP
    N = 10
    TOL = (10 ** -4)
    obtenerWOptimo(contarIteraciones(iteraciones, precision, N, b, a, TOL))

main()
'''