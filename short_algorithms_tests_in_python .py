PYTHONDONTWRITEBYTECODE='dont whrite pychache'

#import Diccionario1
'''
n=int(input('ingrese un numero: '))
i = 2
primo = True
while(primo and i < n//2):
    if (n%i == 0):
       primo = False
    i+=1
print(bool(primo))
'''
#test de sorted
'''
l=[]
for i in range(6):
    n=input()
    l.append(n)
print(sorted(l))
'''
#test de filter
'''
l=[100,3,20]
def div(x):
    x%10==0
    return True

l=list(filter(div,l))
print(l)
'''
#programita corto para quitar doble espacio
'''
txt=input('texto a quitar doble espacio: ')
for i in range (len(txt)):
    while (txt.count('  '))>0:
        txt=txt.replace('  ',' ')
print(txt)
'''
#ej 1 hackerrank.net
'''
def fizzBuzz(n):
    # Write your code here
    n=int(input('give a number: '))
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0 and i%5!=0:
            print('Fizz')
        elif i%5==0 and i%3!=0:
            print('Buzz')
        else:
            print(i)
if __name__ == '__main__':
'''
#ej 2 hackerrank.net
'''
def triangleOrNot(a, b, c):
     
    a1=[]
    b1=[]
    c1=[]
    d=[]
    for n in range(3): 
        a1.append(a)      
        b1.append(b)
        c1.append()
        for i in range(3):
         if a1[i]>b1[i]>b1[i]:
            if b1[i]+c1[i]>a1[i]:
                d[i]='yes'
            else:
                d1[i]='no'
         elif c1[i]>b1[i]>a1[i]:
            if b1[i]+a1[i]>c1[i]:
                d[i]='yes'
            else:
                d[i]='no'           
         elif b1[i]>c1[i]>a1[c]:
            if a1[i]+c1[i]>b1[i]:
                d[i]='yes'
            else:
                d[i]='no'  

if __name__ == "__main__":
'''
#random code-snippet with switcher
'''
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
        20: 'Ginobili'
    }
    print (switcher.get(argument, "Invalid month"))
    return

a=int(input('ingrese un mes: '))
switch_demo(a)
'''
#(prueba random) imprime carita llorando print('\U0001F62D')
'''
HOLA=5
CONSTANTT=4
CONSTANTT=5
print(CONSTANT)
'''
'''
jazmín;gerez;formosa;95/n
roberto;luna;corrientes;68/n
antonio peñate río negro 83
marcelo villate santa cruz 99
joaquín;ortiz;alba;entre;ríos;88/n
mariano;villafáñez;santa;cruz;98/n
nicolás;luzuriaga;santa;cruz;97/n
agustín;méndez;formosa;77/n
'''
'''
txt=input('tx: ')
txt=txt.strip()
txt=txt.replace(' ',';')
txt=txt+'/'+'n'
print(txt)
'''
'''
dat=open('datos3.csv','r')
a=dat.readlines()
dat.close()
dat=open('datos3.csv','w')
for i in range (len(a)):
    a[i]=a[i].replace(' ',';')
    #a[i].split(';')
    dat.write(a[i])
dat.close()
'''
'''
dat=open('datos3.csv','r')
a=dat.readlines()
dat.close()
dat=open('datos3.csv','w')
dat.write(str(a))
dat.close()
'''
#saca ultima letra
'''
txt = input('ingrese texto: ')
txt=txt[:len(txt)-1] #saca ultima letra
print(txt)
'''
'''
t=[]
tabla=[1,2,3]
tabla2=[4,5,6]
#t3=t.append(tabla)
#t.append(tabla2)
t=t+tabla+tabla2
print(t)
'''
'''
#test isnumeric()
a='0'
if a.isnumeric():
    print(a)
# isnumeric() -> true if int #false 4 the rest (float or letters )
'''
#function ex
'''
num_1 = int(input('ingrese un numero: '))
num_2 = int(input('ingrese un numero: '))

def suma (n_1:int,n_2:int) -> str:
    sum = n_1 + n_2
    return sum
print(suma(num_1,num_2))
'''
'''
#old
def llorar2(msj):
    msj=msj.split()
    AlguienLlora=False
    for palabra in msj:
        if palabra.lower() in datos.quejas.values(): 
            AlguienLlora=True
            break
    return AlguienLlora
'''
#update
'''
def llorar2(msj):
    msj=msj.split()
    AlguienLlora = False
    i=0
    while AlguienLlora == False and i < (len(msj)):
        if msj[i].lower() in Diccionario1.quejas.values(): 
            AlguienLlora=True
        
        i += 1
    return AlguienLlora

msj = input('ingrese mensaje: ')
print(bool(llorar2(msj)))
'''
#prueba con enumem
'''
enum ='', '1', '2', 4, 5

for i in range (1,6):
    print(str(i),enum[i])
'''
#Casteos varios en python y practica de types - tipos (mini resumen) (list, tuple, set)
'''
conjunto_vacio = set()
conjunto_con_elementos = {1,2}
tupla = (1,2)
lista = [4,5]

#casteo lista a tupla
tupla_nueva = tuple(lista) #devuelve una lista con 4 y 5
print(tupla_nueva)

#casteo str a lista
lista_nueva = list('hola')

#casteo tupla a lista
lista_nueva_de_tupla = list(tupla)

print(lista_nueva)
print(lista_nueva_de_tupla)

#print(conjunto_con_elementos[0]) #tira error set no no es subciptable
print(tupla[0])  #devuelve 1
print(lista[1])  #devuelve 2

print(type(conjunto_vacio))
print(type(conjunto_con_elementos))
print(type(tupla))
print(type(list))
'''
#ejemplo numerico
'''
n=10
xKMenosUno = []
for i in range(n):
    xKMenosUno.append(0)
print(xKMenosUno)
'''
#ejemplos de busqueda
'''
def llorar2(msj):
    llorar = False
    for queja in Diccionario1.quejas.values():
        if msj.find(str(queja)) >-1 and llorar == False:
            llorar = True
            print(bool(llorar))
    return llorar

msj = input()
if llorar2(msj) == True:
    print('lloro')
'''
'''
def llorar2(msj):
    llorar = False
    for queja in Diccionario1.quejas.values():
        if queja in msj and llorar == False:
            llorar = True
    return llorar

msj = input()
if llorar2(msj) == True:
    print('lloro')
'''
#ejemplo de pasaje x referencia
'''
def modifica_lista_1(l):
    l[0] = 'modif'
l = [1,2,3]

modifica_lista_1(l)
print(l)

#ejemplo de pasaje x valor
def modifica_lista_2(l):
    l ='modif'
    return l

l = [1,2,3]
l_modif = modifica_lista_2(l)
print(l_modif)
'''

#creacion de tablero
'''
tablero_1=[]
for columna in range(4):
    tablero_1.append([])
    for fila in range(4):
        tablero_1[columna]=[' ']*4
for columna in tablero_1:
    print(columna)

print()
'''
'''
l=[]
for i in range(4):
  l.append([])
for i in range(4):
  l[i]=[' ']*4
for i in range(4):
    print (l[i])
'''
'''
tablero_1=[]
for fila in range(4):
    tablero_1.append([])
    for columna in range(4):
        tablero_1[fila].append('  1  ')   
''' 
'''
for fila in tablero_1:
    print(fila)
print(tablero_1)
print(tablero_1[fila])
'''
'''
for i in range(4):
    for j in range(4):
        print(tablero_1[i][j], end =' ')
    print()
'''
'''
tam_matriz = int(input('ingrese tamano: '))

matriz_identidad_1 = []
for i in range(tam_matriz):
    fila = []
    for j in range(tam_matriz):
        if i == j:
            fila.append('1')
        else:
            fila.append('0')
    matriz_identidad_1.append(fila)
#tam_matriz = int(input('ingrese tamano: '))

matriz_identidad = []
for fila in range(tam_matriz):
    matriz_identidad.append([])
    for columna in range(tam_matriz):
        if fila == columna:
            matriz_identidad[fila].append('1')
        else:
            matriz_identidad[fila].append('0')

for i in range(tam_matriz):
    print(matriz_identidad_1[i],)
    print("\n")

print('la otra')

for i in range(tam_matriz):
    for j in range(tam_matriz):
        print(matriz_identidad[i][j],end="   ")
    print("\n")
'''
'''
for i in range(n): 
    for j in range (n): 
        print(matriz[i][j]) # seteale el end a tab acá
    print(salto de línea)
'''
'''
for i in range(tam_matriz):
    for j in range(tam_matriz):
        print(matriz_identidad[i][j], end=",")
    print("\n")
'''
'''
for i in range(tam_matriz):
    for j in range(tam_matriz):
        nuevo_elemento = input('ingrese numero: ')
        matriz_identidad[i][j] = nuevo_elemento
'''

#cargar tablero

#from random import randint
#import random

from random import choice, shuffle
from random import randint
'''
tam_matriz = int(input('tamaño: '))

tablero_1=[]
for fila in range(tam_matriz):
    tablero_1.append([])
    for columna in range(tam_matriz):
        tablero_1[fila].append('')

print('tablero vacio\n')
for i in range(4):
    for j in range(4):
        print(tablero_1[i][j], end ='   ')
    print()


elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge',
'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 
'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']

elementos_xa_tablero =[]

for i in range(int((tam_matriz**2)/2)):
    elegido = choice(elementos)
    elementos_xa_tablero.append(elegido)
    elementos_xa_tablero.append(elegido)
    elementos.pop(elementos.index(elegido))

print(int((tam_matriz**2)/2))
shuffle(elementos_xa_tablero)
print(elementos_xa_tablero)

indice = 0
for fila in range(tam_matriz):
    for columna in range(tam_matriz):
        tablero_1[fila][columna] = elementos_xa_tablero[indice]
        indice += 1 

print('tablero cargado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()

'''
#xa copiar elementos mas facil
'''
dat=open('elementos.txt')
a=dat.readlines()
dat.close()
for ele in a:
    ele=ele[:2]
    print(f" '{ele}', ",end ='')
'''

#no sirve
'''
elementos = ['a','b','c','d','e','f','g','h']
indice = [1,2,3,4,5,6,7,8,]
ya_elegidos = []
for indice in range(indice):
    ya_elegidos.append(elementos[indice])
    
for fila in range(4):
    for columna in range(4):
        tablero_1[fila][columna] = 5

'''
#chequeo eles repes
'''
elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 
    'S', 'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 
    'Ga',  'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 
    'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 'Pb', 
    'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']

for ele in elementos:
    if elementos.count(ele)>1:
        print('cuidad0',ele, 'duplicado!')
    
print('Todo OK!, No hay duplicados')
'''
'''
#ejemplo de uso de pass
def prueba (a):
    pass

b=4
prueba(b)
print('hola')
'''
#recomendacion guido xa convertir letras a indices

#Version ingenieri

'''
print(ord("a"))
print(ord("b"))
coord = input("Ingrese primer coordenada (a-z)")
print(ord(coord)-97)

#Version rudimentaria
dicconver = {"a":0,"b":1}
print(dicconver["a"])
'''

#creacion de tablero

'''
tablero_1=[]
for fila in range(tam_matriz):
    tablero_1.append([])
    for columna in range(tam_matriz):
        tablero_1[fila].append('')
'''
#carga con randint
'''
tam_matriz = int( (input('tamaño: ') ) )

elementos = ['A','B','C','D','E','F','G','H','I','J','K','L']

elementos_xa_tablero = []

for i in range( int( (tam_matriz**2) /2 ) ):

        indice = randint(0,len(elementos)-1)
        
        elegido = elementos[indice]
        elementos.pop(indice)

        elementos_xa_tablero.append(elegido)
        elementos_xa_tablero.append(elegido)

print(elementos_xa_tablero)

for fila in range (tam_matriz):
    for columna in range (tam_matriz) :
        indice = randint (0,len(elementos_xa_tablero)-1)
        tablero_1[fila][columna] = [elementos_xa_tablero [indice],'*']
        elementos_xa_tablero.pop(indice)                              
        

for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j][0], end =' ')
        print()
'''        
#carga con shuffle
'''

tam_matriz = int( (input('tamaño: ') ) )

elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge',
'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 
'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']
'''
'''
elementos_xa_tablero =[]

for i in range(int((tam_matriz**2)/2)):
    elegido = choice(elementos)
    elementos_xa_tablero.append(elegido)
    elementos_xa_tablero.append(elegido)
    elementos.pop(elementos.index(elegido))

print(int((tam_matriz**2)/2))
shuffle(elementos_xa_tablero)
print(elementos_xa_tablero)
'''
#carga con randint
'''
elementos = ['A','B','C','D','E','F','G','H','I','J','K','L']

elementos_xa_tablero = []

print(len(elementos))
for i in range(int((tam_matriz**2)/2)):
        indice = randint(0,len(elementos)-1)

        elegido = elementos[indice]
        elementos.pop(indice)

        elementos_xa_tablero.append(elegido)
        elementos_xa_tablero.append(elegido)

print(elementos_xa_tablero)

#shuffle(elementos) #shuffle es un metodo, no devuelve nada.
#choice es una funcion, devuelve un elemento random del coajunto

for fila in range(tam_matriz):
    for columna in range(tam_matriz):
        indice = randint(0,len(elementos_xa_tablero)-1)
        tablero_1[fila][columna] = [elementos_xa_tablero[indice],'*']
        elementos_xa_tablero.pop(indice)                              
        
        #en la pos i,j meto una lista con 2
                #elementos, el 1ero la ficha el 2do un indicador de si fue adivinada o no
                            # * signfica NO adiviado. ' ', ya adivinada

print('tablero cargado\n')

for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j][0], end =' ')   #[1] es el indicador de adivinado
        print()
'''
'''
# print('tablero cargado\n')
# for i in range(tam_matriz):
#         for j in range(tam_matriz):
#             if tablero_1[i][j][1] == ' ':   #[1] es el indicador de adivinado
#                 print(tablero_1[i][j][0].ljust(2), end ='  ')
#             else:
#                 print('*'.ljust(2), end = '  ')
#         print()

# print(tablero_1)

def ingreso_coordendas() -> tuple:
    """
    POST: devuelve una tupla con las coordenadas escritas como enteros correspondientes a la matriz
    """
    fila = int(input('ingrese fila: ')) - 1     #resto 1 puesto que en las listas de lisats 
    columna =  int(input('ingrese columna: ')) -1 #del tablero estas empiezan con indice "0"
    return fila, columna


def chequeo(tablero_1:list, carta_1:tuple, carta_2: tuple) -> bool:
    """
    POST: devuelve el bool perdio, (por si o por no). si no
    perdio, además desbloquea esa ficha del tablero
    """
    perdio = True
    print(carta_1[0] +1, carta_1[1] +1)
    print(carta_2[0] +1, carta_2[1] +1)
    if ( tablero_1[ carta_1[0] ][ carta_1[1] ] ) == ( tablero_1 [ carta_2[0] ][ carta_2[1] ] ) :
        
        tablero_1 [ carta_1[0] ][ carta_1[1] ] [1] = ' '   #si adivino, cambio * por espacio ' '
        tablero_1 [ carta_2[0] ][ carta_2[1] ] [1] = ' '
        perdio = False
        print('Adivino!, puede jugar de nuevo')
    
    return perdio

def no_gano_el_juego(tablero_1):
    """
    PRE: trae el tablero
    POST: devuelve el bool no_gano_juego, True si no gano, Falso si gano
    """
    #hago algunos comentarios xa mejor comprension
    no_gano_juego = False
    #es decir, es verdadero que alguien gano
    for i in range(tam_matriz):
            for j in range(tam_matriz):   
                if tablero_1[i][j][1] == '*': #si llego a encontrar un *, es decir, un NO ADIVINADO
                    #entonces, es falso que alguien gano. En ese caso, 
                    no_gano_juego = True    #es valido decir q no gano nadie                   

    return no_gano_juego


def hacer_memoria(tablero_1) -> bool:
    """
    """
    no_gano_juego= True    #lo llevo por la positiva para facilitar la funcion no_gano_el_juego
    perdio = False
    while not perdio and no_gano_juego:
        print('tablero modificado\n')
        for i in range(tam_matriz):
                for j in range(tam_matriz):
                    if tablero_1[i][j][1] == ' ':   #[1] es el indicador de adivinado
                        print(tablero_1[i][j][0].ljust(2), end ='  ') #[0] es el indicador de adivinado
                    else:
                        print('*'.ljust(2), end = '  ')
                print()

        print(tablero_1)

        print('ingrese coordendas carta 1')
        carta_1 = ingreso_coordendas()

        print('ingrese coordendas carta 2')
        carta_2 = ingreso_coordendas()

        while carta_1 == carta_2:           #no quiero q ingrese 2 veces las mismas
            print('Por ingrese coordenadas distintas')   #coordenadas xq me 
                                                        #destapa la carta. Tambien lo obligo a dar 
            print('ingrese coordendas carta 1')     # vuelta ambas cartas  "a la vez"

            carta_1 = ingreso_coordendas()      
            print('ingrese coordendas carta 2')
            carta_2 = ingreso_coordendas()                   
        
        perdio = chequeo(tablero_1, carta_1, carta_2)
        
        no_gano_juego = no_gano_el_juego(tablero_1)
    
    return no_gano_juego

def jugando(tablero_1):
    no_gano = True
    while no_gano:
        turno = 0
        while turno !=2 and no_gano:
            print(turno)
            if turno == 0:
                print('trablero 1')
                tablero = tablero_1
            else:
                print('tablero 2')
                tablero = tablero_1
            no_gano = hacer_memoria(tablero)
            # levantar_carta()
            # guardar_carta()
            # jugar_carta()
            turno += 1

jugando(tablero_1)
'''
#random test
'''
import random

a = random.randint(1,10)
print(a)
'''
#Espejar filas y columnas
#Juego cart TOTI
'''
tam_matriz = int(input('tamaño: '))

tablero_1=[]
for fila in range(tam_matriz):
    tablero_1.append([])
    for columna in range(tam_matriz):
        tablero_1[fila].append('')

elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge',
'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 
'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']
'''
'''
elementos_xa_tablero =[]

for i in range(int((tam_matriz**2)/2)):
    elegido = choice(elementos)
    elementos_xa_tablero.append(elegido)
    elementos_xa_tablero.append(elegido)
    elementos.pop(elementos.index(elegido))

print(int((tam_matriz**2)/2))
shuffle(elementos_xa_tablero)

indice = 0
for fila in range(tam_matriz):
    for columna in range(tam_matriz):
        tablero_1[fila][columna] = elementos_xa_tablero[indice]
        indice += 1 

print('tablero cargado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()

sentido = randint(1,2)
#if sentido == 1:
'''
#HORIZONTAL//
'''
filas_aux = []

for fila in range( len(tablero_1)): # fila: 0, 1, 2, 3, 4, 5, 6, 7
    if fila < (len(tablero_1) / 2):
        filas_aux.append(tablero_1 [fila])
        tablero_1[fila] = tablero_1 [ len(tablero_1)-1 - fila ]
        #print(tablero_1[fila])             8      

    else:
        tablero_1[fila] = filas_aux [len(tablero_1)-1 - fila]

#for fila in filas_aux:
#print(filas_aux[0])

print('tablero espejado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()
'''
#VERTICALEMENTE
'''
for fila in range( len(tablero_1)): # fila: 0, 1, 2, 3, 4, 5, 6, 7
    
    columnas_aux = []
    
    for columna in range ( len(tablero_1) ):    #columna: 0, 1, 2, 3, 4, 5, 6, 7
        if columna < (len(tablero_1) / 2):
            columnas_aux.append (tablero_1 [fila][columna] )    
            tablero_1 [fila][columna] = tablero_1 [fila][ len(tablero_1) - 1 - columna]
        
        else:
            tablero_1 [fila][columna] = columnas_aux [ len(tablero_1) - 1 - columna ]

        #print(tablero_1[fila])             8    

print('tablero espejado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()  
'''
#Trasposicion de matrices
#CARTA FATALITY 
'''
matriz = []

for i in range(4):
    matriz.append([])
    for j in range(4):
        if i==0:
            matriz[i].append('A')
        else:
            matriz[i].append('1')

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end =' ')
    print()

aux=[ ["a"]*len(matriz) ] *len(matriz[0])

print(aux)
for i in range(len(aux)):
   for j in range(len(aux[i])):
       aux[i][j] = matriz[j][i]

print()

for i in range(4):
    for j in range(4):
        print(aux[i][j], end =' ')
    print()
'''

#TRSPOSICION de tablero
'''
tam_matriz = int(input('tamaño: '))

tablero_1=[]
for fila in range(tam_matriz):
    tablero_1.append([])
    for columna in range(tam_matriz):
        tablero_1[fila].append('')

elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge',
'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 
'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']


elementos_xa_tablero =[]

for i in range(int((tam_matriz**2)/2)):
    elegido = choice(elementos)
    elementos_xa_tablero.append(elegido)
    elementos_xa_tablero.append(elegido)
    elementos.pop(elementos.index(elegido))

print(int((tam_matriz**2)/2))
shuffle(elementos_xa_tablero)

indice = 0
for fila in range(tam_matriz):
    for columna in range(tam_matriz):
        tablero_1[fila][columna] = elementos_xa_tablero[indice]
        indice += 1 

print('tablero cargado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()
'''

#METODO XA COPIAR TABLERO SIN HACER CAGADA
#el metodo .copy() hace q siga apuntando a la misma direc de memoria!!! NO USAR!!!

'''

l=[[1],[2],[3]]


print(l)
#print('tras',tablero_traspuesto)

l_copiada = []
for i in range(3):
    l_copiada.append (['A'])

for i in range (len(l)):
    for j in range(1):
        l_copiada [i][j] = l[i][j]

l_copiada [0][0]= 0    
l_copiada [1][0] =0


#print('tras dsps',tablero_traspuesto)

print(l_copiada)
print('original',l)

l=[[1],2,3]
print(l)
l_copiada [0][0]=0
l_copiada [1] = 0
print(l)

'''
#NO HACER !!!
'''
tablero_traspuesto = tablero_1.copy()

'''
#HCAER ASI!!
'''
#creo tablero aux xa colocar la traspuesta en el

def traspongo(tablero_1):

    tablero_traspuesto = []    #creo un tablero aux de nuevo. Intente usar el metodo .copy() pero me tocaba el 
    for fila in range():      #tabelro original
        tablero_traspuesto.append([])
        for columna in range(tam_matriz): 
            tablero_traspuesto[fila].append('AUX')

    #print('tablero traspuesto aux')
    #print(tablero_traspuesto)
    #print(tablero_1)
    #copio la traspuesta en el


    for fila in range( len(tablero_traspuesto) ):
            for columna in range( len(tablero_traspuesto) ):
                tablero_traspuesto[fila][columna] = tablero_1[columna][fila]
                #la columna de la traspuesta, es la fila de la original y viceversa
    
    print('tablero traspuesto\n')
    for fila in range( len(tablero_traspuesto) ):
            for columna in range( len(tablero_traspuesto) ):
                print(tablero_traspuesto[fila][columna], end ='  ' )
            
            print()
    
    return tablero_traspuesto

tablero_1 = traspongo(tablero_1)

print('tablero_1 dsps de espejar FUERRA DE TRASPONGO')
for i in range( tam_matriz ):
    for j in range( tam_matriz ):
        print(tablero_1[i][j], end ='  ' )
            
    print()
'''
#pavadita de orden...
'''
elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
    'Mg', 'Al', 'Si', 'P', 'S', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'U', 'Y', 'Rf',
    'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge', 'As', 'Se', 
    'Br', 'Kr', 'Rb', 'Sr', 'Cl', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 
    'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu',
    'Pt', 'Au', 'Hg', 'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'Zr', 'Np','Es']

print(len(elementos))
'''
#BUEN DATO DE FUNCIONES EN PYTHON
#OJO MYPY NO DETECTA ESTO!!!
'''
def n_n (n:str) -> None:
    print(n)
    
    #return n
    #si no pongo return, devuelve predeterminadamente None

a = n_n('hola') #a = None
print(a)    #imprime None
'''
'''
def imprimo(tupla):
    print(tupla[1])

l =list()
imprimo ( (l,2) )
'''
#practica simple con paaremtro sep de print
'''
cadena = 'hola'

for letra in cadena:
    print(letra,'_', sep ='', end='')
'''
#VALIDADOR DE OOPCIONES SUPER UTIL XA PARCIAL (y xa todo en realidad)!!!
'''
def validar_opcion(opc_minimas: int, opc_maximas: int, texto: str = '') -> str:
    """
    PRE: "opc_minimas" y "opc_maximas" son dos números enteros que 
    simbolizan la cantidad de opciones posibles.

    POST: Devuelve en formato string la var "opc" con un número 
    entero dentro del rango de opciones.
    """
    opc = input("{}".format(texto))
    while not opc.isnumeric() or int(opc) > opc_maximas or int(opc) < opc_minimas:
        opc = input("Por favor, ingrese una opcion valida: ")
    
    return opc
'''
#DICCIONARIOS!!

#ej. de como appendearle un ele a una lista que esta com valor del diccionario:
'''
dict = {}
dict['hola'] = []
dict['hola'].append('a')
dict['hola'].append('pepe')
print(dict)
'''
#OJO al comparar strings no olvidar el .lower() o .upper() !!!!
 