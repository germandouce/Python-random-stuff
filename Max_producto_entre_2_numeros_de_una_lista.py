#Programa xa hallar el maximo producto entre 2 numeros de una lista

#GRAN bichada para ingresar solo numeros y poder cortar con cualquier otra cosa
def max_producto(numeros):
    print('productos')
    for i in range(len(numeros)):
        for restante in range (i+1,len(numeros)):
            producto = numeros[i]*numeros[restante]
            if restante == 1:
                mayor = producto
            else:
                if producto >= mayor:
                    mayor = producto
    print('el mayor producto es',mayor)
    return mayor

def ingreso():
    print('Ingrese numeros corte con cualquier letra: ')
    numeros = []
    n = input()
    while n.strip('-').isnumeric():
        numeros.append(int(n))
        n = input()
    return numeros

def main():
    print('Devuelve el mayor producto entre 2 de los numeros ingresados')
    numeros = ingreso()
    print("Numeros ingresados:")
    print(numeros)
    if numeros:        #in python empty lists evaluate False, and non-empty lists evaluate True 
        max_producto(numeros)
    else:
        print('No se ingresaron numeros')
main()

