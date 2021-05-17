conjunto_vacio = set()
conjunto_con_elementos = {1,2}
tupla = (1,2)
lista = [4,5]

#casteo lista a tupla
tupla_nueva = tuple(lista) #devuelve una tupla con 4 y 5
print(tupla_nueva)

#casteo str a lista
lista_nueva_de_str = list('hola')
print(lista_nueva_de_str)

#casteo tupla a lista
lista_nueva_de_tupla = list(tupla) #devuelve lista con 1 y 2
print(lista_nueva_de_tupla)

#print(conjunto_con_elementos[0]) #tira error set no no es subciptable
print(tupla[0])  #devuelve 1
print(lista[1])  #devuelve 5

'''
print(type(conjunto_vacio))
print(type(conjunto_con_elementos))
print(type(tupla))
print(type(list))
'''