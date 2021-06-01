# Hacer un programa python que emule un juego donde la computadora tira un dado , y el usuario debe 
# adivinar el resultado. Si la respuesta es exacta , imprimir que ganó, de lo contrario la maquina 
# da hasta dos oportunidades mas. La computadora debe dar información acerca de si el número sacado 
# en dado es mayor que la respuesta de la persona , y en tal caso esta debe reorientar la nueva 
# resp. similarmente si el resultado es menor que el nro dado por la persona.

'''Modificar el programa subido de adivinar numero de un dado. de modo que solo permita dos intentos
mas a lo sumo. Luego del primer intento. Que informe en caso de fallar al usuario, desde que nro 
tiene sentido dar prox rta.'''

from random import randint
def juego_aleatorio():
    veces=1
    nro_del_dado=randint(1,6)  #aca decia (1,7) un dado tiene 6 caras no 7
    nro_ingresado=int(input("Ingrese un nro entre 1 y 6:"))
    

    while(nro_ingresado<1) or (nro_ingresado>6):
        print("Ud ingreso un nro que no es mayor que 1 o no es menor que 6")
        nro_ingresado=int(input("Ingrese un nro entre 1 y 6:"))
    
    while(nro_ingresado!=nro_del_dado)and(veces != 3): #en vez de <3 !=3 es lo mismo
        if nro_ingresado>nro_del_dado:
            print("El nro ingresado es mayor al nro arrojado por el dado:")
        
        elif nro_ingresado<nro_del_dado:
            print("El nro ingresado ES MENOR al nro arrojado por el dado:")
        
        nro_ingresado=int(input("Ingrese un nro entre 1 y 6:"))
        veces=veces+1 
    
    if(nro_ingresado==nro_del_dado):    # o el numero es =
        print("Exito , es el nro")
        print('Uso', veces, 'intentos')
    
    else:                               #o es distinto, en ese caso,
        print("Se excedio de las veces permitidas , siendo:",veces)
        print("El nro fue el :",nro_del_dado)

juego_aleatorio()

    
    
        
    
    
    
    

