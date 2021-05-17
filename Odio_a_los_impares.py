#ODIO A LOS IMPARES
'''Crear un programa que:
Permita ingresar 5 números enteros positivos.
Calcule el máximo entre esos números; lo muestre.
Calcule el mínimo; lo muestre.
Calcule el promedio; lo muestre.
Sume el máximo, el mínimo; y el promedio (Resultando en un entero. Para eso pueden castear 
el resultado a int. Ejemplo: int(resultado)) y en caso de que el resultado sea par; 
salude al usuario tantas veces como número resultante de esa cuenta, si es impar; 
vuelve a empezar *ToDo* el programa DE NUEVO.'''

def ingreso() -> int:
    #PRE:
    #POST: devuelve un numero entero positivo 
    num = int(input('Ingrese numero: '))
    while num <= 0 or num % 1 != 0:
            num = int(input('OJO, debe ser entero positivo: '))
    return num


def max_y_min (num: int, maximo:int, minimo:int) -> tuple:
    #PRE: num es un numero entero positivos
    #POST: devuelve el maximo y el minimo numero cargado hasta el momento
    if num >= maximo:
        maximo = num

    if num <= minimo:
        minimo = num
    
    return maximo, minimo


def promedio_num(suma_num) -> float:
    #PRE: suma_num es la suma de los 5 numeros enteros positivos ingresados
    #POST: devuelve el promedio de esos 5 numeros como float 
    promedio = suma_num/5
        
    return promedio


def suma(maximo:int, minimo: int, promedio: float) -> float:
    #PRE: maximo y minimo son enetros positivos, promedio es un float
    #devuelve un float resultado de la suma de los parametros ingresados:
    total = maximo + minimo + promedio

    return total


def mostrar(maximo:int, minimo:int, promedio:int) -> None:
    #PRE: maximo minimo y promedio son enetros previamente calculados
    #POST: muestar por panatallo lo siguiente:
    print()
    print(f"El máximo es {maximo}")
    print(f"El mínimo es {minimo}")
    print(f"El promedio es {promedio}")
    print()


def es_par(suma_total: int) -> bool: 
    #PRE: suma_total es un entero
    #POST: devuelve un booleano dependiendo si es par o no
    lo_es = True
    if suma_total %2 != 0:
        lo_es = False

    return lo_es


def main() -> None:
    print("ODIO A LOS IMPARES")
    print()
    print('Ingrese 5 numeros enteros positivos')

    for i in range(5):
        num = ingreso()
        if i == 0:
            maximo = num
            minimo = num
            suma_num = 0
        suma_num += num #me parecio demasiado crear un funcion especial xa sumar los numeros ingresados
        maximo, minimo = max_y_min(num, maximo, minimo)

    promedio = promedio_num(suma_num)
    suma_total = int(suma(maximo, minimo, promedio)) #casteo a entero aqui

    mostrar(maximo, minimo, int(promedio))

    if es_par(suma_total):
        for i in range(suma_total):
            print('hola, ', end = '')
    else:
        main()

main()